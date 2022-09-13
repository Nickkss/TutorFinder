from django.shortcuts import render
from django.views import View
from django.db.models.query_utils import Q
from django.contrib import messages

from users.models import User
from tutor.models import Tutor

# Create your views here.

class HomeView(View):
    def get(self, request):
        
        messages.info(request, "Testing message !")
        
        tutors = Tutor.objects.all()
        context = {'tutors':tutors}
        return render(request, "index.html", context=context)
    
def splash(request):
    return render(request, 'splash.html')