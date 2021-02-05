"""HeatMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from Interface.views import change_language
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login/',auth_views.LoginView.as_view(template_name='./registration/login.html'),name='login'),
#     path('logout/',auth_views.LogoutView.as_view(template_name='./registration/logout.html'),name='logout'),
#     path('', include('Interface.urls')),
    
#     ]
urlpatterns = [
    path('change_language/', 
         change_language, 
         name='change_language')
]

urlpatterns+= i18n_patterns(
    path('fs_heatmap/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='./registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='./registration/logout.html'),name='logout'),
    path('', include('Interface.urls')),
    prefix_default_language=True
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)