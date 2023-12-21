from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import crm_system.views

urlpatterns = [
    path('crm_system/', include('crm_system.urls')),
    path('admin/', admin.site.urls),
    path('', crm_system.views.mainpage, name='mainpage'),
    path('devices/', crm_system.views.get_devices, name='get_devices'),
    path('devpage/', crm_system.views.devpage, name='devpage')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
