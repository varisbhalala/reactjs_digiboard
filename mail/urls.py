
from django.urls import path , include
from . import views

urlpatterns = [
    path('mail/', views.mail,name='mail'),
]
