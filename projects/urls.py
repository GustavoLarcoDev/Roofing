from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'),
         name='logout'),
    path('project/<int:project_id>/', views.project_detail,
         name='project_detail'),
    path('admin/projects/', views.admin_project_list,
         name='admin_project_list'),
    path('admin/projects/<int:project_id>/edit/', views.admin_project_edit,
         name='admin_project_edit'),
    path('admin/projects/create/', views.admin_project_create,
         name='admin_project_create'),

]
