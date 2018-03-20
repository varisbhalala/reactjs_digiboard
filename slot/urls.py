from django.urls import path
from . import views

urlpatterns=[
	path('create_slot/',views.create_slot,name='create_slot'),
	# path('list_slot/',views.list_slot,name='list_slot'),
	path('listSlot/',views.listSlot,name = 'listSlot'),
	path('deleteSlot/',views.deleteSlot,name = 'deleteSlot'),
	path('check_slot/', views.check_slot, name= 'check_slot'),
]