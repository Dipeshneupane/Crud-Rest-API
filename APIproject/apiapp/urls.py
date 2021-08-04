from django.urls import path 
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/books', BookList.as_view()),
    path('api/books/<int:pk>', BookDetail.as_view())
]
