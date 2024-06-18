from django.contrib import admin
from website.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...