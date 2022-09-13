from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse
from django.db.models.query_utils import Q

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
        data = [mon, tue, wed, thu, fri, sat, sun]
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        
        new_data = []
        
        for index, item in enumerate(data):
            if item:
                new_data.append(days[index])

        tutors = Tutor.objects.all()
        
        new_tutors = []
        
        for nd in new_data:
            for tutor in tutors:
                if nd in tutor.days_avail:
                    if tutor not in new_data:
                        new_tutors.append(tutor)
        
        return new_tutors
            
        
    
    def get(self, request):
        print(self.filter_days(request))
        languages = Language.objects.all()
        tutors = Tutor.objects.all()
        context = {'tutors':tutors, 'langs':languages}
        return render(request, 'tutor/tutors.html', context=context)
    
class TutorView(View):
    def get(self, request, pk):
        tutor = get_object_or_404(Tutor, pk=pk)
        context = {'tutor':tutor}
        return render(request, 'tutor/tutor.html', context=context)