from django.urls import path , include
from . import views

urlpatterns = [
<<<<<<< HEAD
    # path('navigation/',views.navigation,name='navigation'),                     #0.0
    # #path('temp/',views.register,name='temp'),
    # path('register/',views.register,name='register'),                           #1.1
    # path('ajaxData/',views.ajaxData,name='ajaxData'),                           #1.1.1
    # path('check_user/',views.check_user,name='check_user'), 
    # path('check_email/',views.check_email_reg,name='check_email'),

    # #path('login/' , views.login,name='login'),                                  #2.0.0
    # path('forgot_password/', views.forgot_password, name='forgot_password'),    #2.1.1
    # path('check_email/', views.check_email, name='check_email'),                #2.1.2
    # path('new_password/', views.new_password, name='new_password'),             #2.1.3
    # path('save_password/', views.save_password, name='save_password'),          #2.1.4
    
    # path('logout/' , views.logout,name='logout'),                               #3.0

    # path('create_board',views.create_board,name="create_board"),                #4.0
    # path('save_board',views.save_board,name='save_board'),
    # path('get_board',views.get_board,name='get_board'),
=======
    path('navigation/',views.navigation,name='navigation'),                     #0.0
    #path('temp/',views.register,name='temp'),
    path('register/',views.register,name='register'),                           #1.1
    path('ajaxData/',views.ajaxData,name='ajaxData'),                           #1.1.1
    path('check_user/',views.check_user,name='check_user'),
    path('check_email/',views.check_email_reg,name='check_email'),

    path('login/' , views.login,name='login'),                                  #2.0.0
    path('forgot_password/', views.forgot_password, name='forgot_password'),    #2.1.1
    path('check_email/', views.check_email, name='check_email'),                #2.1.2
    path('new_password/', views.new_password, name='new_password'),             #2.1.3
    path('save_password/', views.save_password, name='save_password'),          #2.1.4

    path('logout/' , views.logout,name='logout'),                               #3.0

    path('create_board',views.create_board,name="create_board"),                #4.0
    path('save_board',views.save_board,name='save_board'),
    path('get_board',views.get_board,name='get_board'),
    
    path('support_get_board',views.support_get_board,name='support_get_board'),
    path('search/' , views.search , name='search'),
    path('search_done/' , views.search_done , name='search_done'),
    path('slot', views.slot, name='slot'),
    path('save_slot', views.save_slot, name='save_slot')
>>>>>>> 2f558a3a014656362040ae9244468ad07864daf9
]
