from .models import SiteSettings

def site_settings(request):
    return {'settings': SiteSettings.load()}