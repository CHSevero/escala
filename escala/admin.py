from django.contrib import admin

from .models import Address, Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'admission_date', 'active')

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Address)
