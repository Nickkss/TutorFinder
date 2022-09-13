from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse

from .models import Tutor

# Create your views here.

class TutorsView(View):
    def get(self, request):
        return render(request, 'tutor/tutors.html')