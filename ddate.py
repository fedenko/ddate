import datetime, calendar

DISCORDIAN_SEASONS = ["Chaos", "Discord", "Confusion", "Bureaucracy",
    "The Aftermath"]

DISCORDIAN_WEEKDAYS=["Sweetmorn", "Boomtime", "Pungenday", "Prickle-Prickle",
    "Setting Orange"]

def ddate(year, month, day):
    today = datetime.date(year, month, day)
    is_leap_year = calendar.isleap(year)
    if is_leap_year and month == 2 and day == 29:
        return "St. Tib's Day, YOLD " + (year + 1166)
  
    day_of_year = today.timetuple().tm_yday - 1
  
    weekday=day_of_year % 5
    if is_leap_year and day_of_year >= 60:
        day_of_year -= 1 # Compensate for St. Tib's Day
  
    season, dday = divmod(day_of_year, 73)
    return "Today is %s, the %d day of %s in the YOLD %d" \
        % (DISCORDIAN_WEEKDAYS[weekday], dday + 1, \
        DISCORDIAN_SEASONS[season], year + 1166)


today = datetime.date.today()
print ddate(today.year, today.month, today.day)
