from django.urls import path, include
from django.conf.urls import url
from attack import views
from django.contrib.auth.views import LoginView

 
app_name = 'attack'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^register/$',  LoginView.as_view(template_name='attack/register.html')),
    url(r'^login/$',  LoginView.as_view(template_name='attack/login.html')),
    url(r'^maintenance-mode/', include('maintenance_mode.urls')),
    #url(r'^admin/exportdb/', include('exportdb.urls')),
    #url(r'^error-500-demo/$', attack_views.error_500_demo, name = 'error_500_demo'),
    #url(r'^advanced_filters/', include('advanced_filters.urls')),
]

#urlpatterns = patterns('', url(r'^$', views.home, name='home'))
