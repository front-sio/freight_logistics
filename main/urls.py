from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_detail, name='about_detail'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),


    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.admin_users, name='admin_users'),
    path('content/', views.admin_content, name='admin_content'),
    path('reports/', views.admin_reports, name='admin_reports'),
    path('settings/', views.admin_settings, name='admin_settings'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
