from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse
from django.db.models.query_utils import Q
from django.http import QueryDict
from django.db.models.query import QuerySet

from language.models import Language, LangLevel
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
        charges_gte = get.get('charges_gte', None)
        charges_lte = get.get('charges_lte', None)
        
        if charges_gte and charges_lte:
            if not str(charges_gte).isdigit():
                charges_gte = 100
                
            if not str(charges_lte).isdigit():
                charges_lte = 5000
            
            tutors = tutors.filter(Q(charges__gte=charges_gte)&Q(charges__lte=charges_lte))
            
            for tutor in tutors:
                if tutor not in new_tutors:
                    new_tutors.append(tutor)
        # Filter Language
        lang_id = get.get('language', None)
        _lang_level = get.get('lang_level', 1)
        language = None
        print(lang_id)
        try:
            if not str(_lang_level).isdigit():
                _lang_level = 1
            
            language = Language.objects.get(id=lang_id)
            lang_level = LangLevel.objects.filter(Q(language=language, level__lte=_lang_level))
            tutors = tutors.filter(Q(i_speak__in=lang_level))
            for tutor in tutors:
                if tutor not in new_tutors:
                    new_tutors.append(tutor)
        except Exception as ex:
            print(ex)
        
        print(any(new_days) or language or all([charges_gte, charges_lte]))
        if any(new_days) or language or all([charges_gte, charges_lte]):#if any(days):
            return (new_tutors, new_days, (charges_gte, charges_lte), language, _lang_level)
        else:
            return (list(tutors), None, None, None, None)
            
        
    
    def get(self, request):
        languages = Language.objects.all()
        filter_data = self.filter_tutors(request)
        tutors = filter_data[0]
        tutors_count = len(tutors)
        context = {'tutors':tutors, 'langs':languages, 'tutors_count':tutors_count}
        
        new_days = filter_data[1]
        if new_days:
            new_days_dict = dict(zip(new_days, [True for x in new_days]))
            context.update(new_days_dict)
        
        charges = filter_data[2]
        if charges:
            charges_dict = dict(zip(['charges_gte', 'charges_lte'], charges))
            context.update(charges_dict)
            
        language = filter_data[3]
        lang_level = filter_data[4]
        if language:
            context.update({'language':language, 'lang_level':lang_level})
        
        # tutors = Tutor.objects.all()
        return render(request, 'tutor/tutors.html', context=context)
    
class TutorView(View):
    def get(self, request, pk):
        tutor = get_object_or_404(Tutor, pk=pk)
        context = {'tutor':tutor}
        return render(request, 'tutor/tutor.html', context=context)