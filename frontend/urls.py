from django.urls import path

from users.decorators import login_required

from . import views

app_name = "frontend"

urlpatterns = [
    path('', login_required(views.HomeView.as_view(), allowed_roles=[1,2]), name="Home"),
    path('splash/', views.splash, name="splash"),
]
