from django.urls import path
from . import views

urlpatterns=[
	path('publisher/',views.publisher,name='publisher'),
]