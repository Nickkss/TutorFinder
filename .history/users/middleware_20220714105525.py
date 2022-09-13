from .models import Profile

class CreateProfile:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_authenticated:
            user = request.user
            profile, created = Profile.objects.get_or_create(user=user)
            
        return self.get_response(request)