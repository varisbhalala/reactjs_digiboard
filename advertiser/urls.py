from django.urls import path
from . import views

urlpatterns=[
	path('advertiser/',views.advertiser,name='advertiser'),
	path('search/',views.search,name="search"),
	path('search_done/',views.search_done,name="search_done"),
	path('make_ad/',views.make_ad,name='make_ad'),
	path('imp_master',views.imp_master,name='imp_master'),
	path('plan', views.plan, name='plan'),
	path('request_board/', views.request_board, name='request_board'),
	path('upload_content/', views.upload_content, name="upload_content"),
	path('submit_content/', views.submit_content, name="submit_content"),
	path('push_request/',views.push_request,name='push_request'),
	path('advertiser_notify/',views.advertiser_notify,name='advertiser_notify'),
	path('pay/', views.pay , name="pay"),
	path('pay_charge/' , views.pay_charge, name="pay_charge"),
	path('payment_api/' , views.payment_api)
]

