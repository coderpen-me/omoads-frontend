from django.db.models import Q
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from models import Book, Banner
from forms import filterForm, signupForm

def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
		Q(title__icontains=query) |
		Q(authors__first_name__icontains=query) |
		Q(authors__last_name__icontains=query)
		)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("search/search.html", {
		"results": results,
		"query": query,
	})


def index(request):
	form = filterForm(request.GET)
	
	print(form.is_valid())
	if form.is_valid():
		type_banner_input_list = [ str(x) for x in form.cleaned_data['type_banner'] ]
		lighted_banner_input_list = [ str(x) for x in form.cleaned_data['lighted_banner'] ]
		dimensions_banner_input_list = [ str(x) for x in form.cleaned_data['dimensions_banner'] ]
		if form.cleaned_data['min_cost_banner']: 
			min_cost_banner = [float( form.cleaned_data['min_cost_banner'] )]
		else:
			min_cost_banner = []
		if form.cleaned_data['max_cost_banner']:
			max_cost_banner = [float( form.cleaned_data['max_cost_banner'] )]
		else:
			max_cost_banner = []
		
		# print(str(lighted_banner_input_list) + str(dimensions_banner_input_list) + str(type_banner_input_list))
		
		# To create the if - else filter logic using 3 separate Q()
		# qset ANDing for different criteria
		# qset Oring for options within same criteria
		qset_type = Q()
		qset_light = Q()
		qset_dimensions = Q()
		qset_all = Q()
		qset_min_cost = Q()
		qset_max_cost = Q()

		# print(form.type_banner)

		if type_banner_input_list:
			for type_banner_input in type_banner_input_list:
				qset_type = qset_type | Q( banner_type__icontains = type_banner_input )

		if lighted_banner_input_list:
			for lighted_banner_input in lighted_banner_input_list:
				qset_light = qset_light | Q( banner_lighted__icontains = lighted_banner_input )

		if min_cost_banner:
			qset_min_cost = Q( banner_cost__gte = min_cost_banner[0])

		if max_cost_banner:
			qset_max_cost = Q( banner_cost__lte = max_cost_banner[0])


		if dimensions_banner_input_list:
			for dimensions_banner_input in dimensions_banner_input_list:
				qset_dimensions = qset_dimensions | Q( banner_dimensions__icontains = dimensions_banner_input )

		qset_all = qset_dimensions & qset_light & qset_type & qset_max_cost & qset_min_cost

		results = Banner.objects.filter(qset_all)
		all_banner = Banner.objects.all()

		locations = []
		for result in results:
			locations.append( {"lng": result.banner_longitude, "lat": result.banner_lattitude}     )
			# print( str( locations ) )

	return render( request, 'index.html', {'form': form, 'result': results, 'all': all_banner, 'locations': locations})

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form': form})