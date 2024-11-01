from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'),
         name='logout'),

]
