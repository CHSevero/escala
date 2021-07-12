from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from escala.admin import DoctorAdmin
from escala.models import Doctor


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
