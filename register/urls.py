from django.urls import path
from . import views
from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('registration/',views.first_step_reg,name='registration'),
	# path('confirmMail/',views.confirmMail,name='confirmMail'),
	path('ajaxData/',views.ajaxData,name='ajaxData'),
	path('profile/',views.profile,name='profile'),
	path('welcome/',views.welcome,name='welcome'),
	path('login/',views.login,name='login'),
	path('logout/',views.logout,name='logout'),
	path('check_user/',views.check_user,name='check_user'),
	path('check_email/',views.check_email,name='check_email'),
	path('list/', views.userList),
	# path('list_data/', views.userListViewSet.as_view()),
	path('confirmMail/', views.confirmMail_api),
	path('profile_submit/',views.profile_submit),
	path('login_api/' , views.login_api),
	path('api-token-refresh/', refresh_jwt_token),
	path('id_api/' , views.id_api)
]