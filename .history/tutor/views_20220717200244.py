from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse
from django.db.models.query_utils import Q
from django.http import QueryDict
from django.db.models.query import QuerySet

from language.models import Language
from .models import Tutor

# Create your views here.

class TutorsView(View):
    def filter_tutors(self, request):
        get = request.GET
        
        # Filter Days
        mon = get.get('mon', None)
        tue = get.get('tue', None)
        wed = get.get('wed', None)
        thu = get.get('thu', None)
        fri = get.get('fri', None)
        sat = get.get('sat', None)
        sun = get.get('sun', None)
        data = [mon, tue, wed, thu, fri, sat, sun]
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        
        new_days = []
        
        for index, item in enumerate(data):
            if item:
                new_days.append(days[index])

        tutors = Tutor.objects.all()
        
        new_tutors = []
        
        for nd in new_days:
            for tutor in tutors:
                if nd in tutor.get_days_avail_display():
                    if tutor not in new_tutors:
                        new_tutors.append(tutor)
                        
        # Filter Charges
        charges_start = get.get('charges_start', 100)
        charges_end = get.get('charges_end', 5000)
        
        tutors = tutors.filter(Q(charges__gte=charges_start)&Q(charges__lte=charges_end))
        
        for tutor in tutors:
            if tutor not in new_tutors:
                new_tutors.append(tutor)
        
        if any(days):
            return (new_tutors, new_days)
        else:
            return (tutors, None)
            
        
    
    def get(self, request):
        languages = Language.objects.all()
        filter_data = self.filter_tutors(request)
        tutors = filter_data[0]
        new_days = filter_data[1]
        new_days_dict = dict(zip(new_days, [True for x in new_days]))
        
        # tutors = Tutor.objects.all()
        context = {'tutors':tutors, 'langs':languages}
        context.update(new_days_dict)
        return render(request, 'tutor/tutors.html', context=context)
    
class TutorView(View):
    def get(self, request, pk):
        tutor = get_object_or_404(Tutor, pk=pk)
        context = {'tutor':tutor}
        return render(request, 'tutor/tutor.html', context=context)