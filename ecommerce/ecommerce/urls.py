from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from products import views as productsViews

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^map-view$', productsViews.Home.as_view(), name='map_view'),
    url(r'^adminPriceChanger/$', 'products.views.adminPriceChanger', name='price_change_admin'),
    url(r'^printing_material/$', 'products.views.printing_material', name='printing_material'),
    url(r'^buyer_cart/$', 'products.views.buyer_cart', name='buyer_cart'),
    url(r'^addToCart/$', 'products.views.addToCart', name='addToCart'),
    url(r'^booking_status/$', 'products.views.booking_status', name='booking_status'),
    url(r'^check_out/$', 'products.views.check_out', name='check_out'),
    url(r'^clear_cart/$', 'products.views.clear_cart', name='clear_cart'),
    url(r'^buyer_cart/deleteItem/([0-9]+)$', 'products.views.deleteCartItem', name='cart_deleteItem'),
    url(r'^buyer_cart/editCartItemAjax', 'products.views.editCartItemAjax', name='cart_editItem'),
    url(r'^buyer_cart/editCartItem', 'products.views.editCartItem', name='cart_editItemFinal'),
    url(r'^process_payment/$', 'products.views.processPayment', name='cart_process_payment'),
    url(r'^dashboard/$', 'products.views.dashboard', name='dashboard'),
    url(r'^favourites/$', 'products.views.favourites', name='favourites'),

    url(r'^$', 'products.views.index_new_home', name='home'),
    

    url(r'^ajax/onclickMapPoints/$', 'products.views.onclickMapPoints', name='onclickMapPoints'),
    url(r'^ajax/AjaxBannerPrice/$', 'products.views.AjaxBannerPrice', name='AjaxBannerPrice'),
    url(r'^ajax/AjaxFormFilter/$', 'products.views.filterAjax', name='filter_form'),
    # url(r'^blog/', include('blog.urls')),






    url(r'^register/$', productsViews.Signup.as_view(), name='auth_register'),
    # url(r'^register/$', 'products.views.signup', name='auth_register2'),
    url(r'^registerowner/$', productsViews.SignupOwner.as_view(), name='auth_register_owner'),
    url(r'^logout/$', 'products.views.logoutUser', name='auth_logout'),
    url(r'^login/$', productsViews.LoginUsers.as_view(), name='auth_login'),

    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
            name="password_reset"),
    
    url(r'^user/password/reset/done/$',
            'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
            'django.contrib.auth.views.password_reset_confirm', 
            {'post_reset_redirect' : '/user/password/done/'}, name='password_reset_confirm'),
    url(r'^user/password/done/$', 
            'django.contrib.auth.views.password_reset_complete'),

    
    url(r'^auth/', include('social_django.urls', namespace='social')),








    url(r'^owner/home/$', productsViews.OwnerInterfaceHome.as_view(), name='owner_interface'),
    url(r'^owner/book/$', productsViews.BookHoardings.as_view(), name='owner_interface_book'),
    url(r'^owner/cancel/$', productsViews.CancelBooking.as_view(), name='owner_interface_cancel'),
    url(r'^owner/status/$', productsViews.StatusBoards.as_view(), name='owner_interface_status'),
    url(r'^owner/price/$', productsViews.PriceBoards.as_view(), name='owner_interface_price'),


    url(r'^owner/book/confirm$', 'products.views.bookBoards', name='owner_interface_book_board'),
    url(r'^owner/cancel/cancel$', 'products.views.cancelBoard', name='owner_interface_cancel_board'),
    url(r'^price/add$', 'products.views.addIndiPrice', name='add_new_price_indi'),

    url(r'^aboutus/$', 'products.views.aboutus', name='aboutus'),
    url(r'^directions/$', 'products.views.directions', name='directions'),
    url(r'^faq/$', 'products.views.faq', name='faq'),
  
    url(r'^uploadImage/$', 'products.views.uploadImage', name='uploadImage'),
    url(r'^singleFaq/$', 'products.views.single-faq', name='single-faq'), #change faq @sidd
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
