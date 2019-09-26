from TimeManager import download_data_from_database as from_db
from TimeManager import general_functions as gen_funcs
from datetime import time

#   keys = ['arrival_time', 'departure_time', 'dinner', 'remotely',
#            'time_absence_begin', 'time_absence_end', 'comment', 'id_non_appearance_reason']


def get_day_info(cursor, cur_date, record):
    if not record:  # if haven`t data from database
        record = from_db.get_input_data(cursor, cur_date)

    time_presence = get_time_presence(record)
    time_delta, flag_conversion = get_time_delta(time_presence, record['dinner'])

    return time_presence, time_delta, flag_conversion


def get_time_presence(record):
    time_absence_presence = time()
    res_time_presence = time()
    if record:
        ar_time = gen_funcs.str_to_time(record['arrival_time'])
        if record['departure_time']:
            dep_time = gen_funcs.str_to_time(record['departure_time'])
        else:
            dep_time = gen_funcs.get_cur_time()
        if record['time_absence_begin'] and record['time_absence_end']:
            time_absence_begin = gen_funcs.str_to_time(record['time_absence_begin'])
            time_absence_end = gen_funcs.str_to_time(record['time_absence_end'])
            time_absence_presence = gen_funcs.diff_times(time_absence_begin, time_absence_end)

        time_presence = gen_funcs.diff_times(ar_time, dep_time)

        if time_absence_presence != time():
            res_time_presence = gen_funcs.diff_times(time_absence_presence, time_presence)
        else:
            res_time_presence = time_presence

    return res_time_presence


def get_time_delta(time_presence, dinner):
    # TODO: добавить обработку праздничных и сокращенных дней
    time_delta = time()
    flag_conversion = True
    duration_workday_int = 8
    if dinner:
        duration_workday_int += 1
    if time_presence != time():
        duration_workday = time(hour=duration_workday_int)
        time_delta = gen_funcs.diff_times(time_presence, duration_workday)
        if duration_workday > time_presence:
            flag_conversion = False
    return time_delta, flag_conversion
