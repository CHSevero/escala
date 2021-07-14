from django.contrib import admin

from .models import Address, DayOf, Doctor, Place, Schedule


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'admission_date', 'active')

    def has_delete_permission(self, request, obj=None):
        return False


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1

    def has_delete_permission(self, request, obj=None):
        return False


class PlaceAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ('name', 'active')

    def has_delete_permission(self, request, obj=None):
        return False


class DayOfAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'doctor')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date', 'doctor', 'place',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(DayOf, DayOfAdmin)
admin.site.register(Schedule, ScheduleAdmin)
