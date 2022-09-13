from .models import StudentProfile, TutorProfile

class CreateProfile:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_authenticated:
            user = request.user
            if user.role == 1:
                profile, created = TutorProfile.objects.get_or_create(user=user)
            else:
                profile, created = StudentProfile.objects.get_or_create(user=user)
            
        return self.get_response(request)