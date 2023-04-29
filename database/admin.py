from django.contrib import admin
from django.db import models
from .models import Division, Category, College, PayingGuest
from django.forms import SelectMultiple


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('division',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'division', 'city', 'state',)
    list_filter = ('division',)
    search_fields = ('name',)


@admin.register(PayingGuest)
class PayingGuestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple},
    }
    list_display = (
        'name',
        'location',
        'type',
        'division',
        'city',
        'state',
        'category',
    )
    list_filter = ('division', 'category', 'college')
    raw_id_fields = ('college',)
    search_fields = ('name',)
