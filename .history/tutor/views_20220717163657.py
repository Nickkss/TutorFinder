from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse

from language.models import Language
from .models import Tutor

# Create your views here.

class TutorsView(View):
    def filter_days(self, request):
        get = request.GET
        mon = get.get('mon', None)
        tue = get.get('tue', None)
        wed = get.get('wed', None)
        thu = get.get('thu', None)
        fri = get.get('fri', None)
        sat = get.get('sat', None)
        sun = get.get('sun', None)
    
    def get(self, request):
        
        languages = Language.objects.all()
        tutors = Tutor.objects.all()
        context = {'tutors':tutors, 'langs':languages}
        return render(request, 'tutor/tutors.html', context=context)
    
class TutorView(View):
    def get(self, request, pk):
        tutor = get_object_or_404(Tutor, pk=pk)
        context = {'tutor':tutor}
        return render(request, 'tutor/tutor.html', context=context)