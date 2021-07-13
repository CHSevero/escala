from django.contrib import admin

from .models import Address, Doctor, Place


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
    list_display = ('name',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Place, PlaceAdmin)
