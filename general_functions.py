from datetime import datetime, time
from PyQt5 import QtWidgets
import inspect


# Error output mechanism
def show_error(err, additional_text='', parent=None):
    func = inspect.stack()[1][3]  # name of func, in which an error occurred
    prev_func = inspect.stack()[2][3]  # name of func, which called the function, in which an error occurred
    title = "Ошибка"
    msg = "Функция: {} \nРодительская функция: {} \nОшибка: {} : {} \n{}" \
        .format(func, prev_func, type(err).__name__, err, additional_text)
    QtWidgets.QMessageBox.critical(parent, title, msg)
    exit(-1)


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
