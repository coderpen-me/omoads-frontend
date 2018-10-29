from django.shortcuts import render, Http404, HttpResponseRedirect, redirect
from django.contrib import messages
from django.views import generic
import six
from django.shortcuts import render, HttpResponse, Http404
from django.http import HttpResponseBadRequest
#for python 3 use line 8 instead of 9 
#from urllib.parse import parse_qs
if six.PY3:
    from urllib.parse import parse_qs
else:	
    from urlparse import parse_qs

from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json, time
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers

from .forms import *
from .models import *

from dateutil.relativedelta import relativedelta


from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
import datetime
from instamojo_wrapper import Instamojo

# API_KEY='41ac278373a4e455997329fc318344d2'
# AUTH_TOKEN='502835a970d07f3f739ef94e9fe1d5d0'

API_KEY='ea974cdf32f78ca6b3cb05c627d222c0'
AUTH_TOKEN='711bc96a14396d341627dc761db53d2c'


ADVANCE_PRICE = 0.35
GST = 0.18
PAYMENT_1 = 0.35
PAYMENT_2 = 0.30

######
#LANDING PAGE
######

def printing_material(request):
	template = "printingMaterial.html"
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


def blog_page(request):
	template = "blog.html"
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



@login_required(login_url = "/login/")
def dashboard(request):
	template = "dashboard.html"
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


@login_required(login_url = "/login/")
def favourites(request):
	template = "fav.html"
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

def index_new_home(request):
	template = "index.html"
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

def landing(request):
	template = "landing.html"
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


def landing_1(request):
	template = "landing1.html"
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



def aboutus(request):
	template = "about-us.html"
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

def faq(request, f_id):
	template = "single-faq.html"
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
				'f_id':f_id,
				}
	return render(request, template, context)

def uploadImage(request):
	template = "upload-image.html"
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

def adminPriceChanger(request):
	template = "products/adminPriceChanger.html"
	username = ""
	userType = ""
	if request.user.is_authenticated() and request.user.is_superuser:
		details = []
		for banner in Banner.objects.all():
			bookDates = []

			for booked_date in banner.bookingdetails_set.filter(endDate__gte = datetime.datetime.now().strftime("%Y-%m-%d")):
				bookDates.append({'startDate':str(booked_date.startDate), 'endDate': str(booked_date.endDate)})

			details.append({'banner':banner, 
				'active_booking_details': bookDates,})




		context = {
				'loginStatus':request.user.is_authenticated(),
				'username':username,
				'userType':userType,
				'details':details,
				}
		return render(request, template, context)
	else:
		raise Http404("not admin")


@login_required(login_url = "/login/")
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
		messages.error(request, "login first")
		return HttpResponseRedirect("/")
@login_required(login_url = "/login/")
def buyer_cart(request):
	template = 'products/buyer_cart.html'	
	username = ""
	userType = ""

	if request.user.is_authenticated():
		username = request.user.username
		try:
			Agency.objects.get(user = request.user)
			userType = "Agency"
			messages.error(request, "You can not buy banners because you are Agency owner")
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

	cart.paymentAdvance = round(cart.totalSumPrice * ADVANCE_PRICE, 2)
	cart.payment1 = round(cart.totalSumPrice * PAYMENT_1, 2)
	cart.payment2 = round(cart.totalSumPrice * PAYMENT_2, 2)
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
			return HttpResponseRedirect('/login/')
	cartItem = cart.cartitem_set.create(banner = b, startDate = startDateParsed, endDate = endDateParsed, price = total)
	cartItem.save()
	cart.save()
	processCart(cart)
	print(cart)
	print(cart.cartitem_set.all())
	return HttpResponseRedirect(reverse('buyer_cart'))


def editCartItemAjax(request):
	if request.is_ajax():
		print("222")
		cartItem = CartItem.objects.get(pk=int(request.POST['idCartItem']))
		b = cartItem.banner
		print("444")
		bookDates = []
		for detailset in b.bookingdetails_set.filter(active = True):
			bookDates.append({'startDate':str(detailset.startDate), 'endDate': str(detailset.endDate)})
		try:
			for item in request.user.cart.cartitem_set.filter(banner = b):
				if item.id == cartItem.id:
					continue
				bookDates.append({'startDate':str(item.startDate), 'endDate': str(item.endDate)})
		except:
			print("no user")

		print("here1")
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
		"bookDates":bookDates,
		"oldStart": str(cartItem.startDate),
		"oldEnd":str(cartItem.endDate),
		}
		# print(data)
		
		json_data = json.dumps(data)

		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404

def editCartItem(request):
	ci = request.user.cart.cartitem_set.get(pk=int(request.POST['cartItemId']))
	ci.delete()
	return addToCart(request)
	
@login_required(login_url = "/login/")
def check_out(request):
	request.currentPayementRequest = None
	for item in request.user.cart.cartitem_set.all():
		if not checkDateRange(item.startDate, item.endDate, item.banner):
			print("fault in date")
			messages.error(request, "check date again for item ID" + item.banner.id + "start date:" + item.startDate + " end date:" + item.endDate)
			return HttpResponseRedirect(reverse("buyer_cart"))
	if request.user.cart.cartitem_set.all().count()==0:
		print("no item in cart")
		messages.error(request, "empty cart")
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
		redirect_url="https://omoads.com/process_payment",
	 	send_email = False,
		send_sms = False,
		allow_repeated_payments = False
		)

	# print response
	print (response)

	if(response['success'] is True):
		request.session['currentPayementRequest'] = response['payment_request']['id']
		return redirect(response['payment_request']['longurl'])
	else:
		print("no api working")
		messages.error(request, "amount too low")
		return HttpResponseRedirect(reverse('buyer_cart'))


	

def processPayment(request):
	paymentID = request.GET['payment_id']
	paymentRequestID = request.GET['payment_request_id']
	if request.session['currentPayementRequest'] is not None:
		if request.session['currentPayementRequest'] == paymentRequestID:
			request.session['currentPayementRequest'] = None
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
@login_required(login_url = "/login/")
def deleteCartItem(request, itemId):
	ci = request.user.cart.cartitem_set.get(pk=int(itemId))
	print(ci)
	ci.delete()
	processCart(request.user.cart)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



class Home(generic.TemplateView):
	login_form_class = LoginForm
	signup_form_class = UserForm
	form = filterForm()
	def get(self, request, *args, **kwargs):
		template = 'products/home.html'	
		results = Banner.objects.all()

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
			'form': self.form,
			'result': results,
			'all': results,
			'locations': locations,
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
			
			if user is None:
				try:
					ex = ExtendedUser(phone_number = username)
					u = User.objects.get(extendeduser = ex)
					username = u.get_username()
					user = authenticate(username = username, password = password)
				except ExtendedUser.DoesNotExist or User.DoesNotExist:
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


def filterAjax(request):
	if request.is_ajax():
		
		filter_form = parse_qs(request.POST['filter_form'])
		banners = Banner.objects.all()

		qc = Q()
		try:
			if filter_form['user'][0] == '0':
				cart_banner = request.user.cart.cartitem_set.values_list('banner__id', flat = True)
				qc = Q(id__in = list(cart_banner))
		except Exception as e:
			pass

		qo = Q()
		try:
			if filter_form['user'][1] == '0':
				order_banner = request.user.order_set.values_list('orderitem__bookingDetails__banner__id', flat = True)
				qo = Q(id__in = list(order_banner))
		except Exception as e:
			print(e)


		q_dimension = Q()
		try:
			for dim in filter_form['dimensions_banner']:
				q_dimension = q_dimension|Q(banner_dimensions = dim)
		except Exception as e:
			pass
		q_type = Q()
		try:
			for T in filter_form['type_banner']:
				q_type = q_type|Q(banner_type = T)
		except Exception as e:
			pass
		q_light = Q()
		try:
			for L in filter_form['lighted_banner']:
				q_light = q_light|Q(banner_lighted = L)
		except Exception as e:
			pass

		q_price = Q()
		try:
			today_date = datetime.date.today()
			try:
				min_price = filter_form['min_price'][0]
			except Exception as e:
				min_price = 0

			try:
				max_price = filter_form['max_price'][0]
			except Exception as e:
				max_price = 99999999
			
			price_set = PricePeriod.objects.filter(endDate__gte = str(today_date), 
										startDate__lte = str(today_date), 
										price__gte=min_price, 
										price__lte=max_price)
			q_price = q_price|Q(priceperiod__in=price_set)
			
		except Exception as e:
			print(str(e))


		q_date = Q()
		try:
			startDateParsed = datetime.datetime.strptime(filter_form['start_date'][0], "%d/%m/%Y").date()
			endDateParsed = datetime.datetime.strptime(filter_form['end_date'][0], "%d/%m/%Y").date()
			booked_detail_set = BookingDetails.objects.filter(endDate__gte=startDateParsed, startDate__lte=endDateParsed, active=True)
			q_date = q_date|Q(bookingdetails__in = booked_detail_set)
		except Exception as e:
			print(e)




		banner_ids = []
		banner_ids = banners.filter((qo|qc)&q_dimension&q_type&q_light&q_price).exclude(q_date).values_list('id', flat = True)
		print(banner_ids)
		
		data = {
			"ids": list(banner_ids),
		}
		try:
			json_data = json.dumps(data)
		except Exception as e:
			print(e)
		return HttpResponse(json_data, content_type='application/json')


def onclickCardStatus(request):
    if request.is_ajax():
        print(request.POST['id_point'])
        b = Banner.objects.get(pk=int(request.POST['id_point']))
        bookDates = []
        for detailset in b.bookingdetails_set.filter(active = True):
            bookDates.append({'startDate':str(detailset.startDate), 'endDate': str(detailset.endDate)})
        data = {'booking_dates': bookDates}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        raise Http404



def onclickMapPoints(request):
	try:
		if request.is_ajax():
			b = Banner.objects.get(pk=int(request.POST['id_point']))
			bookDates = list()
			bookingDetails_set = b.bookingdetails_set.filter(Q(active = True)&Q(endDate__gte = datetime.date.today())&Q(startDate__lte = (datetime.date.today() + relativedelta(years=1)))).order_by("startDate")
			i = 0
			total_delta = 0
			for detailset in bookingDetails_set:
				try:
					if i > 0:
						lastEndDate = bookingDetails_set[i-1].endDate
						delta2dates = detailset.startDate - lastEndDate
						if(delta2dates.days > 0):
							total_delta+=delta2dates.days
							bookDates.append({'startDate':str(lastEndDate + relativedelta(days=1)), 'endDate': str(detailset.startDate + relativedelta(days=-1)), 'dayPer365':(delta2dates.days-2)*100/365, 'status':"false"})
					elif i == 0:
						if datetime.date.today() < detailset.startDate:
							deltaLateStart = detailset.startDate - datetime.date.today()
							total_delta+=deltaLateStart.days
							bookDates.append({'startDate':str(datetime.date.today()), 'endDate': str(detailset.startDate + relativedelta(days=-1)), 'dayPer365':(deltaLateStart.days)*100/365, 'status':"false"})
					if i != 0:
						delta = detailset.endDate - detailset.startDate
					else:
						delta = detailset.endDate - datetime.date.today()
					total_delta+=delta.days
					bookDates.append({'startDate':str(detailset.startDate), 'endDate': str(detailset.endDate), 'dayPer365':delta.days*100/365, 'status':"true"})
					i+=1

				except Exception as e:
					print(e)
			try:
				if total_delta < 365:
					bookDates.append({'startDate':str(bookDates[-1]["endDate"]), 'endDate': str(datetime.date.today() + relativedelta(years=1)), 'dayPer365':(365-total_delta)*100/365, 'status':"false"})
				else:
					bookDates[-1]["dayPer365"] = bookDates[-1]["dayPer365"] - (total_delta-365)*100/365
			except Exception as e:
				print(e)

			is_favourite = False
			if request.user.is_authenticated():
				try:
					Favourite.objects.get(banner = b, user = request.user)
				except Exception as e:
					is_favourite=False
				else:
					is_favourite = True

			
			context = {"bookdates":bookDates}
			try:
				contact_number = b.agency.user.extendeduser.phone_number
				
			except Exception as e:
				contact_number = "NONE"
			try:
				data = {
				"id" : str(b.id),
				"url": str(b.bannerimage),
				"type": str(type_choices[str(b.banner_type)]),
				"lighted": str(light_choices[str(b.banner_lighted)]),
				"facing" : str(b.banner_facing),
				"landmark" : str(b.banner_landmark),
				"zone" : str(b.zone),
				"lat" : str(b.banner_lattitude),
				"long" : str(b.banner_longitude),
				"dim" : str(dimension_choices[str(b.banner_dimensions)]),
				"bookDates":bookDates,
				"agency_name":b.agency.agency_name,
				"agency_address":b.agency.agency_address,
				"agency_email":b.agency.user.email,
				"agency_phone":contact_number,
				"current_price":b.get_current_price(),
				"is_favourite": is_favourite,
				}
			except Exception as e:
				print(e)
			# print(data)
			
			json_data = json.dumps(data)
			
			return HttpResponse(json_data, content_type='application/json')
		else:
			raise Http404
	except Exception as e:
		print(e)

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

def AjaxAddToFavourites(request):
	if request.is_ajax():
		b = Banner.objects.get(pk=int(request.POST['banner_id']))
		if request.user.is_authenticated():
			try:
				Favourite.objects.get(banner = b, user = request.user)
			except Favourite.DoesNotExist:
				Favourite(user = request.user, banner = b).save()
				data = {
					"success":"1",
					'msg':"added to favourite"
				}
			except Favourite.MultipleObjectsReturned as e:
				print(e)
				for o in Favourite.objects.filter(banner = b, user = request.user):
					o.delete()
			else:
				Favourite.objects.get(banner = b, user = request.user).delete()
				data = {
					"success":"2",
					'msg':"removed from fav"
				}
			# print(data)
			json_data = json.dumps(data)

			return HttpResponse(json_data, content_type='application/json')
		else:
			data = {
					"success":"3",
					'msg':"login please"
				}
			# print(data)
			json_data = json.dumps(data)

			return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404

def AjaxDeleteFavourites(request):
	if request.is_ajax():
		if request.user.is_authenticated():
			try:
				Favourite.objects.get(pk=int(request.POST['fav_id'])).delete()
			except Favourite.DoesNotExist:
				data = {
					"success":"2",
					"fav_id":request.POST['fav_id'],
				}
			else:
				data = {
					"success":"1",
					"fav_id":request.POST['fav_id'],
				}
			# print(data)
			json_data = json.dumps(data)

			return HttpResponse(json_data, content_type='application/json')
		else:
			raise Http404
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
			messages.error(request,"Enter Correct Values In All The Fields")
			print("invalid")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		new_user = form.save(commit=False)
		new_user.username = new_user.email
		password = request.POST['password1']
		new_user.set_password(password)
		try:
			quer = User.objects.get(email=new_user.email)
		except User.DoesNotExist:
			try:
				quer=User.objects.get(username=new_user.username)
			except User.DoesNotExist:
				try:
					quer=ExtendedUser.objects.get(phone_number=request.POST['phone_number'])
				except ExtendedUser.DoesNotExist:
					new_user.save()
					ExtendedUser(user = new_user, phone_number = request.POST['phone_number']).save()
					c = Cart(user = new_user)
					c.save()
					return HttpResponseRedirect("/")
				else:
					messages.error(request, "The phone already exists.")
					print("invalid phone already")
					return HttpResponseRedirect(reverse('auth_register'))
			else:
				messages.error(request, "The username already exists.")
				print("invalid username already")
				return HttpResponseRedirect(reverse('auth_register'))
		else:
			messages.error(request, "The email already exists.")
			print("invalid email already")
			return HttpResponseRedirect(reverse('auth_register'))



# def signup(request):
# 	form = UserForm.form_class(request.POST)
# 	if form.is_valid():
# 		pass
# 	else:
# 		messages.error(request,"Enter Correct Values In All The Fields")
# 		return HttpResponseRedirect("/")
# 	new_user = form.save(commit=False)
# 	password = request.POST['password1']
# 	new_user.set_password(password)
# 	try:
# 		quer = User.objects.get(email=new_user.email)
# 	except User.DoesNotExist:
# 		try:
# 			quer=User.objects.get(username=new_user.username)
# 		except User.DoesNotExist:
# 			try:
# 				quer=ExtendedUser.objects.get(phone_number=new_user.phoneNumber)
# 			except ExtendedUser.DoesNotExist:
# 				new_user.save()
# 				ExtendedUser(user = new_user, phone_number = request.POST['phone_number']).save()
# 				c = Cart(user = new_user)
# 				c.save()
# 				return HttpResponseRedirect("/")
# 			else:
# 				messages.error(request, "The phone already exists.")
# 				print("invalid phone already")
# 				return HttpResponseRedirect(reverse('auth_register'))
# 		else:
# 			messages.error(request, "The username already exists.")
# 			print("invalid username already")
# 			return HttpResponseRedirect(reverse('auth_register'))
# 	else:
# 		messages.error(request, "The email already exists.")
# 		print("invalid email already")
# 		return HttpResponseRedirect(reverse('auth_register'))


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
				try:
					quer=ExtendedUser.objects.get(phone_number=new_user.phoneNumber)
				except ExtendedUser.DoesNotExist:
					new_user.save()
					new_agency.user = new_user
					new_agency.save()
					ExtendedUser(user = new_user, phone_number = request.POST['phone_number']).save()
					c = Cart(user = new_user)
					c.save()
					return HttpResponseRedirect("/")
				else:
					messages.error(request, "The phone already exists.")
					print("invalid phone already")
					return HttpResponseRedirect(reverse('auth_register'))
			else:
				messages.error(request, "The username already exists.")
				print("invalid username already")
				return HttpResponseRedirect(reverse('auth_register'))
		else:
			messages.error(request, "The email already exists.")
			print("invalid email already")
			return HttpResponseRedirect(reverse('auth_register'))




######
#SESSION AND LOGIN LOGOUT
######

class LoginUsers(generic.edit.FormView):
	form_class = LoginForm
	template_name = 'login.html'
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
		if request.user.is_authenticated():
			try:
				if request.session['isAgency'] is not None and request.session['isAgency'] is True:
					return HttpResponseRedirect(reverse('owner_interface'))
			except KeyError:
				return HttpResponseRedirect("/")	
			return HttpResponseRedirect("/")
		try:
			haveNext = False
			nextPage = ""
			try:
				nextPage = request.GET['next']
				haveNext = True
			except:
				print("no next")

			

			username = request.POST['email']
			password = request.POST['password']
			
			user = authenticate(username = username, password = password)
			print(user)
			if user is None:
				try:
					u = User.objects.get(email = username)
					username = u.get_username()
					user = authenticate(username = username, password = password)
				except User.DoesNotExist:
					user = None
			if user is None:
				try:
					ex = ExtendedUser.objects.get(phone_number = username)
					u = ex.user
					username = u.get_username()
					user = authenticate(username = username, password = password)
				except ExtendedUser.DoesNotExist:
					user = None
				except User.DoesNotExist:
					user = None

			if user is not None:
				try:
					a = Agency.objects.get(user = user)
					login(request, user)
					request.session['isAgency'] = True
					request.session['AgencyId'] = a.id
					print("logged in as an agency")
					if not haveNext:
						return HttpResponseRedirect(reverse('owner_interface'))
					else:
						return HttpResponseRedirect(reverse('home') + nextPage)

				except Agency.DoesNotExist:
					login(request, user)
					request.session['isAgency'] = False
					print("logged in as a user")
					print(user.extendeduser.phone_number)
					if not haveNext:
						return HttpResponseRedirect("/")
					else:
						return HttpResponseRedirect(nextPage)
					
			else:
				print("galat daala")
				messages.error(request, "wrong username passowrd", extra_tags = 'wrong_credentials')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		except Exception as e:
			print(e)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





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
			try:
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
			except KeyError:
				
				print("u r not an agency")
				#To-Do: Generate a msg
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			#To-Do: Generate a msg
			messages.error(request, "Login required")
			return HttpResponseRedirect('/login/?next=%s' % (request.path))


######
#CANCEL PAGE
######

class CancelBooking(generic.TemplateView):
	template_name = "cancel-booking.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
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
			except KeyError:
				context = {}
				print("u r not an agency")
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
				#To-Do: Generate a msg
		else:
			print("u need to login")
			#To-Do: Generate a msg
			messages.error(request, "Login required")
			return HttpResponseRedirect('/login/?next=%s' % (request.path))

@login_required(login_url = reverse_lazy('auth_login'), redirect_field_name = reverse_lazy('owner_interface_cancel'))
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
			try:
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
			except KeyError:
				context = {}
				print("u r not an agency")
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			messages.error(request, "Login required")
			return HttpResponseRedirect('/login/?next=%s' % (request.path))


######
#PRICE CHANGE PAGE
######

class PriceBoards(generic.TemplateView):
	template_name = "change-price.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
				if request.session['isAgency'] is not None and request.session['isAgency'] is True:

					username = request.user.username
					a = Agency.objects.get(user = request.user)



					details = []
					for banner in Banner.objects.filter(agency=a):
						bookDates = []

						for booked_date in banner.bookingdetails_set.filter(endDate__gte = datetime.datetime.now().strftime("%Y-%m-%d")):
							bookDates.append({'startDate':str(booked_date.startDate), 'endDate': str(booked_date.endDate)})

						details.append({'banner':banner, 
							'active_booking_details': bookDates,
							'price_set':banner.priceperiod_set.all().order_by('-startDate')[:4][::-1]})

					print(details)
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
			except KeyError:
				context = {}
				print("u r not an agency")
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			messages.error(request, "Login required")
			return HttpResponseRedirect('/login/?next=%s' % (request.path))
			
@login_required(login_url = reverse_lazy('auth_login'), redirect_field_name = reverse_lazy('owner_interface_price'))
def addIndiPrice(request):
	if request.user.is_superuser or (request.session['isAgency'] is not None and request.session['isAgency'] is True):
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
			if not request.user.is_superuser:
				return HttpResponseRedirect(reverse('owner_interface_price'))
			else:
				return HttpResponseRedirect(reverse('price_change_admin'))
		else:
			messages.error(request,"the selected dates have board bookings", extra_tags = "price_change_success")
			if not request.user.is_superuser:
				return HttpResponseRedirect(reverse('owner_interface_price'))
			else:
				return HttpResponseRedirect(reverse('price_change_admin'))
	else:
		messages.error(request, "unauthorised")
		return HttpResponseRedirect("/")
	

######
#booking PAGE
######

class BookHoardings(generic.TemplateView):
	template_name = "book-hoarding.html"
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			try:
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
			except KeyError:
				context = {}
				print("u r not an agency")
				messages.error(request, "you are not authorised to access this page")
				return HttpResponseRedirect("/")
		else:
			print("u need to login")
			messages.error(request, "Login required")
			return HttpResponseRedirect('/login/?next=%s' % (request.path))

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





def share_app(request, o_id):
	template = "app.html"
	username = ""
	userType = ""
	
	if request.user.is_authenticated():
		username = request.user.username
		try:
			Agency.objects.get(user = request.user)
			userType = "Agency"
		except Agency.DoesNotExist:
			userType = "Buyer"
	try:	
		banners = Banner.objects.filter(agency__id = int(o_id))
		banner_details = list()
		
		for banner in banners:
			banner_details.append({
				"id" : str(banner.id),
				"zone": str(banner.zone),
				"facing": str(banner.banner_facing),
				"banner": str(banner.banner_dimensions),
				"type": str(banner.banner_type),
				"lighted": str(banner.banner_lighted),
				"dimension": str(banner.get_banner_dimensions_display()),

				"url": str(banner.bannerimage.image.url),
			})
		context = {'banner_details':banner_details}
		return render(request, template, context)
	except Exception as e:
		print(e)

	return render(request, template, {})





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
			total = total + ((Area[str(banner.banner_dimensions)])*price.price*(delta.days+1)/30.0)
			print(total)
		elif(startDate <= price.endDate and startDate >= price.startDate and endDate > price.endDate):
			delta = price.endDate - startDate + datetime.timedelta(days=1)
			total = total + ((Area[str(banner.banner_dimensions)])*price.price*delta.days/30.0)
			print(total)
		elif(startDate <= price.startDate and endDate >= price.endDate):
			total = total + ((Area[str(banner.banner_dimensions)])*price.price*(price.numberDays+1)/30.0)
			print(total)
		elif(startDate < price.startDate and endDate >= price.startDate and endDate <= price.endDate):
			delta = endDate - price.startDate
			total = total + ((Area[str(banner.banner_dimensions)])*price.price*(delta.days+1)/30.0)
			print(total)
	return round(total,2)


def checkDateRange(startDate, endDate, banner):
	for detailset in banner.bookingdetails_set.filter(active = True):
		if ((detailset.startDate <= startDate and startDate <= detailset.endDate) or 
			(detailset.startDate <= endDate and endDate <= detailset.endDate)  or (booking.startDate >= self.startDate and booking.endDate <= self.endDate)):
			return False
	#TO-DO
	#for cartitem in banner.cartitem_set.filter(cart.user = request.user):
	#	if ((cartitem.startDate <= startDate and startDate <= cartitem.endDate) or 
	#		(cartitem.startDate <= endDate and endDate <= cartitem.endDate)):
	#		messages
	#		return False
	return True
