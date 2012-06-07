#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import calendar
import argparse
import sys

DISCORDIAN_SEASONS = ["Chaos", "Discord", "Confusion", "Bureaucracy",
    "The Aftermath"]

DISCORDIAN_WEEKDAYS = ["Sweetmorn", "Boomtime", "Pungenday", "Prickle-Prickle",
    "Setting Orange"]


def ddate(year, month, day):
    """
        stolen from otfbot (http://www.otfbot.org/)
    """
    today = datetime.date(year, month, day)
    is_leap_year = calendar.isleap(year)
    if is_leap_year and month == 2 and day == 29:
        return "St. Tib's Day, YOLD " + (year + 1166)

    day_of_year = today.timetuple().tm_yday - 1


    if is_leap_year and day_of_year >= 60:
        day_of_year -= 1  # Compensate for St. Tib's Day

    weekday = day_of_year % 5

    season, dday = divmod(day_of_year, 73)
    return "%s, %s %d, %d YOLD" \
        % (DISCORDIAN_WEEKDAYS[weekday],\
        DISCORDIAN_SEASONS[season], dday + 1, year + 1166)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int, nargs='?')
    parser.add_argument('month', type=int, nargs='?')
    parser.add_argument('year', type=int, nargs='?')
    args = parser.parse_args()

    if not(bool(args.day) == bool(args.month) == bool(args.year)):
        parser.error('too few arguments')

    if args.day:
        message = ddate(args.year, args.month, args.day)
    else:
        today = datetime.date(year, month, day)
        message = ddate(today.year, today.month, today.day)

    sys.stdout.write("%s\n" % message)

if __name__ == '__main__':
    main()
