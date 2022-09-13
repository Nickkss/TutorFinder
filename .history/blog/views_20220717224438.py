from django.shortcuts import render, get_object_or_404
from django.views import View

from blog.models import Blog

# Create your views here.

class BlogsView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {'blogs':blogs}
        
        return render(request, "blog/blogs.html", context=context)
    
class BlogView(View):
    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        
        context = {'blog':blog}
        
        return render(request, 'blog/blog.html', context=context)