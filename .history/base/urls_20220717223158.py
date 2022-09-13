from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    
    path("", include('frontend.urls')),
    path("auth/", include('users.urls')),
    path("tutors/", include('tutor.urls')),
    path("blogs/", include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))