from django.shortcuts import render
from django.views import View

from blog.models import Blog

# Create your views here.

class BlogsView(View):
    def get(self, request):
        return render(request, "blog/blogs.html")