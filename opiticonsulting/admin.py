from django.contrib import admin
from .models import Demo, Service, Contact

# Register your models here.

@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
	list_display = ('title','link')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('title','link')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','country','title')
    search_fields = ['name','title']