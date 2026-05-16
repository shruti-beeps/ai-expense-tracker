from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add/', views.add_expense, name='add_expense'),

    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),

    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
]