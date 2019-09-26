from datetime import datetime, time, timedelta
from PyQt5 import QtWidgets
import inspect
import pyodbc
import calendar

SERVER = r'LIT-SQLSRV-01\LESTER14'
DATABASE = 'Tracker'


# Creating a database connection
def connect_to_database():
    try:
        connect = pyodbc.connect("Driver={SQL Server};"
                                 "Server=" + SERVER + ";"
                                                      "Database=" + DATABASE + ";"
                                                                               "Trusted_Connection=yes;")
        return connect
    except Exception as e:
        show_error(err=e)


# Error output mechanism
def show_error(err, additional_text='', parent=None):
    func = inspect.stack()[1][3]  # name of func, in which an error occurred
    prev_func = inspect.stack()[2][3]  # name of func, which called the function, in which an error occurred
    title = "Ошибка"
    msg = "Функция: {} \nРодительская функция: {} \nОшибка: {} : {} \n{}" \
        .format(func, prev_func, type(err).__name__, err, additional_text)
    QtWidgets.QMessageBox.critical(parent, title, msg)
    exit(-1)  # TODO: убрать при релизе


# Convert str to time
def str_to_time(strtime):
    temp_time = [int(i) for i in strtime.split(':')]
    return time(*temp_time)


# Change separator in string: - -> :
def change_sep(strtime):
    return strtime.replace('-', ':')


# Get current time
def get_cur_time():
    return datetime.now().time()


# Add ' '
def add_q(string):
    return '\'' + string + '\''


# Return difference time: end - start.
def diff_times(start, end):
    if start > end:
        end, start = start, end
    diff_h = end.hour - start.hour
    diff_m = end.minute - start.minute
    if diff_m < 0:
        diff_h -= 1
        diff_m += 60
    diff_time = time(hour=diff_h, minute=diff_m)
    return diff_time


def day_name_by_date(date_):
    # date_ = 2019-09-24
    work_date = datetime.strptime(date_, "%Y-%m-%d")
    days_dict = {
        'Mon': 'Понедельник',
        'Tue': 'Вторник',
        'Wed': 'Среда',
        'Thu': 'Четверг',
        'Fri': 'Пятница',
        'Sat': 'Суббота',
        'Sun': 'Воскресенье'
    }
    number_day = work_date.date().weekday() + 1
    name_day = days_dict[calendar.day_abbr[work_date.date().weekday()]]
    return number_day, name_day


def boundaries_work_week(date_):
    number_day, _ = day_name_by_date(date_)
    work_date = datetime.strptime(date_, "%Y-%m-%d")
    start_week = work_date + timedelta(days=(1 - number_day))
    end_week = work_date + timedelta(days=(5 - number_day))
    return start_week, end_week


def boundaries_work_month(date_):
    work_date = datetime.strptime(date_, "%Y-%m-%d")
    number_day = work_date.day
    max_days_in_month = calendar.monthrange(work_date.year, work_date.month)[1]
    start_month = work_date + timedelta(days=(1 - number_day))
    end_month = work_date + timedelta(days=(max_days_in_month - number_day))
    return start_month, end_month
