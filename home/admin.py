from django.contrib import admin

from .models import Contacts, Testimonials, Partners, ServiceInfo


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'mobile',
        'email',
        'message',
        'checked',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating', 'message', 'image', 'occupation')
    search_fields = ('name',)


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)


@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'happy_clients',
        'hard_worker',
        'tie_ups',
        'support',
    )
