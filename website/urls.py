from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from website.views import customers as customers_views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('customers')),
    path('customers', customers_views.index, name='customers'),
    path('customers/<int:customer_id>/show', customers_views.show, name='customer'),
    path('search/', customers_views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
