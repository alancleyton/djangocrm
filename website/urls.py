from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponseRedirect

from website.views import customers as customers_views
from website.views import users as users_views

urlpatterns = [
    path('', lambda r: HttpResponseRedirect('customers')),

    # Users
    path('register/', users_views.user_register_view, name='user_register'),
    path('login/', users_views.user_login_view, name='user_login'),
    path('logout/', users_views.user_logout_view, name='user_logout'),
    path('profile/', users_views.user_update_view, name='update_user'),
    path('profile/password', users_views.user_update_password_view, name='update_user_password'),

    # Customers
    path('customers', customers_views.index_customers_view, name='index_customers'),
    path('customers/create', customers_views.create_customer_view, name='create_customer'),
    path('customers/<int:customer_id>/update', customers_views.update_customer_view, name='update_customer'),
    path('customers/<int:customer_id>/show', customers_views.show_customer_view, name='show_customer'),
    path('customers/<int:customer_id>/delete', customers_views.delete_customer_view, name='delete_customer'),
    path('search/', customers_views.search_customer_view, name='search_customer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
