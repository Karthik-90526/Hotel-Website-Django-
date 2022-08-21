from django.contrib import admin
from django.urls import path
from Hotelapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('validate', views.validate, name = 'validate'),
    path('login', views.login, name = 'login'),
    path('welcome', views.payment, name = 'welcome'),
]