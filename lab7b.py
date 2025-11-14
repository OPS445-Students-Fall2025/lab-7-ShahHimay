#!/usr/bin/env python3
# Student ID: 118541234

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    total = Time(0, 0, 0)
    total.hour = t1.hour + t2.hour
    total.minute = t1.minute + t2.minute
    total.second = t1.second + t2.second

    # Same carry logic as lab7a
    while total.second >= 60:
        total.second -= 60
        total.minute += 1

    while total.minute >= 60:
        total.minute -= 60
        total.hour += 1

    return total


def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True


def change_time(time, seconds):
    """
    Modifier: change the given time object by the number of seconds.

    This function *modifies* the existing time object instead of returning a new one.
    It works for both positive and negative values of 'seconds'.
    """
    # First dump all the extra seconds straight into the second field
    time.second += seconds

    if valid_time(time) is not True:
        # If seconds are 60 or more push the extra into minutes
        while time.second >= 60:
            time.second -= 60
            time.minute += 1

        # If seconds are negative borrow minutes until seconds are back to 0–59
        while time.second < 0:
            time.second += 60
            time.minute -= 1

        # If minutes are 60 or more push the extra into hours
        while time.minute >= 60:
            time.minute -= 60
            time.hour += 1

        # If minutes are negative borrow from hours until minutes are 0–59
        while time.minute < 0:
            time.minute += 60
            time.hour -= 1

    return None
