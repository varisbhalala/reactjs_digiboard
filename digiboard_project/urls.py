"""digiboard_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from rest_framework.urlpatterns import format_suffix_patterns
from register import views 
from django.views import generic
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('navigation.urls')),
    #path('',include('mail.urls')),
    path('',include('register.urls')),
    path('',include('publisher.urls')),
    path('',include('board.urls')),
    path('',include('slot.urls')),
    path('',include('data.urls')),
    path('',include('advertiser.urls')),
    path('',include('example.urls')),
    path('api-token-verify/', obtain_jwt_token),
    path('react/',generic.TemplateView.as_view(template_name='index.html')),
    # path('api/token/' , TokenObtainPairView.as_view()),
    # path('api/token/refresh' , TokenRefreshView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
