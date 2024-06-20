from django.contrib import admin
from website.models import Customer, Company

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ...