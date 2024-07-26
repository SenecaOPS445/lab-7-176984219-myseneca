#!/usr/bin/env python3
# Student ID: osokunbi1

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add another time object (t2) to this time object and return the sum."""
        sum_hour = self.hour + t2.hour
        sum_minute = self.minute + t2.minute
        sum_second = self.second + t2.second

        if sum_second >= 60:
            sum_minute += sum_second // 60
            sum_second = sum_second % 60

        if sum_minute >= 60:
            sum_hour += sum_minute // 60
            sum_minute = sum_minute % 60

        sum_hour = sum_hour % 24

        return Time(sum_hour, sum_minute, sum_second)

    def change_time(self, seconds):
        self.second += seconds
        while self.second >= 60:
            self.second -= 60
            self.minute += 1
        while self.second < 0:
            self.second += 60
            self.minute -= 1
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        while self.hour >= 24:
            self.hour -= 24
        while self.hour < 0:
            self.hour += 24
        return None

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def valid_time(t):
    """Check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

