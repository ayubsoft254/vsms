from django.contrib import admin

# Register your models here.
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price', 'status')
    search_fields = ('make', 'model', 'VIN')
    list_filter = ('status', 'year', 'make')
    ordering = ('-year', 'make', 'model')
    fieldsets = (
        (None, {
            'fields': ('make', 'model', 'VIN', 'year', 'specs', 'price', 'mileage', 'color', 'photos', 'status')
        }),
    )
