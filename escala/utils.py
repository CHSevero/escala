from datetime import timedelta

from .models import Place, Schedule


def generate_spreadsheet(date_to_generate):
    places = Place.objects.filter(active=True).order_by('name')
    place_list = list()
    for place in places:
        place_list.append(str(place))
    week = generate_week(date_to_generate)
    week_schedule_list = list()
    for day in week:
        day_schedule = list()
        for place in places:
            day_place_schedule = Schedule.objects.filter(date=day['date'], place=place)
            if day_place_schedule.exists():
                day_place_schedule_list = list(day_place_schedule)
                day_schedule.append(str(day_place_schedule_list[0]).split(',')[0])
            else:
                day_schedule.append('')

        week_schedule_list.append({
            'date': str(day['date']),
            'day': day['weekday'],
            'schedule': day_schedule
        })

    return place_list, week_schedule_list


def generate_monday(week_date):
    """
    Receive a date and returns the Monday's date of the week that date belongs to.
    """
    week_day = week_date.weekday()
    monday = week_date - timedelta(days=week_day)
    return monday


def generate_week(week_date):
    """
    Receive a date and returns a list with all dates from thate date's week.
    """
    monday = generate_monday(week_date)
    week = list()
    week_day = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
    for i in range(7):
        week.append(
            {
                'date': monday + timedelta(i),
                'weekday': week_day[i]
            })
    return week
