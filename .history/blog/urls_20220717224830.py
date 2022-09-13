from django.urls import path
from users.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.BlogsView.as_view()), name="Blogs"),
    path('<slug>/', login_required(views.BlogView.as_view()), name="Blog"),
]
