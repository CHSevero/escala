from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from escala.admin import AddressInline, DoctorAdmin, PlaceAdmin
from escala.models import Address, Doctor, Place


class DoctorAdminTests(TestCase):

    def setUp(self):
        self.doctor_admin1 = DoctorAdmin(model=Doctor, admin_site=AdminSite())

    def test_has_delete_permission(self):
        """
        has_delete_permission should return False.
        """
        doctor_admin = self.doctor_admin1
        self.assertFalse(
            doctor_admin.has_delete_permission(
                request=None,
                obj=Doctor()))


class PlaceAdminTests(TestCase):

    def setUp(self):
        self.place_admin1 = PlaceAdmin(model=Place, admin_site=AdminSite())

    def test_has_delete_permission(self):
        """
        has_delete_permission should return False.
        """
        place_admin = self.place_admin1
        self.assertFalse(
            place_admin.has_delete_permission(
                request=None,
                obj=Place()
            )
        )


class AddressInlineTests(TestCase):

    def setUp(self):
        self.address_inline = AddressInline(parent_model=Address, admin_site=AdminSite())

    def test_has_delete_permission(self):
        """
        has_delete_permission should return False.
        """
        address_inline = self.address_inline
        self.assertFalse(
            address_inline.has_delete_permission(
                request=None,
                obj=Address()
            )
        )
