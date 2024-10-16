from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('home/', views.home, name='home'),  
    path('booking/', views.booking, name='booking'),
    path('booking_detail/', views.booking_detail, name='booking_detail'),
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]


# <int:field_id>/