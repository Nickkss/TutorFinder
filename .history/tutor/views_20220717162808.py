from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse

from language.models import Language
from .models import Tutor

# Create your views here.

class TutorsView(View):
    def get(self, request):
        tutors = Tutor.objects.all()
        context = {'tutors':tutors}
        return render(request, 'tutor/tutors.html', context=context)
    
class TutorView(View):
    def get(self, request, pk):
        tutor = get_object_or_404(Tutor, pk=pk)
        context = {'tutor':tutor}
        return render(request, 'tutor/tutor.html', context=context)