from django.shortcuts import render, Http404

from django.shortcuts import render, HttpResponse, Http404
from django.http import HttpResponseBadRequest

from django.db.models import Q
import json
# Create your views here.

from marketing.forms import EmailForm
from marketing.models import MarketingMessage, Slider

from .forms import filterForm
from .models import Product, ProductImage, Banner



def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query': q, 'products': products}
		template = 'products/results.html'	
	else:
		template = 'products/home.html'	
		context = {}
	return render(request, template, context)


def home(request):
	sliders = Slider.objects.all_featured()
	products = Product.objects.all()
	template = 'products/home.html'	

	form = filterForm(request.GET)

	print(form.is_valid())
	if form.is_valid():
		type_banner_input_list = [str(x) for x in form.cleaned_data['type_banner']]
		lighted_banner_input_list = [str(x) for x in form.cleaned_data['lighted_banner']]
		dimensions_banner_input_list = [str(x) for x in form.cleaned_data['dimensions_banner']]
		if form.cleaned_data['min_cost_banner']:
			min_cost_banner = [float(form.cleaned_data['min_cost_banner'])]
		else:
			min_cost_banner = []
		if form.cleaned_data['max_cost_banner']:
			max_cost_banner = [float(form.cleaned_data['max_cost_banner'])]
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
				qset_type = qset_type | Q(banner_type__icontains=type_banner_input)

		if lighted_banner_input_list:
			for lighted_banner_input in lighted_banner_input_list:
				qset_light = qset_light | Q(banner_lighted__icontains=lighted_banner_input)

		if min_cost_banner:
			qset_min_cost = Q(banner_cost__gte=min_cost_banner[0])

		if max_cost_banner:
			qset_max_cost = Q(banner_cost__lte=max_cost_banner[0])

		if dimensions_banner_input_list:
			for dimensions_banner_input in dimensions_banner_input_list:
				qset_dimensions = qset_dimensions | Q(banner_dimensions__icontains=dimensions_banner_input)

		qset_all = qset_dimensions & qset_light & qset_type & qset_max_cost & qset_min_cost

		results = Banner.objects.filter(qset_all)
		all_banner = Banner.objects.all()

		locations = []
		for result in results:
			locations.append({"lng": result.banner_longitude, "lat": result.banner_lattitude, "id":result.id})
		# print( str( locations ) )

	context = {
		"products": products,
		"sliders": sliders,
		'form': form,
		'result': results,
		'all': all_banner,
		'locations': locations
	}

	return render(request, template, context)

def ham_honge_kamiyab(request):
	if request.is_ajax():
		

		b = Banner.objects.get(pk=int(request.POST['id_point']))
		data = {"id" : str(b.id), "cost" : str(b.banner_cost), "lat" : str(b.banner_lattitude), "long" : str(b.banner_longitude), "dim" : str(b.banner_dimensions)}
		json_data = json.dumps(data)

		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404

def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'	
	return render(request, template, context)


def single(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		#images = product.productimage_set.all()
		images = ProductImage.objects.filter(product=product)
		context = {'product': product, "images": images}
		template = 'products/single.html'	
		return render(request, template, context)
	except:
		raise Http404
