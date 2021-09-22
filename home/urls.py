from django.urls import path, include
from . import views

app_name='home'

urlpatterns=[
    path('/',views.home, name='home'),
    path('search', views.search, name='search'),
    path('<int:id>/sold_info', views.sold_info, name='sold_info'),
]