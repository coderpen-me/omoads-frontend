from django.shortcuts import render, Http404, HttpResponseRedirect

from django.views import generic

from django.shortcuts import render, HttpResponse, Http404
from django.http import HttpResponseBadRequest

from django.db.models import Q
import json, time
# Create your views here.

from marketing.forms import EmailForm
from marketing.models import MarketingMessage, Slider

from .forms import *
from .models import Product, ProductImage, Banner, Agency, DIMENSION_CHOICES,BookingDetails,PricePeriod
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime

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

class Home(generic.TemplateView):
	login_form_class = LoginForm
	signup_form_class = UserForm
	def get(self, request, *args, **kwargs):
		sliders = Slider.objects.all_featured()
		products = Product.objects.all()
		template = 'products/home.html'	
		login_form = self.login_form_class
		signup_form = self.signup_form_class
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




		username = ""
		userType = ""
		if request.user.is_authenticated():
			username = request.user.username
			try:
				Agency.objects.get(user = request.user)
				userType = "Agency"
			except Agency.DoesNotExist:
				userType = "Buyer"
		context = {
			"products": products,
			"sliders": sliders,
			'form': form,
			'result': results,
			'all': all_banner,
			'locations': locations,
			'login_form':login_form,
			'signup_form':signup_form,
			'loginStatus':request.user.is_authenticated(),
			'username':username,
			'userType':userType
		}

		return render(request, template, context)

	def post(self, request, *args, **kwargs):
		try:
			username = request.POST['username']
			password = request.POST['password']
			print(username + " " + password)
			user = authenticate(username = username, password = password)
			if user is not None:
				try:
					a = Agency.objects.get(user = user)
					login(request, user)
					request.session['isAgency'] = True
					request.session['AgencyId'] = a.id
					print("logged in as an agency")
					return HttpResponseRedirect(reverse('owner_interface'))

				except Agency.DoesNotExist:
					login(request, user)
					request.session['isAgency'] = False
					print("logged in as a user")
					return HttpResponseRedirect("/")
			else:
				print("galat daala")
				return HttpResponseRedirect(reverse('auth_login'))
		except Exception as e:
			print(e)
			return HttpResponseRedirect(reverse('auth_login'))


def onclickMapPoints(request):
	if request.is_ajax():
		

		b = Banner.objects.get(pk=int(request.POST['id_point']))

		data = {"id" : str(b.id), "landmark": str(b.banner_landmark), "cost" : str(b.banner_cost), "lat" : str(b.banner_lattitude), "long" : str(b.banner_longitude), "dim" : str(DIMENSION_CHOICES[int(b.banner_dimensions)][1])}
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

class Signup(generic.edit.FormView):
	form_class  = UserForm
	template_name = 'signup.html'
	def get(self, request, *args, **kwargs):
		try:
			form = self.form_class
			if not request.user.is_authenticated():
				return render(request, self.template_name, {'form':form})
			#elif((request.session['adminSession'] is True)):
			#	return HttpResponseRedirect(reverse('portal:adminPage'))
			#else:
			#	return HttpResponseRedirect(reverse('portal:index'))
			else:
				return HttpResponseRedirect("/")
		except KeyError:
			return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			pass
		else:
			#messages.error(request,"Enter Correct Values In All The Fields")
			print("invalid")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		new_user = form.save(commit=False)
		password = request.POST['password1']
		new_user.set_password(password)
		try:
			quer = User.objects.get(email=new_user.email)
		except User.DoesNotExist:
			try:
				quer=User.objects.get(username=new_user.username)
			except User.DoesNotExist:
				new_user.save()
				return HttpResponseRedirect("/")
			else:
				#messages.error(request, "The username or email already exists.")
				print("invalid username already")
				return HttpResponseRedirect(reverse('auth_register'))
		else:
			#messages.error(request, "The username or email already exists.")
			print("invalid email already")
			return HttpResponseRedirect(reverse('auth_register'))



def signup(request):
	form = UserForm.form_class(request.POST)
	if form.is_valid():
		pass
	else:
		#messages.error(request,"Enter Correct Values In All The Fields")
		print("invalid pagalpanti")
		return HttpResponseRedirect("/")
	new_user = form.save(commit=False)
	password = request.POST['password1']
	new_user.set_password(password)
	try:
		quer = User.objects.get(email=new_user.email)
	except User.DoesNotExist:
		try:
			quer=User.objects.get(username=new_user.username)
		except User.DoesNotExist:
			new_user.save()
			return HttpResponseRedirect("/")
		else:
			#messages.error(request, "The username or email already exists.")
			print("invalid username already")
			return HttpResponseRedirect(reverse('auth_register'))
	else:
		#messages.error(request, "The username or email already exists.")
		print("invalid email already")
		return HttpResponseRedirect(reverse('auth_register'))


class SignupOwner(generic.edit.FormView):
	form_user  = UserForm
	form_agency = AgencyForm
	template_name = 'signupAgency.html'
	def get(self, request, *args, **kwargs):
		try:
			formUser = self.form_user
			formAgency = self.form_agency
			if not request.user.is_authenticated():
				return render(request, self.template_name, {'form':formUser, 'agency':formAgency})
			else:
				return HttpResponseRedirect("/")

		except KeyError:
			return render(request, self.template_name, {'form':formUser, 'agency':formAgency})

	def post(self, request, *args, **kwargs):
		form = self.form_user(request.POST)
		agency = self.form_agency(request.POST)
		if form.is_valid():
			pass
		else:
			#messages.error(request,"Enter Correct Values In All The Fields")
			print("invalid")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		new_user = form.save(commit=False)
		password = request.POST['password1']
		new_user.set_password(password)
		new_agency = agency.save(commit = False)
		try:
			quer = User.objects.get(email=new_user.email)
		except User.DoesNotExist:
			try:
				quer=User.objects.get(username=new_user.username)
			except User.DoesNotExist:
				new_user.save()
				print("bawal")
				new_agency.user = new_user
				new_agency.save()
				return HttpResponseRedirect("/")
			else:
				#messages.error(request, "The username or email already exists.")
				print("invalid username already")
				return HttpResponseRedirect(reverse('auth_register_owner'))
		else:
			#messages.error(request, "The username or email already exists.")
			print("invalid email already")
			return HttpResponseRedirect(reverse('auth_register_owner'))


class LoginUsers(generic.edit.FormView):
	form_class = LoginForm
	template_name = 'userlogin.html'
	def get(self, request, *args, **kwargs):
		try:
			form = self.form_class
			if not request.user.is_authenticated():
				print("chalega")
				return render(request, self.template_name, {'form':form})
			else:
				return HttpResponseRedirect("/")
			
		except KeyError:
			return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		try:
			username = request.POST['username']
			password = request.POST['password']
			print(username + " " + password)
			user = authenticate(username = username, password = password)
			if user is not None:
				try:
					a = Agency.objects.get(user = user)
					login(request, user)
					request.session['isAgency'] = True
					request.session['AgencyId'] = a.id
					print("logged in as an agency")
					return HttpResponseRedirect(reverse('owner_interface'))

				except Agency.DoesNotExist:
					login(request, user)
					request.session['isAgency'] = False
					print("logged in as a user")
					return HttpResponseRedirect("/")
				
			else:
				print("galat daala")
				return HttpResponseRedirect(reverse('auth_login'))
		except Exception as e:
			print(e)
			return HttpResponseRedirect(reverse('auth_login'))

def	adminInterface1(request):
	return render(request, 'adminIndex.html', {})

def	adminInterface2(request):
	return render(request, 'book-hoarding.html', {})

def	adminInterface3(request):
	return render(request, 'cancel-booking.html', {})

def	adminInterface4(request):
	return render(request, 'change-price.html', {})

def	adminInterface5(request):
	return render(request, 'status.html', {})


def logoutUser(request):
	request.session['isAgency'] = None
	request.session['AgencyId'] = None
	logout(request)
	print("successfully logged out")
	return HttpResponseRedirect("/")


class OwnerInterfaceHome(generic.TemplateView):
	template_name = "adminIndex.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			if request.session['isAgency'] is not None and request.session['isAgency'] is True:

				username = request.user.username
				a = Agency.objects.get(user = request.user)
				userType = "Agency"
				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType,
					'details': Banner.objects.filter(agency=a)
				}

				return render(request, self.template_name, context)
			else:
				context = {}
				print("u r not an agency")
				#To-Do: Generate a msg
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			#To-Do: Generate a msg
			return HttpResponseRedirect(reverse('auth_login'))

class CancelBooking(generic.TemplateView):
	template_name = "cancel-booking.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			if request.session['isAgency'] is not None and request.session['isAgency'] is True:

				username = request.user.username
				a = Agency.objects.get(user = request.user)
				userType = "Agency"
				details = []
				for banner in Banner.objects.filter(agency=a, banner_bookingStatus = True):
					bd = banner.bookingdetails_set.get(active = True)
					details.append({'banner':banner, 'bookingDate':bd.bookingDate, 'startDate':bd.startDate,
								 'endDate':bd.endDate, 'bdID':bd.id})

				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType,
					'details':details	
				}

				return render(request, self.template_name, context)
			else:
				context = {}
				print("u r not an agency")
				return HttpResponseRedirect("/")
				#To-Do: Generate a msg
		else:
			print("u need to login")
			#To-Do: Generate a msg
			return HttpResponseRedirect(reverse('auth_login'))



class StatusBoards(generic.TemplateView):
	template_name = "owner-interface/status.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			if request.session['isAgency'] is not None and request.session['isAgency'] is True:

				username = request.user.username
				userType = "Agency"
				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType
				}

				return render(request, self.template_name, context)
			else:
				context = {}
				print("u r not an agency")
				return HttpResponseRedirect("/")
				#To-Do: Generate a msg
		else:
			print("u need to login")
			#To-Do: Generate a msg
			return HttpResponseRedirect(reverse('auth_login'))

class PriceBoards(generic.TemplateView):
	template_name = "change-price.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			if request.session['isAgency'] is not None and request.session['isAgency'] is True:

				username = request.user.username
				a = Agency.objects.get(user = request.user)

				details = []
				for banner in Banner.objects.filter(agency=a):

					details.append({'banner':banner, 'price_set':banner.priceperiod_set.all().order_by('-id')[:8][::-1]})


				userType = "Agency"
				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType,
					'details':details
				}

				return render(request, self.template_name, context)
			else:
				context = {}
				print("u r not an agency")
				return HttpResponseRedirect("/")
				#To-Do: Generate a msg
		else:
			print("u need to login")
			#To-Do: Generate a msg
			return HttpResponseRedirect(reverse('auth_login'))




class BookHoardings(generic.TemplateView):
	template_name = "book-hoarding.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			if request.session['isAgency'] is not None and request.session['isAgency'] is True:

				username = request.user.username
				a = Agency.objects.get(user = request.user)
				userType = "Agency"
				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType,
					'details': Banner.objects.filter(agency=a, banner_bookingStatus = False)
				}

				return render(request, self.template_name, context)
			else:
				context = {}
				print("u r not an agency")
				#To-Do: Generate a msg
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			#To-Do: Generate a msg
			return HttpResponseRedirect(reverse('auth_login'))


def bookBoards(request):
	for boardID in request.POST.getlist('boards'):
		print(boardID)
		banner = Banner.objects.get(pk = boardID)
		bd = banner.bookingdetails_set.create(bookingDate = time.strftime("%Y-%m-%d"),
									startDate = request.POST['dateStart'], endDate = request.POST['dateEnd'],
									numberDays = request.POST['days'], active = True)
		bd.save()
		banner.banner_bookingStatus = True
		banner.save()

	return HttpResponseRedirect(reverse('owner_interface'))


def cancelBoard(request):
	if request.is_ajax():
		banner = Banner.objects.get(pk = request.POST['boardID'])
		banner.banner_bookingStatus = False
		banner.save()
		bd = BookingDetails.objects.get(pk = request.POST['bdID'])
		bd.active = False
		bd.save()
		data = {"success":True}
		json_data = json.dumps(data)

		return HttpResponse(json_data, content_type='application/json')
	else:
		Http404




def addIndiPrice(request):
	banner = Banner.objects.get(pk = request.POST['boardID'])
	startDateParsed = datetime.datetime.strptime(request.POST['dateStart'], "%Y-%m-%d").date()
	endDateParsed = datetime.datetime.strptime(request.POST['dateEnd'], "%Y-%m-%d").date()

	price_set = banner.priceperiod_set.filter(endDate__gte = startDateParsed, startDate__lte = endDateParsed)
	book_set = banner.bookingdetails_set.filter(startDate__gte = startDateParsed, endDate__lte = endDateParsed)
	if len(book_set) == 0:
		for price in price_set:
			if (price.endDate >= startDateParsed) and (price.startDate < startDateParsed):
				price.endDate = (startDateParsed - datetime.timedelta(days=1))
				print(startDateParsed)
				price.save()
			if (price.startDate <= endDateParsed) and (price.endDate >endDateParsed):
				price.startDate = (endDateParsed + datetime.timedelta(days=1))
				price.save()
			if (price.startDate >= startDateParsed and price.endDate <= endDateParsed):
				price.delete()

		newPrice = banner.priceperiod_set.create(startDate = startDateParsed, endDate = endDateParsed, numberDays = request.POST['days'], price = request.POST['price'])
		newPrice.save()
		banner.save()
		return HttpResponseRedirect(reverse('owner_interface_price'))
	else:
		Http404
	
