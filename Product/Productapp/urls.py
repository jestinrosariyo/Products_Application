from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('user.html',views.userDetails),
    path('type.html',views.typeShow),
    path('/user.html/<str:types>',views.getDetails, name='user'),
]