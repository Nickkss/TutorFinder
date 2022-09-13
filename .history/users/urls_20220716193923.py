from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="Register"),
    path('signup/', views.RegisterView.as_view(), name="Signup"),
    
    path('login/', views.LoginView.as_view(), name="Login"),
    path('signin/', views.LoginView.as_view(), name="Signin"),
    
    path('logout/', login_required(views.LogoutView.as_view()), name="Logout"),
    
    path('profile/', login_required(views.ProfileView.as_view()), name="Profile"),
    
]