from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from search.views import search, index, signup, home, account_activation_sent, activate
from django.contrib.auth import views as auth_views

from django_filters.views import FilterView

from mysite.search.filters import UserFilter


urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^$', index, name='index'),
    url(r'^search/$', search, name='search'),
    # url(r'^signup/$', signup, name='signup'),
    # url(r'^contact/$', contact, name='contact'),
    # url(r'^search/$', FilterView.as_view(filterset_class=UserFilter, template_name='search/user_list.html'), name='search'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
     url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^captcha/', include('captcha.urls')),
]
