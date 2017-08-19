from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from products import views as productsViews

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', productsViews.Home.as_view(), name='home'),
    url(r'^s/$', 'products.views.search', name='search'),

    

    url(r'^products/$', 'products.views.all', name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),
    url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
    url(r'^cart/$', 'carts.views.view', name='cart'),
    url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
    url(r'^orders/$', 'orders.views.orders', name='user_orders'),
    url(r'^ajax/dismiss_marketing_message/$', 'marketing.views.dismiss_marketing_message', name='dismiss_marketing_message'),
    url(r'^ajax/email_signup/$', 'marketing.views.email_signup', name='ajax_email_signup'),
    url(r'^ajax/add_user_address/$', 'accounts.views.add_user_address', name='ajax_add_user_address'),
    url(r'^ajax/onclickMapPoints/$', 'products.views.onclickMapPoints', name='onclickMapPoints'),

    # url(r'^blog/', include('blog.urls')),
    #(?P<all_items>.*)
    #(?P<id>\d+)
    

    url(r'^register/$', productsViews.Signup.as_view(), name='auth_register'),
    url(r'^register/$', 'products.views.signup', name='auth_register2'),
    url(r'^registerowner/$', productsViews.SignupOwner.as_view(), name='auth_register_owner'),
    url(r'^logout/$', 'products.views.logoutUser', name='auth_logout'),
    url(r'^login/$', productsViews.LoginUsers.as_view(), name='auth_login'),




    url(r'^owner/home/$', productsViews.OwnerInterfaceHome.as_view(), name='owner_interface'),
    url(r'^owner/book/$', productsViews.BookHoardings.as_view(), name='owner_interface_book'),
    url(r'^owner/cancel/$', productsViews.CancelBooking.as_view(), name='owner_interface_cancel'),
    url(r'^owner/status/$', productsViews.StatusBoards.as_view(), name='owner_interface_status'),
    url(r'^owner/price/$', productsViews.PriceBoards.as_view(), name='owner_interface_price'),


    url(r'^owner/book/confirm$', 'products.views.bookBoards', name='owner_interface_book_board'),
    url(r'^owner/cancel/cancel$', 'products.views.cancelBoard', name='owner_interface_cancel_board'),
    url(r'^owner/price/add$', 'products.views.addIndiPrice', name='owner_interface_add_new_price_indi'),

    url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^accounts/address/add/$', 'accounts.views.add_user_address', name='add_user_address'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),
) 


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)