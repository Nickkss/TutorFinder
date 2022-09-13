from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import User, TutorProfile, StudentProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm, TutorProfileForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    
    
    
    def avtar_image(self, instance):
        return format_html("""<img src="{}" style="width:30px; height:100%;float:left;object-fit:cover;"/>""".format(instance.avtar.url))
    
    avtar_image.short_description = "Avtar"

    model = User

    list_display = ('username', 'email', 'name', 'avtar_image', 'role', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active',)
    fieldsets = (
        ("Credentials", {'fields': ('username', 'password', 'role')}),
        ('Personal Info', {'fields': ('name', 'email', 'avtar',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Contact Info', {'fields':('phone', 'country', 'state', 'city', 'address')}),
        ('Important Dates', {'fields':('date_joined', 'last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('name', 'username', 'phone', 'email',)
    ordering = ('username', )
    
class Tutor(User):
    class Meta:
        proxy = True

class TutorAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        obj.role = 1
        super().save_model(request, obj, form, change)
        
    def get_queryset(self, request):
        return self.model.objects.filter(role = 1)
    
    def avtar_image(self, instance):
        return format_html("""<img src="{}" style="width:30px; height:100%;float:left;object-fit:cover;"/>""".format(instance.avtar.url))
    
    avtar_image.short_description = "Avtar"

    model = User

    list_display = ('username', 'email', 'name', 'avtar_image', 'role', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active',)
    fieldsets = (
        ("Credentials", {'fields': ('username', 'password', 'role')}),
        ('Personal Info', {'fields': ('name', 'email', 'avtar',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Contact Info', {'fields':('phone', 'country', 'state', 'city', 'address')}),
        ('Important Dates', {'fields':('date_joined', 'last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('name', 'username', 'phone', 'email',)
    ordering = ('username', )

class Student(User):
    class Meta:
        proxy = True
        
class StudentAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        obj.role = 2
        super().save_model(request, obj, form, change)
        
    def get_queryset(self, request):
        return self.model.objects.filter(role = 2)
    
    def avtar_image(self, instance):
        return format_html("""<img src="{}" style="width:30px; height:100%;float:left;object-fit:cover;"/>""".format(instance.avtar.url))
    
    avtar_image.short_description = "Avtar"

    model = User

    list_display = ('username', 'email', 'name', 'avtar_image', 'role', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active',)
    fieldsets = (
        ("Credentials", {'fields': ('username', 'password', 'role')}),
        ('Personal Info', {'fields': ('name', 'email', 'avtar',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Contact Info', {'fields':('phone', 'country', 'state', 'city', 'address')}),
        ('Important Dates', {'fields':('date_joined', 'last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('name', 'username', 'phone', 'email',)
    ordering = ('username', )

class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'charges', 'about_me', 'created_on', 'updated_on']
    
    form = TutorProfileForm

admin.site.register(User, CustomUserAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Student, StudentAdmin)

admin.site.register(TutorProfile, TutorProfileAdmin)
admin.site.register(StudentProfile)