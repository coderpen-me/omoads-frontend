from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from products import views as productsViews

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', productsViews.Home.as_view(), name='home'),

    url(r'^buyer_cart/$', 'products.views.buyer_cart', name='buyer_cart'),
    url(r'^addToCart/$', 'products.views.addToCart', name='addToCart'),
    url(r'^booking_status/$', 'products.views.booking_status', name='booking_status'),
    url(r'^check_out/$', 'products.views.check_out', name='check_out'),
    url(r'^clear_cart/$', 'products.views.clear_cart', name='clear_cart'),
    url(r'^buyer_cart/deleteItem/([0-9]+)$', 'products.views.deleteCartItem', name='cart_deleteItem'),
    url(r'^buyer_cart/editCartItemAjax', 'products.views.editCartItemAjax', name='cart_editItem'),
    url(r'^buyer_cart/editCartItem', 'products.views.editCartItem', name='cart_editItemFinal'),
    url(r'^process_payment/$', 'products.views.processPayment', name='cart_process_payment'),
    

    url(r'^ajax/onclickMapPoints/$', 'products.views.onclickMapPoints', name='onclickMapPoints'),
    url(r'^ajax/AjaxBannerPrice/$', 'products.views.AjaxBannerPrice', name='AjaxBannerPrice'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^register/$', productsViews.Signup.as_view(), name='auth_register'),
    # url(r'^register/$', 'products.views.signup', name='auth_register2'),
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

    url(r'^aboutus/$', 'products.views.aboutus', name='aboutus'),
    url(r'^directions/$', 'products.views.directions', name='directions'),
    url(r'^faq/$', 'products.views.faq', name='faq'),
    url(r'^uploadImage/$', 'products.views.uploadImage', name='uploadImage'),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)