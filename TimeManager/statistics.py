from TimeManager import download_data_from_database as from_db
from TimeManager import general_functions as gen_funcs
from datetime import timedelta

keys = ['arrival_time', 'departure_time', 'dinner', 'remotely',
            'time_absence_begin', 'time_absence_end', 'comment', 'id_non_appearance_reason']


def get_time_presence(cursor, cur_date):
    record = from_db.get_input_data(cursor, cur_date)
    time_presence = '00:00'
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
