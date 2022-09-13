from django.shortcuts import render
from django.views import View
from django.db.models.query_utils import Q

from users.models import User

# Create your views here.

class HomeView(View):
    def get(self, request):
        tutors = User.objects.filter(Q(role=1))
        context = {'tutors':tutors}
        return render(request, "index.html", context=context)
    
def splash(request):
    return render(request, 'splash.html')