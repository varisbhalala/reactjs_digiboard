from django.urls import path
from . import views

urlpatterns = [
    path('state/',views.state_api),
    path('cities/',views.city_api)
]