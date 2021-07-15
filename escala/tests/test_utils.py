from datetime import date

from django.test import TestCase

from escala.models import Doctor, Place, Schedule
from escala.utils import generate_monday, generate_spreadsheet, generate_week


class utilsTests(TestCase):

    def test_generate_monday(self):
        """
        generate_monday() should returns the correct date.
        """
        date1 = date.fromisoformat('2021-07-15')
        response_monday = generate_monday(date1)
        monday = date.fromisoformat('2021-07-12')
        self.assertEqual(response_monday, monday)

    def test_generate_week(self):
        date1 = date.fromisoformat('2021-07-15')
        response_week = generate_week(date1)
        week = [
            {
                'date': date.fromisoformat('2021-07-12'),
                'weekday': 'seg'
            },
            {
                'date': date.fromisoformat('2021-07-13'),
                'weekday': 'ter'
            },
            {
                'date': date.fromisoformat('2021-07-14'),
                'weekday': 'qua'
            },
            {
                'date': date.fromisoformat('2021-07-15'),
                'weekday': 'qui'
            },
            {
                'date': date.fromisoformat('2021-07-16'),
                'weekday': 'sex'
            },
            {
                'date': date.fromisoformat('2021-07-17'),
                'weekday': 'sab'
            },
            {
                'date': date.fromisoformat('2021-07-18'),
                'weekday': 'dom'
            }
        ]

        self.assertEqual(response_week, week)

    def test_generate_spreadsheet(self):
        date1 = date.fromisoformat('2021-07-15')
        doctor1 = Doctor.objects.create(firstname='Antônio', lastname='antonio', active=True, admission_date=date1)
        place1 = Place.objects.create(name='Posto de trabalho 1', active=True)
        Schedule.objects.create(doctor=doctor1, place=place1, date=date1)

        response_place_list, response_week_schedule_list = generate_spreadsheet(date1)
        place_list = ['Posto de trabalho 1']
        week_schedule_list = [
            {'date': '2021-07-12', 'day': 'seg', 'schedule': ['']},
            {'date': '2021-07-13', 'day': 'ter', 'schedule': ['']},
            {'date': '2021-07-14', 'day': 'qua', 'schedule': ['']},
            {'date': '2021-07-15', 'day': 'qui', 'schedule': ['Antônio antonio']},
            {'date': '2021-07-16', 'day': 'sex', 'schedule': ['']},
            {'date': '2021-07-17', 'day': 'sab', 'schedule': ['']},
            {'date': '2021-07-18', 'day': 'dom', 'schedule': ['']}
        ]
        self.assertEqual(response_place_list, place_list)
        self.assertEqual(response_week_schedule_list, week_schedule_list)
