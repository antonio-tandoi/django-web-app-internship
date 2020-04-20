from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .models import Attacks, Categories, Values
from django.contrib.auth.decorators import login_required
from django.http import Http404

#site.site_title = 'App'

# def index(request):
#     latest_attack_list = Attacks.objects.order_by('name')
#     template = loader.get_template('attack/index.html')
#     context = {
#         'latest_attack_list': latest_attack_list,
#     }
#     return render(request, 'attack/index.html', {
# 	'latest_attack_list': latest_attack_list,
# 	'error_message': "Impossibile", })

def index(request):
    numbers = [1, 2, 3, 4]
    name = "Nome nome"
    args = {
        'myName': name,
        'numbers': numbers
        }
    return render(request, 'attack/home.html', args)
    
    
def home(request):
    pass

def error_404_view(request, exception):
    return render(request, 'attack/404.html')

# def error_500_view(request):
#     return render(request, 'attack/500.html')
# 
# def error_500_demo(request):
#     return render(request, 'attack/500.html')



