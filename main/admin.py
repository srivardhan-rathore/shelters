from django.contrib import admin

from .models import AirportTaxiService, AccommodationService, HotelService


@admin.register(AirportTaxiService)
class AirportTaxiServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'journey_type',
        'car_type',
        'travel_date',
        'travel_time',
        'status',
        'address',
        'order_id',
        'checked',
        'created_at',
    )
    list_filter = ('client', 'travel_date', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(AccommodationService)
class AccommodationServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'accommodation_type',
        'occupancy',
        'move_in_date',
        'gender',
        'address',
        'order_id',
        'checked',
        'created_at',
    )
    list_filter = ('client', 'move_in_date', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(HotelService)
class HotelServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'budget',
        'room',
        'people',
        'check_in_date',
        'check_out_date',
        'address',
        'order_id',
        'date',
        'checked',
        'created_at',
    )
    list_filter = ('client', 'check_in_date', 'check_out_date', 'created_at')
    date_hierarchy = 'created_at'
