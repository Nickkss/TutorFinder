from django.shortcuts import render
from django.views import View
from django.db.models.query_utils import Q
from django.contrib import messages

from users.models import User
from tutor.models import Tutor
from blog.models import Blog

# Create your views here.

class HomeView(View):
    def get(self, request):
        tutors = Tutor.objects.all()
        blogs = Blog.objects.all().order_by('-created_on')[0:3]
        context = {'tutors':tutors, 'blogs':blogs}
        return render(request, "index.html", context=context)
    
def splash(request):
    return render(request, 'splash.html')