from django.urls import path
from example.views import user_list,log_in,log_out,sign_up


urlpatterns = [
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('sign_up/', sign_up, name='sign_up'),
    path('', user_list, name='user_list'),
]
