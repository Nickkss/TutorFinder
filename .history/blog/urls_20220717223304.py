from django.urls import path
from users.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.BlogsView.as_view()), name="Blogs"),
]
