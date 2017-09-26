from django.shortcuts import render, Http404, HttpResponseRedirect, redirect
from django.contrib import messages
from django.views import generic

from django.shortcuts import render, HttpResponse, Http404
from django.http import HttpResponseBadRequest

from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json, time
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers

from .forms import *
from .models import *


from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
import datetime
from instamojo_wrapper import Instamojo

API_KEY='41ac278373a4e455997329fc318344d2'
AUTH_TOKEN='502835a970d07f3f739ef94e9fe1d5d0'


ADVANCE_PRICE = 0.02
GST = 0.18
PAYMENT_1 = 0.48
PAYMENT_2 = 0.5

######
#LANDING PAGE
######

def aboutus(request):
	template = "aboutus.html"
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
				'loginStatus':request.user.is_authenticated(),
				'username':username,
				'userType':userType
				}
	return render(request, template, context)

def directions(request):
	template = "directions.html"
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
				'loginStatus':request.user.is_authenticated(),
				'username':username,
				'userType':userType
				}
	return render(request, template, context)

def faq(request):
	template = "faqs.html"
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
				'loginStatus':request.user.is_authenticated(),
				'username':username,
				'userType':userType
				}
	return render(request, template, context)


@login_required(login_url = "/")
def booking_status(request):
	template = 'products/booking-status.html'	
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
			'loginStatus':request.user.is_authenticated(),
			'username':username,
			'userType':userType,
			'orders':Order.objects.filter(user = request.user),
		}
		return render(request, template, context)
	else:
		return HttpResponseRedirect("/")
@login_required(login_url = "/")
def buyer_cart(request):
	template = 'products/buyer_cart.html'	
	username = ""
	userType = ""

	if request.user.is_authenticated():
		username = request.user.username
		try:
			Agency.objects.get(user = request.user)
			userType = "Agency"
			messages.error(request, "you can't access this page")
			return HttpResponseRedirect(reverse('owner_interface'))
		except Agency.DoesNotExist:
			userType = "Buyer"

		for item in request.user.cart.cartitem_set.all():
			if not checkDateRange(item.startDate, item.endDate, item.banner):
				item.dateAccept = False
			

		context = {
			'loginStatus':request.user.is_authenticated(),
			'username':username,
			'userType':userType,
			'cart':request.user.cart,
		}
		request.currentPayementRequest = None
		return render(request, template, context)
	else:
		return HttpResponseRedirect("/")

def processCart(cart):
	cart.totalPrice = 0.00
	for cartItem in cart.cartitem_set.all():
		cart.totalPrice = cart.totalPrice + cartItem.price

	cart.totalSumPrice = round(cart.totalPrice + cart.installationPrice, 2)
	cart.tax = round(cart.totalSumPrice * GST, 2)
	cart.totalSumPrice = round(cart.totalSumPrice + cart.tax, 2)

	cart.paymentAdvance = round(cart.totalPrice * ADVANCE_PRICE, 2)
	cart.payment1 = round(cart.totalPrice * PAYMENT_1, 2)
	cart.payment2 = round(cart.totalPrice * PAYMENT_2, 2)
	cart.save()
	

def addToCart(request):
	b = Banner.objects.get(pk=int(request.POST['bannerIDAddCart']))
	print(b)
	startDateParsed = datetime.datetime.strptime(request.POST['startDateAddCart'], "%Y-%m-%d").date()
	endDateParsed = datetime.datetime.strptime(request.POST['endDateAddCart'], "%Y-%m-%d").date()


	total = calculatePrice(b,startDateParsed,endDateParsed)
	try:
		cart = request.user.cart
	except AttributeError:
		if request.user.is_authenticated():
			cart = Cart(user = request.user)
			cart.save()
		else:
			messages.error(request, "login first")
			return HttpResponseRedirect('/')
	cartItem = cart.cartitem_set.create(banner = b, startDate = startDateParsed, endDate = endDateParsed, price = total)
	cartItem.save()
	cart.save()
	processCart(cart)
	print(cart)
	print(cart.cartitem_set.all())
	return HttpResponseRedirect(reverse('buyer_cart'))
	

def check_out(request):
	request.currentPayementRequest = None
	for item in request.user.cart.cartitem_set.all():
		if not checkDateRange(item.startDate, item.endDate, item.banner):
			print("fault in date")
			return HttpResponseRedirect(reverse("buyer_cart"))
	if request.user.cart.cartitem_set.all().count()==0:
		print("no item in cart")
		return HttpResponseRedirect(reverse("buyer_cart"))
	print("checkOut")
	print('create request url')

	api = Instamojo(api_key=API_KEY,
				auth_token=AUTH_TOKEN)

	# Create a new Payment Request
	response = api.payment_request_create(
		amount=str(request.user.cart.paymentAdvance),
		email = request.user.email,
		purpose=str(request.user.get_username()),
		redirect_url="http://www.omoads.com/process_payment",
	 	send_email = False,
		send_sms = False,
		allow_repeated_payments = False
		)

	# print response
	print (response)

	if(response['success'] is True):
		request.currentPayementRequest = response['payment_request']['id']
		return redirect(response['payment_request']['longurl'])
	else:
		print("no api working")


	

def processPayment(request):
	paymentID = request.GET['payment_id']
	paymentRequestID = request.GET['payment_request_id']

	if request.currentPayementRequest == paymentRequestID and request.currentPayementRequest is not None:
		request.currentPayementRequest = None
		api = Instamojo(api_key=API_KEY,
					auth_token=AUTH_TOKEN)

		# Create a new Payment Request
		try:
			response = api.payment_request_payment_status(paymentRequestID, paymentID)
			print(response)
			print ("test")             # Purpose of Payment Request
		   # Payment status
			success = response['success']
			if success is True:
				status = response['payment_request']['payment']['status']
				payment = Payments(user = request.user, paymentId = paymentID, paymentRequestId = paymentRequestID, paymentStatus = status)
				payment.save()
				print (status)
				if (status == "Credit"):
					order = Order(user = request.user,totalPrice = request.user.cart.totalPrice,
								paymentAdvance =  request.user.cart.paymentAdvance,
						 		payment1 =  request.user.cart.payment1, payment2 =  request.user.cart.payment2,
						 		installationPrice =  request.user.cart.installationPrice, tax =  request.user.cart.tax,
						 		totalSumPrice =  request.user.cart.totalSumPrice, status = 1)
					order.save()
					payment.order = order
					
					
					for item in request.user.cart.cartitem_set.all():
						bd = BookingDetails(banner = item.banner, bookingDate = time.strftime("%Y-%m-%d"),
													startDate = item.startDate, endDate = item.endDate,
													numberDays = (item.endDate - item.startDate).days, active = True)
						bd.save()
						order.orderitem_set.create(bookingDetails = bd, price = item.price).save()
						
					clear_cart(request.user.cart)
					messages.success(request, "payment successful")
					payment.save()
					return HttpResponseRedirect(reverse('booking_status'))
				elif (status == "Failed"):
					messages.error(request, "payment failed")
					return HttpResponseRedirect(reverse('buyer_cart'))
				
			else:
				print("something went wrong.payment details couldnt be fetched")
		except Exception as e:
			print("something went wrong :" + str(e))
	else:
		messages.error(request, "unauthorised access")
		return HttpResponseRedirect(reverse('buyer_cart'))

	

def clear_cart(cart):
	cart.cartitem_set.all().delete()
	cart.totalPrice = 0.00
	cart.paymentAdvance = 0.00
	cart.payment1 = 0.00
	cart.payment2 = 0.00
	cart.installationPrice = 0.00
	cart.tax = 0.00
	cart.totalSumPrice = 0.00
	cart.save()

def deleteCartItem(request, itemId):
	ci = request.user.cart.cartitem_set.get(pk=int(itemId))
	print(ci)
	ci.delete()
	processCart(request.user.cart)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



class Home(generic.TemplateView):
	login_form_class = LoginForm
	signup_form_class = UserForm
	def get(self, request, *args, **kwargs):
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
		request.currentPayementRequest = None
		return render(request, template, context)

	def post(self, request, *args, **kwargs):
		try:
			username = request.POST['username']
			password = request.POST['password']
			print(username + " " + password)
			user = authenticate(username = username, password = password)
			print(user)
			if user is None:
				try:
					u = User.objects.get(email = username)
					username = u.get_username()
					user = authenticate(username = username, password = password)
				except User.DoesNotExist:
					user = None
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
				messages.error(request, "wrong username passowrd", extra_tags = 'wrong_credentials')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		except Exception as e:
			print(e)
			messages.error(request, e)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def onclickMapPoints(request):
	if request.is_ajax():
		b = Banner.objects.get(pk=int(request.POST['id_point']))
		bookDates = []
		for detailset in b.bookingdetails_set.filter(active = True):
			bookDates.append({'startDate':str(detailset.startDate), 'endDate': str(detailset.endDate)})
		try:
			for item in request.user.cart.cartitem_set.filter(banner = b):
				bookDates.append({'startDate':str(item.startDate), 'endDate': str(item.endDate)})
		except:
			print("no user")

		
		context = {"bookdates":bookDates}
		data = {
		"id" : str(b.id),
		# "landmark": str(b.banner_landmark),
		"url": str(b.bannerimage),
		"type": str(type_choices[str(b.banner_type)]),
		"lighted": str(light_choices[str(b.banner_lighted)]),
		# "cost" : str(b.banner_cost),
		"lat" : str(b.banner_lattitude),
		"long" : str(b.banner_longitude),
		"dim" : str(dimension_choices[str(b.banner_dimensions)]),
		"bookDates":bookDates
		}
		# print(data)
		json_data = json.dumps(data)

		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404

def AjaxBannerPrice(request):
	if request.is_ajax():
		b = Banner.objects.get(pk=int(request.POST['id_point']))
		print(b)
		startDateParsed = datetime.datetime.strptime(request.POST['startDate'], "%Y-%m-%d").date()
		endDateParsed = datetime.datetime.strptime(request.POST['endDate'], "%Y-%m-%d").date()

		if not checkDateRange(startDateParsed, endDateParsed, b):
			print("fault in date")
			messages.error(request, "fault in date")
			return

		total = calculatePrice(b,startDateParsed,endDateParsed)

			
			
		print(total)


		data = {
		'total':total
		}
		# print(data)
		json_data = json.dumps(data)

		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404


######
#SIGUNUP PAGE AND SIGNUP FUNCTION FOR HOME PAGE
######

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
				c = Cart(user = new_user)
				c.save()
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
		messages.error(request,"Enter Correct Values In All The Fields")
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
			c = Cart(user = new_user)
			c.save()
			return HttpResponseRedirect("/")
		else:
			#messages.error(request, "The username or email already exists.")
			print("invalid username already")
			return HttpResponseRedirect(reverse('auth_register'))
	else:
		#messages.error(request, "The username or email already exists.")
		print("invalid email already")
		return HttpResponseRedirect(reverse('auth_register'))



######
#SIGNUP OWNER
######

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
		new_agency = Agency(agency_name = request.POST['agency_name'],agency_state = request.POST['agency_state'],agency_city = request.POST['agency_city'])
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


######
#SESSION AND LOGIN LOGOUT
######

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




def logoutUser(request):
	request.session['isAgency'] = None
	request.session['AgencyId'] = None
	logout(request)
	print("successfully logged out")
	return HttpResponseRedirect("/")



######
#OWNER START
######

######
#OWNER LANDING PAGE
######

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
					'details': Banner.objects.filter(agency=a),
					'zones':Zone.objects.filter(banner__agency=a).distinct()
				}

				return render(request, self.template_name, context)
			else:
				
				print("u r not an agency")
				#To-Do: Generate a msg
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			#To-Do: Generate a msg
			messages.error(request, "Login required")
			return HttpResponseRedirect('/?next=%s' % (request.path))


######
#CANCEL PAGE
######

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
					bannerDetails = banner.bookingdetails_set.filter(active = True)
					for detail in bannerDetails:
						details.append({'banner':banner, 'bookingDate':detail.bookingDate, 'startDate':detail.startDate,
								 	'endDate':detail.endDate, 'bdID':detail.id})

				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType,
					'details':details,
					'zones':Zone.objects.filter(banner__agency=a).distinct()
				}

				return render(request, self.template_name, context)
			else:
				context = {}
				print("u r not an agency")
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
				#To-Do: Generate a msg
		else:
			print("u need to login")
			#To-Do: Generate a msg
			messages.error(request, "Login required")
			return HttpResponseRedirect('/?next=%s' % (request.path))

@login_required(login_url = "/", redirect_field_name = reverse_lazy('owner_interface_cancel'))
def cancelBoard(request):
	if request.is_ajax():
		banner = Banner.objects.get(pk = request.POST['boardID'])
		if banner.bookingdetails_set.filter(active = True).count() is 0:
			banner.banner_bookingStatus = False
			banner.save()
		bd = BookingDetails.objects.get(pk = request.POST['bdID'])
		bd.active = False
		bd.save()
		data = {"success":True}
		json_data = json.dumps(data)
		messages.success(request, "board cancelled", extra_tags = 'cancel_successful')
		return HttpResponse(json_data, content_type='application/json')
	else:
		Http404


######
#STATUS PAGE
######

class StatusBoards(generic.TemplateView):
	template_name = "status.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			if request.session['isAgency'] is not None and request.session['isAgency'] is True:
				username = request.user.username
				userType = "Agency"
				a = Agency.objects.get(user = request.user)
				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType,
					'zones':Zone.objects.filter(banner__agency=a).distinct()
				}

				return render(request, self.template_name, context)
			else:
				context = {}
				print("u r not an agency")
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			messages.error(request, "Login required")
			return HttpResponseRedirect('/?next=%s' % (request.path))


######
#PRICE CHANGE PAGE
######

class PriceBoards(generic.TemplateView):
	template_name = "change-price.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			if request.session['isAgency'] is not None and request.session['isAgency'] is True:

				username = request.user.username
				a = Agency.objects.get(user = request.user)

				details = []
				for banner in Banner.objects.filter(agency=a):

					details.append({'banner':banner, 'price_set':banner.priceperiod_set.all().order_by('-startDate')[:4][::-1]})


				userType = "Agency"
				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType,
					'details':details,
					'zones':Zone.objects.filter(banner__agency=a).distinct()
				}

				return render(request, self.template_name, context)
			else:
				messages.error(request, "you are not authorised to access this page")
				print("u r not an agency")
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			messages.error(request, "Login required")
			return HttpResponseRedirect('/?next=%s' % (request.path))
			
@login_required(login_url = "/", redirect_field_name = reverse_lazy('owner_interface_price'))
def addIndiPrice(request):
	banner = Banner.objects.get(pk = request.POST['boardID'])
	startDateParsed = datetime.datetime.strptime(request.POST['dateStart'], "%Y-%m-%d").date()
	endDateParsed = datetime.datetime.strptime(request.POST['dateEnd'], "%Y-%m-%d").date()

	price_set = banner.priceperiod_set.filter(endDate__gte = startDateParsed, startDate__lte = endDateParsed)

	book_set = banner.bookingdetails_set.filter(startDate__gte = startDateParsed, startDate__lte = endDateParsed, active = True)
	book_set_2 = banner.bookingdetails_set.filter(endDate__gte = startDateParsed, endDate__lte = endDateParsed, active = True)
	book_set_3 = banner.bookingdetails_set.filter(startDate__lte = startDateParsed, endDate__gte = endDateParsed, active = True)
	if (len(book_set) == 0) and (len(book_set_2) == 0) and (len(book_set_3) == 0):
		for price in price_set:
			if (price.startDate < startDateParsed) and (price.endDate > endDateParsed):
				delta = price.endDate-endDateParsed
				newPrice1 = banner.priceperiod_set.create(startDate = endDateParsed + datetime.timedelta(days=1), endDate = price.endDate, numberDays = delta.days + 1, price = price.price)
				newPrice1.save()
				price.endDate = (startDateParsed - datetime.timedelta(days=1))
				price.save()
			elif (price.endDate >= startDateParsed) and (price.startDate < startDateParsed):
				price.endDate = (startDateParsed - datetime.timedelta(days=1))
				print(startDateParsed)
				price.save()
			elif (price.startDate <= endDateParsed) and (price.endDate >endDateParsed):
				price.startDate = (endDateParsed + datetime.timedelta(days=1))
				price.save()
			elif (price.startDate >= startDateParsed and price.endDate <= endDateParsed):
				price.delete()

		newPrice = banner.priceperiod_set.create(startDate = startDateParsed, endDate = endDateParsed, numberDays = request.POST['days'], price = request.POST['price'])
		newPrice.save()
		banner.save()
		messages.success(request,"price changed", extra_tags = "price_change_success")
		return HttpResponseRedirect(reverse('owner_interface_price'))
	else:
		messages.success(request,"the selected dates have board bookings", extra_tags = "price_change_success")
		return HttpResponseRedirect(reverse('owner_interface_price'))
	

######
#booking PAGE
######

class BookHoardings(generic.TemplateView):
	template_name = "book-hoarding.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			if request.session['isAgency'] is not None and request.session['isAgency'] is True:

				username = request.user.username
				a = Agency.objects.get(user = request.user)
				details = []
				for banner in Banner.objects.filter(agency=a):
					bookDates = []
					for detailset in banner.bookingdetails_set.filter(active = True):
						bookDates.append({'startDate':detailset.startDate, 'endDate': detailset.endDate})
					details.append({'banner':banner, 'dates':bookDates})
					
				userType = "Agency"
				context = {
					'loginStatus':True,
					'username':username,
					'userType':userType,
					'details': details,
					'zones':Zone.objects.filter(banner__agency=a).distinct()
				}

				return render(request, self.template_name, context)
			else:
				context = {}
				print("u r not an agency")
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			messages.error(request, "Login required")
			return HttpResponseRedirect('/?next=%s' % (request.path))

@login_required(login_url = "/", redirect_field_name = reverse_lazy('owner_interface_book'))
def bookBoards(request):
	for boardID in request.POST.getlist('boards'):
		print(boardID)
		banner = Banner.objects.get(pk = boardID)
		bd = banner.bookingdetails_set.create(bookingDate = time.strftime("%Y-%m-%d"),
									startDate = request.POST['dateStart'+ str(boardID)], endDate = request.POST['dateEnd'+ str(boardID)],
									numberDays = request.POST['days'+ str(boardID)], active = True)
		bd.save()
		banner.banner_bookingStatus = True
		banner.save()
	messages.success(request, "board(s) booked", extra_tags = 'book_successful')
	return HttpResponseRedirect(reverse('owner_interface'))










######
#HELPERS
######

def calculatePrice(banner,startDate,endDate):
	price_set = banner.priceperiod_set.filter(endDate__gte = startDate, startDate__lte = endDate).order_by('startDate')
	print(Area[str(banner.banner_dimensions)])
	print(price_set)
	total = 0
	for price in price_set:
		print(price)

		if(startDate >= price.startDate and endDate <= price.endDate):
			delta = endDate - startDate
			total = total + ((Area[str(banner.banner_dimensions)])*price.price*(delta.days+1)/30.4)
			print(total)
		elif(startDate <= price.endDate and startDate >= price.startDate and endDate > price.endDate):
			delta = price.endDate - startDate + datetime.timedelta(days=1)
			total = total + ((Area[str(banner.banner_dimensions)])*price.price*delta.days/30.4)
			print(total)
		elif(startDate <= price.startDate and endDate >= price.endDate):
			total = total + ((Area[str(banner.banner_dimensions)])*price.price*(price.numberDays+1)/30.4)
			print(total)
		elif(startDate < price.startDate and endDate >= price.startDate and endDate <= price.endDate):
			delta = endDate - price.startDate
			total = total + ((Area[str(banner.banner_dimensions)])*price.price*(delta.days+1)/30.4)
			print(total)
	return round(total,2)


def checkDateRange(startDate, endDate, banner):
	for detailset in banner.bookingdetails_set.filter(active = True):
		if ((detailset.startDate <= startDate and startDate <= detailset.endDate) or 
			(detailset.startDate <= endDate and endDate <= detailset.endDate)):
			return False
	#TO-DO
	#for cartitem in banner.cartitem_set.filter(cart.user = request.user):
	#	if ((cartitem.startDate <= startDate and startDate <= cartitem.endDate) or 
	#		(cartitem.startDate <= endDate and endDate <= cartitem.endDate)):
	#		messages
	#		return False
	return True