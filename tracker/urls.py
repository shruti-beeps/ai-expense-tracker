from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # FIRST PAGE = REGISTER
    path('', views.register, name='register'),

    # LOGIN PAGE
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    # HOME PAGE
    path('home/', views.home, name='home'),

    # ADD EXPENSE
    path('add/', views.add_expense, name='add_expense'),

    # EDIT EXPENSE
    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),

    # DELETE EXPENSE
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
]