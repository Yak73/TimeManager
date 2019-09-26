from TimeManager import download_data_from_database as from_db
from TimeManager import general_functions as gen_funcs
from datetime import time, datetime, date, timedelta

#   keys = ['arrival_time', 'departure_time', 'dinner', 'remotely',
#            'time_absence_begin', 'time_absence_end', 'comment', 'id_non_appearance_reason']


def get_stat_for_all_periods(cursor, cur_date):
    keys = ['d_time_presence', 'd_time_delta', 'd_flag_conversion',
            'w_time_presence', 'w_time_delta', 'w_flag_conversion',
            'w_production_percent', 'w_avg_arrival_time', 'w_avg_departure_time',
            'm_time_presence', 'm_time_delta', 'm_flag_conversion']
    stat_dict = {}

    day_stat = get_stat_for_period(cursor, type_interval='d', date_interval=cur_date)

    week_interval = gen_funcs.boundaries_work_week(cur_date)
    week_interval_dates = tuple([gen_funcs.date_to_str(date_) for date_ in week_interval])
    week_stat = get_stat_for_period(cursor, type_interval='w', date_interval=week_interval_dates)

    m_interval = gen_funcs.boundaries_work_month(cur_date)
    m_interval_dates = tuple([gen_funcs.date_to_str(date_) for date_ in m_interval])
    month_stat = get_stat_for_period(cursor, type_interval='m', date_interval=m_interval_dates)

    if not day_stat or not week_stat or not month_stat:
        return

    for key, value in zip(keys[:3], day_stat):
        stat_dict[key] = value

    for key, value in zip(keys[3:9], week_stat):
        stat_dict[key] = value

    for key, value in zip(keys[9:], month_stat):
        stat_dict[key] = value

    return stat_dict


def get_stat_for_period(cursor, type_interval, date_interval):
    # TODO: учитывать праздник и сокращенные дни
    duration_workday_int = 8
    duration_dinner_int = 1

    records = from_db.get_input_data(cursor, type_interval, date_interval)
    if not records:
        return

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

    time_presence = timedelta(seconds=sum_time_presence_fact)
    time_delta = sum_time_presence_fact - sum_time_reg
    flag_conversion = False if time_delta < 0 else True
    time_delta = abs(timedelta(seconds=time_delta))
    # TODO: сменить время присутствия (сумм)

    if type_interval == 'w':
        # TODO: считать регламент всю недели, а не где есть строчки
        production_percent = int(100 * round(sum_time_presence_fact / sum_time_reg, 2))
        avg_arrival_time, avg_departure_time = from_db.get_avg_times(cursor, type_interval, date_interval)
        return time_presence, time_delta, flag_conversion, production_percent, avg_arrival_time, avg_departure_time

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
