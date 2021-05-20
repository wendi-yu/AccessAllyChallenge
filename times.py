import bisect
import os
import sys


def generate_times():
    """Generate a list (in order) of times that are arithmetic sequences"""
    hours = [i for i in range(13)]

    ranges = [i for i in range(5)]
    arithmetic_hours = set()

    for hour in hours:
        for diff in ranges:
            if check_bounds(hour, diff):
                m1, m2 = build_minutes(hour, diff)
                arithmetic_hours.add(rep(hour, m1, m2))
            if diff != 0 and check_bounds(hour, -diff):
                m1, m2 = build_minutes(hour, -diff)
                arithmetic_hours.add(rep(hour, m1, m2))

    return sorted(list(arithmetic_hours))


def build_minutes(hour, diff):
    """Build the miniute arithmetic sequence"""
    m1 = hour % 10 + diff
    m2 = m1 + diff

    return m1, m2


def check_bounds(hour, diff):
    """Check a sequence to make sure it's arithmetic and represents a valid time"""
    minute_1, minute_2 = build_minutes(hour, diff)

    if hour < 1 or hour > 12:
        return False

    if minute_1 < 0 or minute_1 > 5:
        return False

    if minute_2 < 0 or minute_2 > 9:
        return False

    # check that the arithmetic sequence holds for the hour
    h1 = hour // 10
    h2 = hour % 10
    if h1 != 0 and h2 - h1 != diff:
        return False

    return True


def rep(hour, m1, m2):
    """Create integer representation of a time"""
    # % 12 to show as 0 to help with sorting
    str_rep = str(hour % 12) + str(m1) + str(m2)

    return int(str_rep)


def find_times(total_minutes):
    """Find number of arithmetic times seen in total_minutes"""
    # full cycles watched - 720 minutes in a 12 hour period
    cycles = total_minutes // 720
    # leftover minutes
    minutes = total_minutes % 720

    display_minutes = minutes % 60
    display_hours = minutes // 60
    if display_hours == 0:
        display_hours = 12

    display_time = rep(display_hours, display_minutes // 10, display_minutes % 10)

    arithmetic_times = generate_times()
    times_per_cycle = len(arithmetic_times)

    idx = bisect.bisect(arithmetic_times, display_time)

    return cycles*times_per_cycle + idx


fname = sys.argv[1]
with open(fname) as f:
    total_minutes  = int(f.read())
    print(find_times(total_minutes))
