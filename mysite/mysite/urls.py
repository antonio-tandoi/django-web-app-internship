from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, handler404, handler500



urlpatterns = [
    path('attack/', include('attack.urls')),  
    path('admin/', admin.site.urls),
    url(r'^admin/exportdb/', include('exportdb.urls')),
    path('', RedirectView.as_view(url='/attack/login', permanent=True)),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

handler404 = 'attack.views.error_404_view'
#handler500 = 'attack.views.error_500_view'