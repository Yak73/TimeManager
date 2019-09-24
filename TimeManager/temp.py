from datetime import time


def str_to_time(strtime):
    temp_time = [int(i) for i in strtime.split(':')]
    return time(*temp_time)


def diff_times(start, end):
    diff_h = end.hour - start.hour
    diff_m = end.minute - start.minute
    if diff_m < 0:
        diff_h -= 1
        diff_m = 60 + diff_m
    diff_time = time(hour=diff_h, minute=diff_m)
    return diff_time


cur_time = str_to_time('12:12:30')
ar_time = str_to_time('10:30')
time_presence = minute_interval(ar_time, cur_time)
print(time_presence)

