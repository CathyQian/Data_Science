from datetime import date, timedelta

class MeetupException(Exception):
    pass

def meetup_day(year, month, day_of_the_week, which):
    # day_of_the_week: Monday to Sunday
    # which: 1st, 2nd, 3rd, 4th, 5th, last, teenth
    # return example: date(2012, 12, 7)
    # test, I'm quite confused with the problem description
    weekdays = {'Monday': 1, 'Tuesday': 2,'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    meetup_date = date(year, month, 1)

    if meetup_date.isoweekday() < weekdays[day_of_the_week]:
        meetup_date += timedelta(days = weekdays[day_of_the_week] - meetup_date.isoweekday())
        
