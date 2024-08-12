from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Root URL
    path('signup/', views.signup_view, name='signup'),  # Root URL
    path('home/', views.home_view, name='home'),  # Root URL
]