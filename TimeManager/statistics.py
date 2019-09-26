from TimeManager import download_data_from_database as from_db
from TimeManager import general_functions as gen_funcs
from datetime import time, datetime, date, timedelta

#   keys = ['arrival_time', 'departure_time', 'dinner', 'remotely',
#            'time_absence_begin', 'time_absence_end', 'comment', 'id_non_appearance_reason']


def get_stat_for_all_periods(cursor, cur_date):
    # TODO: изменить переменные и вовзращаемое значение
    a, b, c = get_stat_for_period(cursor, type_interval='d', date_interval=cur_date)

    week_interval = gen_funcs.boundaries_work_week(cur_date)
    week_interval_dates = tuple([gen_funcs.date_to_str(date_) for date_ in week_interval])
    d, e, f, g = get_stat_for_period(cursor, type_interval='w', date_interval=week_interval_dates)

    m_interval = gen_funcs.boundaries_work_month(cur_date)
    m_interval_dates = tuple([gen_funcs.date_to_str(date_) for date_ in m_interval])
    y, u, i, o = get_stat_for_period(cursor, type_interval='w', date_interval=m_interval_dates)

    return c, g, o


def get_stat_for_period(cursor, type_interval, date_interval):
    # TODO: учитывать праздник и сокращенные дни
    duration_workday_int = 8
    duration_dinner_int = 1

    records = from_db.get_input_data(cursor, type_interval, date_interval)

    # if day
    if type_interval == 'd':
        time_presence = get_time_presence(records[0])
        time_delta, flag_conversion = get_time_delta(time_presence, records[0]['dinner'])
        return time_presence, time_delta, flag_conversion

    # if week or month
    sum_time_presence_fact = 0
    sum_time_reg = 0

    for record in records:
        time_presence = get_time_presence(record)
        # time -> seconds
        sum_time_presence_fact += (time_presence.hour * 60 + time_presence.minute) * 60 + time_presence.second

        if record['dinner']:
            t = time(hour=duration_workday_int + duration_dinner_int)
        else:
            t = time(hour=duration_workday_int)
        sum_time_reg += (t.hour * 60 + t.minute) * 60 + t.second

    time_presence = sum_time_presence_fact
    time_delta = sum_time_presence_fact - sum_time_reg
    flag_conversion = False if time_delta < 0 else True
    # TODO: считать регламент всю недели, а не где есть строчки
    production_percent = 100 * round(sum_time_presence_fact / sum_time_reg, 2)

    return time_presence, time_delta, flag_conversion, production_percent


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
    duration_workday_int = 8
    duration_dinner_int = 1
    flag_conversion = True
    if dinner:
        duration_workday_int += duration_dinner_int
    if time_presence != time():
        duration_workday = time(hour=duration_workday_int)
        time_delta = gen_funcs.diff_times(time_presence, duration_workday)
        if duration_workday > time_presence:
            flag_conversion = False
    return time_delta, flag_conversion
