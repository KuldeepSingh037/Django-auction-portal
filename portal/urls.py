from django.urls import path
from . import views

app_name='portal'

urlpatterns=[
    path('<int:cid>/create_auction', views.auction, name='auction'),
    path('<int:cid>/detail', views.detail, name='detail'),
    path('<int:bid>/particular', views.particular, name='particular'),
    path('<int:bid>/bid', views.bid, name='bid'),
]

########
# add in the policy that auction of every property will be ccloaseds at the midnight only






