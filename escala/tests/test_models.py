from django.test import TestCase
from django.utils import timezone

from escala.models import Doctor


class DoctorModelTests(TestCase):

    def setUp(self):
        """
        Set up data for the tests.
        """
        self.doctor1 = Doctor(
            firstname="Carlos",
            lastname="Severo",
            admission_date=timezone.now(),
            active=True)

    def test__str__return(self):
        """
        __str__() returns the right string.
        """
        doctor = self.doctor1
        self.assertEqual(str(doctor), "Carlos Severo")
