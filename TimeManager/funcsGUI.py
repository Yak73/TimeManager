from PyQt5 import QtWidgets, QtGui
from datetime import time

from TimeManager import design
from TimeManager import general_functions as gen_funcs
from TimeManager import download_data_from_database as from_db
from TimeManager import upload_data_to_database as to_db
from TimeManager import statistics as stat


class TimeManagerApp(QtWidgets.QMainWindow, design.Ui_TimeManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Менеджер времени")
        self.setWindowIcon(QtGui.QIcon('icon2.png'))
        self.set_init_state()

    def set_init_state(self):
        # Read data from database
        connect = gen_funcs.connect_to_database()
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
        self.te_time_arr.setTime(gen_funcs.get_cur_time())

    # Set current time as departure time
    def set_cur_dep_time(self):
        self.te_time_dep.setTime(gen_funcs.get_cur_time())

    # Save data from input widgets to database and update statistics
    def save_changes(self):
        # TODO: добавить проверку сохраняемых данных (защита от дурака)
        fields = dict()
        fields['tracked_date'] = self.cal_calendar.selectedDate().toString("yyyy-MM-dd")
        fields['arrival_time'] = self.te_time_arr.time().toString("hh-mm")
        fields['departure_time'] = self.te_time_dep.time().toString("hh-mm")
        fields['dinner'] = self.chb_dinner.isChecked()
        fields['remotely'] = self.chb_remotely.isChecked()
        fields['time_absence_begin'] = self.te_time_absense_start.time().toString("hh-mm")
        fields['time_absence_end'] = self.te_time_absense_stop.time().toString("hh-mm")
        fields['comment'] = self.te_comment.toPlainText()
        fields['non_appearance_reason'] = self.cb_reason.currentText()

        connect = gen_funcs.connect_to_database()
        with connect:
            with connect.cursor() as crs:
                to_db.save_to_database(crs, fields)
                self.update_fields(crs, upd_init_f=False, upd_input_f=True, upd_output_f=True)

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
        self.cb_reason.setCurrentText("")
        self.tb_time_presence.setText("")

        self.tb_time_presence.setText('')
        self.tb_difference.setText('')
        self.tb_time_presence_sum.setText('')
        self.tb_difference_sum_week.setText('')
        self.lcd_production.display(str(0))
        self.tb_time_arr_avg.setText('')
        self.tb_time_dep_avg.setText('')
        self.tb_difference_sum_month.setText('')
        self.tb_difference_sum_week.setStyleSheet("background-color: white; font-size: 12pt;")
        self.tb_difference.setStyleSheet("background-color: white; font-size: 12pt;")
        self.tb_difference_sum_month.setStyleSheet("background-color: white; font-size: 12pt;")

    # Update data in fields, when date was changed
    def change_output_by_date(self):
        connect = gen_funcs.connect_to_database()
        with connect:
            with connect.cursor() as crs:
                self.update_fields(crs, upd_init_f=False, upd_input_f=True, upd_output_f=True)

    # Set data in fields GUI from database
    def update_fields(self, cursor, upd_init_f=True, upd_input_f=True, upd_output_f=True):
        try:
            # TODO: функция update_input должна возвращать результ запроса
            #  и передавать далее, чтобы не делать повторный запрос
            self.clear_fields()
            if upd_init_f:
                self.update_init_fields(cursor)
            if upd_input_f:
                self.update_input_fields(cursor)
            if upd_output_f:
                self.update_output_fields(cursor)
        except Exception as e:
            gen_funcs.show_error(e)

    # Update values in "init_fields" - user and list of reasons
    def update_init_fields(self, cursor):
        self.tb_user.setText(from_db.get_cur_user(cursor, slice_flag=True))
        self.cb_reason.addItems(from_db.get_reasons(cursor))

    # Update values in "input_fields" - left part of GUI
    def update_input_fields(self, cursor):
        input_data = None
        try:
            selected_date = self.cal_calendar.selectedDate().toString("yyyy-MM-dd")
            print(selected_date)
            print(gen_funcs.boundaries_work_month(selected_date))
            input_data = from_db.get_input_data(cursor, type_interval='d', date_interval=selected_date)
            if type(input_data) == list and input_data:
                input_data = input_data[0]
        except Exception as e:
            gen_funcs.show_error(e)

        # if exist record with the date
        if input_data:
            if input_data['arrival_time']:
                self.te_time_arr.setTime(gen_funcs.str_to_time(input_data['arrival_time']))
            if input_data['departure_time']:
                self.te_time_dep.setTime(gen_funcs.str_to_time(input_data['departure_time']))
            if input_data['dinner'] is not None:
                self.chb_dinner.setChecked(input_data['dinner'])
            if input_data['remotely'] is not None:
                self.chb_remotely.setChecked(input_data['remotely'])
            if input_data['time_absence_begin']:
                self.te_time_absense_start.setTime(gen_funcs.str_to_time(input_data['time_absence_begin']))
            if input_data['time_absence_end']:
                self.te_time_absense_stop.setTime(gen_funcs.str_to_time(input_data['time_absence_end']))
            if input_data['comment']:
                self.te_comment.setText(input_data['comment'])
            if input_data['reason']:
                # '(\'Больничный\', )' -> 'Больничный'
                if input_data['reason'].startswith('(\'') and input_data['reason'].endswith('\', )'):
                    input_data['reason'] = input_data['reason'][2:-4]

                index = self.cb_reason.findText(input_data['reason'])
                if index == -1:  # if this reason not exist, set reason '' (index=0)
                    index = 0
                try:
                    self.cb_reason.setCurrentIndex(index)
                except TypeError as e:
                    gen_funcs.show_error(e)

    # Update values in "output_fields" - right part of GUI
    def update_output_fields(self, cursor):
        selected_date = self.cal_calendar.selectedDate().toString("yyyy-MM-dd")

        # update stats
        stat_dict = stat.get_stat_for_all_periods(cursor, selected_date)
        if not stat_dict:
            return
        # stat_dict = ['d_time_presence', 'd_time_delta', 'd_flag_conversion',
        #             'w_time_presence', 'w_time_delta', 'w_flag_conversion',
        #             'w_production_percent', 'w_avg_arrival_time', 'w_avg_departure_time',
        #             'm_time_presence', 'm_time_delta', 'm_flag_conversion']

        # view day stat
        self.tb_time_presence.setText(str(stat_dict['d_time_presence']))
        self.tb_difference.setText(str(stat_dict['d_time_delta']))
        if stat_dict['d_flag_conversion']:
            self.tb_difference.setStyleSheet("background-color: green; font-size: 12pt;")
        else:
            self.tb_difference.setStyleSheet("background-color: red; font-size: 12pt;")

        # view week stat
        self.tb_time_presence_sum.setText(str(stat_dict['w_time_presence']))
        self.tb_difference_sum_week.setText(str(stat_dict['w_time_delta']))
        if stat_dict['w_flag_conversion']:
            self.tb_difference_sum_week.setStyleSheet("background-color: green; font-size: 12pt;")
        else:
            self.tb_difference_sum_week.setStyleSheet("background-color: red; font-size: 12pt;")
        self.lcd_production.display(str(stat_dict['w_production_percent']))
        self.tb_time_arr_avg.setText(str(stat_dict['w_avg_arrival_time']))
        self.tb_time_dep_avg.setText(str(stat_dict['w_avg_departure_time']))

        # view month stat
        self.tb_difference_sum_month.setText(str(stat_dict['m_time_delta']))
        if stat_dict['m_flag_conversion']:
            self.tb_difference_sum_month.setStyleSheet("background-color: green; font-size: 12pt;")
        else:
            self.tb_difference_sum_month.setStyleSheet("background-color: red; font-size: 12pt;")








