from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils import timezone
from django.views import View
from django.db.models import Q
from django.conf import settings

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from .forms import CustomUserCreationForm

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Already Registerd !")
            return redirect(reverse('frontend:Home'))
        else:
            form = CustomUserCreationForm()
            context = {'form':form}
            return render(request, 'auth/register.html', context=context)
    
    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            messages.success(request, 'Registered successfully!')
            return redirect(reverse("frontend:Home"))
        else:
            messages.warning(request, f"Errors : {form.errors}")
            context = {'form':form}
            return render(request, 'auth/register.html', context=context)
            #return redirect(reverse("users:Register"))
        
class LoginView(View):
    def get(self, request):
        next = request.GET.get('next', "/")
        context = {"next":next}
        if request.user.is_authenticated:
            messages.info(request, "Already Logged In !")
            return redirect(reverse('frontend:Home'))
        else:
            return render(request, 'auth/login.html', context=context)
        
    def is_user_banned(self, email):
        try:
            user = User.objects.get(Q(email=email))
            return (not user.is_active)
        except Exception as ex:
            return False
    
    def post(self, request):
        email = request.POST.get('username', None)
        form = AuthenticationForm(request, data=request.POST)
        next = request.POST.get('next', None)
        if self.is_user_banned(email):
            messages.warningerror(request, "Your account is deactivated, please contact us for support.")
            return redirect(reverse("frontend:Home"))
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user.last_login = timezone.now()
                user.save()
                
                messages.success(request, f"You are now logged in as {user.name}")
                try:
                    if next:
                        return redirect(next)
                except Exception as ex:
                    pass
                return redirect(reverse("frontend:Home"))
            else:
                messages.error(request,"Email or Password is Wrong !")
                return redirect(reverse('users:Login'))
        else:
            messages.error(request,"User Not Found !")
            return redirect(reverse("users:Login"))
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You Just Logged Out !")
        return redirect(reverse('frontend:Home'))
