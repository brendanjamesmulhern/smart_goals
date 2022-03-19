from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.apiOverview, name='Home'),
    path('/register', views.register, name='register'),
    path('/login', views.login, name='login'),
    path('goal-create/', views.add_goal, name='add-items'),
    path('goal-list/', views.goal_list, name='goal-list'),
    path('goal-update/<str:pk>/', views.goal_update, name='goal-update'),
    path('goal-delete/<str:pk>/', views.goal_delete, name='goal-delete'),
]