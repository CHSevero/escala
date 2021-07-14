from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from escala.models import Address, DayOf, Doctor, Place, Schedule


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

    def setUp_clean(self):
        """
        Make the setUp for testing the clean() method.
        """
        doctor = Doctor.objects.create(
            firstname="João",
            lastname="Silva",
            admission_date=date.fromisoformat('2019-12-04'),
            active=True)
        place = Place.objects.create(name="Hospital", active=True)
        return doctor, place

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

    def test_clean_with_schedule(self):
        """
        clean() should return ValidationError
        """
        doctor, place = self.setUp_clean()
        Schedule.objects.create(
            date=date.fromisoformat('2021-07-13'),
            place=place,
            doctor=doctor
        )
        day_of = DayOf(day=3, doctor=doctor)
        with self.assertRaisesMessage(
            expected_exception=ValidationError,
            expected_message="O médico está escalado para trabalhar nesse dia da semana!"
        ):
            day_of.clean()

    def test_clean_without_schedule(self):
        """
        clean() should return None
        """
        doctor, place = self.setUp_clean()
        day_of = DayOf.objects.create(day=3, doctor=doctor)
        self.assertIsNone(day_of.clean())


class ScheduleModelsTests(TestCase):

    def setUp(self):
        self.doctor1 = Doctor.objects.create(
            firstname="Carlos",
            lastname="Severo",
            admission_date=timezone.now(),
            active=True)
        self.place1 = Place.objects.create(name="Hospital", active=True)

    def test__str__(self):
        schedule = Schedule(
            date=timezone.now().date(),
            place=self.place1,
            doctor=self.doctor1
        )

        self.assertEqual(str(schedule), f"Carlos Severo, Hospital, {timezone.now().date()}")

    def test_convert_weekday(self):
        schedule1 = Schedule(date=date.fromisoformat('2021-07-11'), place=self.place1, doctor=self.doctor1)
        schedule2 = Schedule(date=date.fromisoformat('2021-07-12'), place=self.place1, doctor=self.doctor1)
        schedule3 = Schedule(date=date.fromisoformat('2021-07-13'), place=self.place1, doctor=self.doctor1)
        schedule4 = Schedule(date=date.fromisoformat('2021-07-14'), place=self.place1, doctor=self.doctor1)
        schedule5 = Schedule(date=date.fromisoformat('2021-07-15'), place=self.place1, doctor=self.doctor1)
        schedule6 = Schedule(date=date.fromisoformat('2021-07-16'), place=self.place1, doctor=self.doctor1)
        schedule7 = Schedule(date=date.fromisoformat('2021-07-17'), place=self.place1, doctor=self.doctor1)

        self.assertEqual(schedule1.convert_weekday(), 1)
        self.assertEqual(schedule2.convert_weekday(), 2)
        self.assertEqual(schedule3.convert_weekday(), 3)
        self.assertEqual(schedule4.convert_weekday(), 4)
        self.assertEqual(schedule5.convert_weekday(), 5)
        self.assertEqual(schedule6.convert_weekday(), 6)
        self.assertEqual(schedule7.convert_weekday(), 7)

    def test_clean_with_day_of(self):
        """
        clean() should returns ValidationError
        """
        DayOf.objects.create(day=2, doctor=self.doctor1)
        scheduele = Schedule(
            date=date.fromisoformat('2021-07-12'),
            place=self.place1,
            doctor=self.doctor1)

        with self.assertRaisesMessage(
            expected_exception=ValidationError,
            expected_message="O médico tem folga nessa data. Por favor escolha outra data."
        ):
            scheduele.clean()

    def test_clean_without_day_of(self):
        """
        clean() should return None
        """
        scheduele = Schedule(
            date=date.fromisoformat('2021-07-17'),
            place=self.place1,
            doctor=self.doctor1)

        self.assertIsNone(scheduele.clean())

    def test_clean_with_no_active_doctor(self):
        """
        clean() should return ValidationError
        """
        doctor = Doctor.objects.create(
            firstname="Não",
            lastname="Ativo",
            admission_date=timezone.now(),
            active=False)

        place = Place.objects.create(name="Hospital", active=True)

        scheduele = Schedule(
            date=date.fromisoformat('2021-07-17'),
            place=place,
            doctor=doctor)

        with self.assertRaisesMessage(
            expected_exception=ValidationError,
            expected_message="Este médico não está ativo."
        ):
            scheduele.clean()

    def test_clean_with_no_active_place(self):
        """
        clean() should return ValidationError
        """
        doctor = Doctor.objects.create(
            firstname="Ativo",
            lastname="Ativo",
            admission_date=timezone.now(),
            active=True)

        place = Place.objects.create(name="Não ativo Hospital", active=False)

        scheduele = Schedule(
            date=date.fromisoformat('2021-07-17'),
            place=place,
            doctor=doctor)

        with self.assertRaisesMessage(
            expected_exception=ValidationError,
            expected_message="Este posto de trabalho não está ativo."
        ):
            scheduele.clean()
