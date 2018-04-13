from django.urls import path
from . import views

urlpatterns=[
	path('create_board/',views.create_board,name='create_board'),
	path('save_board',views.save_board,name='save_board'),
	path('get_board/',views.get_board,name='get_board'),
	path('list_board',views.list_board,name='list_board'),
	path('test_bootstrap',views.test_bootstrap,name='test_bootstrap'),
    path('requests/',views.requests,name='requests'),
    path('accept_or_decline/',views.accept_or_decline,name="accept_or_decline"),
    path('get_board_api/', views.get_board_api),
	path('create_board_api/' , views.create_board_api),
	path('search_board_api/' , views.search_board_api)
]