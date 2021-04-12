from django.urls import path

from account import views

urlpatterns = [
    path('', views.register_view),
    path('login/', views.LoginView.as_view()),
    path('current-user/', views.current_user_view),
]
