from TimeManager import download_data_from_database as from_db
from TimeManager import general_functions as gen_funcs
from datetime import time

#   keys = ['arrival_time', 'departure_time', 'dinner', 'remotely',
#            'time_absence_begin', 'time_absence_end', 'comment', 'id_non_appearance_reason']


def get_day_info(cursor, cur_date):
    record = from_db.get_input_data(cursor, cur_date)
    time_presence = get_time_presence(record)
    time_delta, flag_conversion = get_time_delta(time_presence)
    return time_presence, time_delta, flag_conversion


def get_time_presence(record):
    # TODO: добавить обработку временного отсутствия
    time_presence = time()
    dinner = False
    if record:
        ar_time = gen_funcs.str_to_time(record['arrival_time'])
        if record['departure_time']:
            end_time = gen_funcs.str_to_time(record['departure_time'])
        else:
            end_time = gen_funcs.get_cur_time()
        if record['dinner']:
            dinner = True
        time_presence = gen_funcs.diff_times(ar_time, end_time, dinner=dinner)
    return time_presence


def get_time_delta(time_presence):
    time_delta = time()
    flag_conversion = True
    if time_presence != time():
        duration_workday = time(hour=8)
        time_delta = gen_funcs.diff_times(time_presence, duration_workday)
        if duration_workday > time_presence:
            flag_conversion = False
    return time_delta, flag_conversion
