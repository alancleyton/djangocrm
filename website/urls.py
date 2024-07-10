from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from website.views import customers as customers_views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('customers')),
    path('customers', customers_views.list_customers, name='customers'),
    path('customers/<int:customer_id>/details', customers_views.show_customer, name='customer'),
    path('search/', customers_views.search_customers, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
