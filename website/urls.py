from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from website.views import customers as customers_views

urlpatterns = [
    path('', customers_views.list_customers, name='list_customers')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
