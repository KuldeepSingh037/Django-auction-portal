from django.urls import path
from . import views

app_name='login'

urlpatterns=[
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logout, name='logout'),
    
]



