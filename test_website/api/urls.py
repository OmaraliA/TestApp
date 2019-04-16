from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('lectures/', views.lecture_list, name='lecture'),
    path('lectures/test/', views.testing, name='testing'),
    path('lectures/<int:pk>/', views.lecture_details, name="lecturedetails"),
    path('lectures/<int:pk>/test/', views.test_details, name = "testdetails"),
    path('users/', views.user_list),
]
