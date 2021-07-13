from django.test import TestCase
from django.utils import timezone

from escala.models import Address, DayOf, Doctor, Place


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


class DayOfModelTests(TestCase):

    def setUp(self):
        doctor1 = Doctor(
            firstname="Carlos",
            lastname="Severo",
            admission_date=timezone.now(),
            active=True)
        self.day_of1 = DayOf(day=1, doctor=doctor1)
        self.day_of2 = DayOf(day=2, doctor=doctor1)
        self.day_of3 = DayOf(day=3, doctor=doctor1)
        self.day_of4 = DayOf(day=4, doctor=doctor1)
        self.day_of5 = DayOf(day=5, doctor=doctor1)
        self.day_of6 = DayOf(day=6, doctor=doctor1)
        self.day_of7 = DayOf(day=7, doctor=doctor1)

    def test_convert_weekday(self):
        self.assertEqual(self.day_of1.convert_weekday(), 'Domingo')
        self.assertEqual(self.day_of2.convert_weekday(), 'Segunda')
        self.assertEqual(self.day_of3.convert_weekday(), 'Terça')
        self.assertEqual(self.day_of4.convert_weekday(), 'Quarta')
        self.assertEqual(self.day_of5.convert_weekday(), 'Quinta')
        self.assertEqual(self.day_of6.convert_weekday(), 'Sexta')
        self.assertEqual(self.day_of7.convert_weekday(), 'Sábado')

    def test__str__(self):
        self.assertEqual(str(self.day_of1), 'Domingo')
