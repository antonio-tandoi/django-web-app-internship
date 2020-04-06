from django.urls import path
from django.conf.urls import url
from attack import views
from django.contrib.auth.views import LoginView

 
app_name = 'attack'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^register/$',  LoginView.as_view(template_name='attack/register.html')),
    url(r'^login/$',  LoginView.as_view(template_name='attack/login.html'))
]

#urlpatterns = patterns('', url(r'^$', views.home, name='home'))
