from django.test import TestCase
from django.utils import timezone

from escala.models import Address, Doctor, Place


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
        Overridden __str__() returns the right string.
        """
        doctor = self.doctor1
        self.assertEqual(str(doctor), "Carlos Severo")


class AddressModelTests(TestCase):

    def setUp(self):
        self.place1 = Place(name="Hospital", active=True)
        self.addres1 = Address(
            country="Brasil",
            state="São Paulo",
            city="São Paulo",
            district="ABC",
            street="São Bento",
            number="25",
            place=self.place1
        )

    def test__str__(self):
        """
        Overridden __str__() returns the right string.
        """
        address = self.addres1
        self.assertEqual(
            str(address),
            "São Bento, 25, ABC, São Paulo, São Paulo, Brasil")


class PlaceModelTest(TestCase):

    def setUp(self):
        self.place1 = Place(name="Hospital", active=True)

    def test__str__(self):
        """
        Overridden __str__() returns the right string.
        """
        place = self.place1
        self.assertEqual(str(place), "Hospital")
