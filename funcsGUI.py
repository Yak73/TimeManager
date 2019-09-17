from PyQt5 import QtWidgets, QtGui
import design
import pyodbc
from datetime import datetime, time
import inspect


SERVER = 'LIT-SQLSRV-01\LESTER14'
DATABASE = 'Tracker'


class TimeManagerApp(QtWidgets.QMainWindow, design.Ui_TimeManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Менеджер времени")
        self.setWindowIcon(QtGui.QIcon('icon2.png'))
        self.set_init_state()

    def set_init_state(self):
        # Read data from database
        connect = self.connect_to_database()
        with connect:
            with connect.cursor() as crs:
                self.update_fields(crs)  # all refresh

        # bind buttons
        self.b_cur_time_arr.clicked.connect(self.set_cur_arr_time)
        self.b_cur_time_dep.clicked.connect(self.set_cur_dep_time)
        self.b_apply.clicked.connect(self.save_changes)
        self.b_clear.clicked.connect(self.clear_fields)
        self.cal_calendar.selectionChanged.connect(self.change_output_by_date)

    # Set current time as arrival time
    def set_cur_arr_time(self):
        self.te_time_arr.setTime(GetValuesFromDatabase.get_cur_time())

    # Set current time as departure time
    def set_cur_dep_time(self):
        self.te_time_dep.setTime(GetValuesFromDatabase.get_cur_time())

    # Save data from input widgets to database and update statistics
    def save_changes(self):
        fields = dict()
        fields['tracked_date'] = self.cal_calendar.selectedDate().toString("yyyy-MM-dd")
        fields['arrival_time'] = self.te_time_arr.time().toString("hh-mm")
        fields['departure_time'] = self.te_time_dep.time().toString("hh-mm")
        fields['dinner'] = self.chb_dinner.isChecked()
        fields['remotely'] = self.chb_remotely.isChecked()
        fields['time_absense_begin'] = self.te_time_absense_start.time().toString("hh-mm")
        fields['time_absense_end'] = self.te_time_absense_stop.time().toString("hh-mm")
        fields['comment'] = self.te_comment.toPlainText()
        fields['non_appearance_reason'] = self.cb_reason.currentText()

        connect = self.connect_to_database()
        with connect:
            with connect.cursor() as crs:
                self.save_to_database(crs, fields)
                self.update_fields(crs, upd_init_f=False, upd_input_f=False, upd_output_f=True)

    # Set default value for all input fields
    def clear_fields(self):
        zero_time = time()
        self.te_time_arr.setTime(zero_time)
        self.te_time_dep.setTime(zero_time)
        self.te_time_absense_start.setTime(zero_time)
        self.te_time_absense_stop.setTime(zero_time)
        self.te_comment.setText('')
        self.chb_dinner.setChecked(True)
        self.chb_remotely.setChecked(False)
        self.gb_additional_param.setChecked(False)

    # Update data in fields, when date was changed
    def change_output_by_date(self):
        connect = self.connect_to_database()
        with connect:
            with connect.cursor() as crs:
                self.update_fields(crs, upd_init_f=False, upd_input_f=True, upd_output_f=True)

    # Set data in fields GUI from database
    def update_fields(self, cursor, upd_init_f=True, upd_input_f=True, upd_output_f=True):
        try:
            if upd_init_f:
                self.tb_user.setText(GetValuesFromDatabase.get_cur_user(cursor, slice_flag=True))
                self.cb_reason.addItems(GetValuesFromDatabase.get_reasons(cursor))

            if upd_input_f:
                date = self.cal_calendar.selectedDate().toString("yyyy-MM-dd")
                print(date)
                input_data = GetValuesFromDatabase.get_input_data(cursor, date)
                # if exist record with the date
                if input_data:
                    if input_data['arrival_time']:
                        self.te_time_arr.setTime(str_to_time(input_data['arrival_time']))
                    if input_data['departure_time']:
                        self.te_time_dep.setTime(str_to_time(input_data['departure_time']))
                    if input_data['dinner']:
                        self.chb_dinner.setChecked(input_data['dinner'])
                    if input_data['remotely']:
                        self.chb_dinner.setChecked(input_data['remotely'])
                    if input_data['time_absence_begin']:
                        self.te_time_absense_start.setTime(str_to_time(input_data['time_absence_begin']))
                    if input_data['time_absence_end']:
                        self.te_time_absense_stop.setTime(str_to_time(input_data['time_absence_end']))
                    if input_data['comment']:
                        self.te_comment.setText(input_data['comment'])
                    if input_data['reason']:
                        index = self.cb_reason.findText(input_data['reason'])
                        if index == -1:  # if this reason not exist, set reason '' (index=0)
                            index = 0
                        self.cb_reason.setItemData(index)

                else:
                    self.clear_fields()

            if upd_output_f:
                pass

        except Exception as e:
            self.show_error(e)

    # Save data to database
    def save_to_database(self, cursor, data_dict):
        # TODO Сделать сохранение данных в БД (мб вынести/статик)
        return
        cursor.execute("""SELECT tracked_date FROM TimeLog WHERE username = SUSER_SNAME()""")
        if cursor.rowcount == 0:  # then INSERT
            cursor.execute("""INSERT INTO""")
        else:  # then UPDATE
            tracked_date = cursor.fetchone()

        """
        data_dict['tracked_date']
        data_dict['arrival_time']
        data_dict['departure_time']
        data_dict['dinner']
        data_dict['remotely']
        data_dict['time_absense_begin'] 
        data_dict['time_absense_end'] 
        data_dict['comment'] 
        data_dict['non_appearance_reason'] 
        """

    def connect_to_database(self):
        try:
            connect = pyodbc.connect("Driver={SQL Server};"
                                     "Server=" + SERVER + ";"
                                     "Database=" + DATABASE + ";"
                                     "Trusted_Connection=yes;")
            return connect
        except Exception as e:
            self.show_error(err=e)

    def show_error(self, err, additional_text='', parent=None):
        if not parent:
            parent = self
        func = inspect.stack()[1][3]  # name of func, in which an error occurred
        prev_func = inspect.stack()[2][3]  # name of func, which called the function, in which an error occurred
        title = "Ошибка"
        msg = "Функция: {} \nРодительская функция: {} \nОшибка: {} : {} \n{}"\
            .format(func, prev_func, type(err).__name__, err, additional_text)
        QtWidgets.QMessageBox.critical(parent, title, msg)
        exit(-1)


class GetValuesFromDatabase:
    # 'Static' class for union methods, which read the data from database

    # Get name of current user
    @staticmethod
    def get_cur_user(cursor, slice_flag=False):
        cursor.execute('SELECT suser_sname()')
        name = str(cursor.fetchone())
        if 'LESTER' in name and slice_flag:
            name = name[10:-4]
        return name

    # Get all kinds of NonAppearanceReasons from database
    @staticmethod
    def get_reasons(cursor):
        cursor.execute('SELECT name FROM NonAppearanceReasons')
        reasons = [str(row)[2:-4] for row in cursor.fetchall()]
        reasons.insert(0, '')
        return reasons

    # Get current time
    @staticmethod
    def get_cur_time():
        return datetime.now().time()

    @staticmethod
    def get_input_data(cursor, date):
        date = "\'{}\'".format(date)
        keys = ['arrival_time', 'departure_time', 'dinner', 'remotely',
                'time_absence_begin', 'time_absence_end', 'comment', 'id_non_appearance_reason']
        select_string = ", ".join(keys)
        cursor.execute("""SELECT {select_str}
                        FROM 
                            TimeLog AS tl
                        WHERE 
                            tl.username = SUSER_SNAME() 
                            AND tl.tracked_date = {cur_date}
                        """.format(select_str=select_string, cur_date=date))

        input_data = dict()

        # if not exist record with the date
        if cursor.rowcount == 0:
            return input_data

        row = list(cursor.fetchone())
        for value, key in zip(row, keys):
            input_data[key] = value
        input_data['reason'] = None

        # if not exist reason (on field: TimeLog.id_non_appearance_reason)
        if not input_data['id_non_appearance_reason']:
            return input_data
        else:
            cursor.execute("""SELECT name FROM NonAppearanceReasons WHERE id_non_appearance_reason = {id_reason}
                                        """.format(id_reason=input_data['id_non_appearance_reason']))

        # if not exist reason (on field: NonAppearanceReasons.name)
        if cursor.rowcount == 0:
            return input_data
        else:
            input_data['reason'] = str(cursor.fetchone())

        return input_data


def str_to_time(strtime):
    temp_time = [int(i) for i in strtime.split(':')]
    return time(*temp_time)

# TODO: Добавить расчет статистики

