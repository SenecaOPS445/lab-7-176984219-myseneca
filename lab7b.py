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

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum_hour = t1.hour + t2.hour
    sum_minute = t1.minute + t2.minute
    sum_second = t1.second + t2.second
    
    if sum_second >= 60:
        sum_minute += sum_second // 60
        sum_second = sum_second % 60
    
    if sum_minute >= 60:
        sum_hour += sum_minute // 60
        sum_minute = sum_minute % 60
    
    sum_hour = sum_hour % 24

    return Time(sum_hour, sum_minute, sum_second)


def change_time(time, seconds):
    time.second += seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
    while time.hour >= 24:
        time.hour -= 24
    while time.hour < 0:
        time.hour += 24
    return None

def valid_time(t):
    """Check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

