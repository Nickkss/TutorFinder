from django.urls import path
from users.decorators import login_required

from . import views

app_name = "tutor"

urlpatterns = [
    path('', login_required(views.TutorsView.as_view()), name="Tutors"),
]
