# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeManager.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TimeManager(object):
    def setupUi(self, TimeManager):
        TimeManager.setObjectName("TimeManager")
        TimeManager.resize(931, 602)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 250, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 65, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 250, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 65, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 250, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 250, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 65, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        TimeManager.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(TimeManager)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.gb_input = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_input.setGeometry(QtCore.QRect(10, 10, 411, 581))
        self.gb_input.setTitle("")
        self.gb_input.setObjectName("gb_input")
        self.cal_calendar = QtWidgets.QCalendarWidget(self.gb_input)
        self.cal_calendar.setGeometry(QtCore.QRect(50, 40, 296, 183))
        self.cal_calendar.setMinimumSize(QtCore.QSize(291, 181))
        self.cal_calendar.setObjectName("cal_calendar")
        self.b_apply = QtWidgets.QPushButton(self.gb_input)
        self.b_apply.setGeometry(QtCore.QRect(290, 520, 101, 41))
        self.b_apply.setObjectName("b_apply")
        self.gb_input_time = QtWidgets.QGroupBox(self.gb_input)
        self.gb_input_time.setGeometry(QtCore.QRect(10, 240, 381, 271))
        self.gb_input_time.setTitle("")
        self.gb_input_time.setObjectName("gb_input_time")
        self.te_time_arr = QtWidgets.QTimeEdit(self.gb_input_time)
        self.te_time_arr.setGeometry(QtCore.QRect(20, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.te_time_arr.setFont(font)
        self.te_time_arr.setObjectName("te_time_arr")
        self.l_time_arr = QtWidgets.QLabel(self.gb_input_time)
        self.l_time_arr.setGeometry(QtCore.QRect(10, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_time_arr.setFont(font)
        self.l_time_arr.setObjectName("l_time_arr")
        self.l_time_dep = QtWidgets.QLabel(self.gb_input_time)
        self.l_time_dep.setGeometry(QtCore.QRect(240, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_time_dep.setFont(font)
        self.l_time_dep.setObjectName("l_time_dep")
        self.te_time_dep = QtWidgets.QTimeEdit(self.gb_input_time)
        self.te_time_dep.setGeometry(QtCore.QRect(250, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.te_time_dep.setFont(font)
        self.te_time_dep.setObjectName("te_time_dep")
        self.chb_dinner = QtWidgets.QCheckBox(self.gb_input_time)
        self.chb_dinner.setGeometry(QtCore.QRect(150, 50, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chb_dinner.setFont(font)
        self.chb_dinner.setChecked(True)
        self.chb_dinner.setTristate(False)
        self.chb_dinner.setObjectName("chb_dinner")
        self.gb_additional_param = QtWidgets.QGroupBox(self.gb_input_time)
        self.gb_additional_param.setGeometry(QtCore.QRect(20, 120, 341, 141))
        self.gb_additional_param.setCheckable(True)
        self.gb_additional_param.setChecked(False)
        self.gb_additional_param.setObjectName("gb_additional_param")
        self.te_time_absense_start = QtWidgets.QTimeEdit(self.gb_additional_param)
        self.te_time_absense_start.setGeometry(QtCore.QRect(80, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.te_time_absense_start.setFont(font)
        self.te_time_absense_start.setObjectName("te_time_absense_start")
        self.l_reason = QtWidgets.QLabel(self.gb_additional_param)
        self.l_reason.setGeometry(QtCore.QRect(220, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.l_reason.setFont(font)
        self.l_reason.setObjectName("l_reason")
        self.cb_reason = QtWidgets.QComboBox(self.gb_additional_param)
        self.cb_reason.setGeometry(QtCore.QRect(200, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_reason.setFont(font)
        self.cb_reason.setObjectName("cb_reason")
        self.te_time_absense_stop = QtWidgets.QTimeEdit(self.gb_additional_param)
        self.te_time_absense_stop.setGeometry(QtCore.QRect(200, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.te_time_absense_stop.setFont(font)
        self.te_time_absense_stop.setObjectName("te_time_absense_stop")
        self.l_time_absense_start = QtWidgets.QLabel(self.gb_additional_param)
        self.l_time_absense_start.setGeometry(QtCore.QRect(70, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.l_time_absense_start.setFont(font)
        self.l_time_absense_start.setObjectName("l_time_absense_start")
        self.l_time_absense_stop = QtWidgets.QLabel(self.gb_additional_param)
        self.l_time_absense_stop.setGeometry(QtCore.QRect(190, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.l_time_absense_stop.setFont(font)
        self.l_time_absense_stop.setObjectName("l_time_absense_stop")
        self.l_comment = QtWidgets.QLabel(self.gb_additional_param)
        self.l_comment.setGeometry(QtCore.QRect(40, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.l_comment.setFont(font)
        self.l_comment.setObjectName("l_comment")
        self.te_comment = QtWidgets.QTextEdit(self.gb_additional_param)
        self.te_comment.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.te_comment.setObjectName("te_comment")
        self.b_cur_time_arr = QtWidgets.QPushButton(self.gb_input_time)
        self.b_cur_time_arr.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.b_cur_time_arr.setObjectName("b_cur_time_arr")
        self.b_cur_time_dep = QtWidgets.QPushButton(self.gb_input_time)
        self.b_cur_time_dep.setGeometry(QtCore.QRect(250, 80, 91, 21))
        self.b_cur_time_dep.setObjectName("b_cur_time_dep")
        self.chb_remotely = QtWidgets.QCheckBox(self.gb_input_time)
        self.chb_remotely.setGeometry(QtCore.QRect(150, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chb_remotely.setFont(font)
        self.chb_remotely.setChecked(False)
        self.chb_remotely.setTristate(False)
        self.chb_remotely.setObjectName("chb_remotely")
        self.l_user = QtWidgets.QLabel(self.gb_input)
        self.l_user.setGeometry(QtCore.QRect(170, 10, 71, 16))
        self.l_user.setObjectName("l_user")
        self.b_clear = QtWidgets.QPushButton(self.gb_input)
        self.b_clear.setGeometry(QtCore.QRect(10, 520, 101, 41))
        self.b_clear.setObjectName("b_clear")
        self.tb_user = QtWidgets.QTextBrowser(self.gb_input)
        self.tb_user.setGeometry(QtCore.QRect(250, 10, 131, 23))
        self.tb_user.setObjectName("tb_user")
        self.gb_output = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_output.setGeometry(QtCore.QRect(430, 0, 481, 591))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_output.setFont(font)
        self.gb_output.setObjectName("gb_output")
        self.gb_week = QtWidgets.QGroupBox(self.gb_output)
        self.gb_week.setGeometry(QtCore.QRect(20, 140, 421, 291))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_week.setFont(font)
        self.gb_week.setObjectName("gb_week")
        self.tb_time_arr_avg = QtWidgets.QTextBrowser(self.gb_week)
        self.tb_time_arr_avg.setGeometry(QtCore.QRect(30, 60, 111, 41))
        self.tb_time_arr_avg.setObjectName("tb_time_arr_avg")
        self.l_time_arr_avg = QtWidgets.QLabel(self.gb_week)
        self.l_time_arr_avg.setGeometry(QtCore.QRect(10, 30, 181, 21))
        self.l_time_arr_avg.setObjectName("l_time_arr_avg")
        self.tb_time_dep_avg = QtWidgets.QTextBrowser(self.gb_week)
        self.tb_time_dep_avg.setGeometry(QtCore.QRect(260, 60, 111, 41))
        self.tb_time_dep_avg.setObjectName("tb_time_dep_avg")
        self.l_time_dep_avg = QtWidgets.QLabel(self.gb_week)
        self.l_time_dep_avg.setGeometry(QtCore.QRect(240, 30, 181, 21))
        self.l_time_dep_avg.setObjectName("l_time_dep_avg")
        self.tb_time_presence_sum = QtWidgets.QTextBrowser(self.gb_week)
        self.tb_time_presence_sum.setGeometry(QtCore.QRect(30, 150, 111, 41))
        self.tb_time_presence_sum.setObjectName("tb_time_presence_sum")
        self.l_time_presence_sum = QtWidgets.QLabel(self.gb_week)
        self.l_time_presence_sum.setGeometry(QtCore.QRect(10, 120, 201, 21))
        self.l_time_presence_sum.setObjectName("l_time_presence_sum")
        self.l_prodaction = QtWidgets.QLabel(self.gb_week)
        self.l_prodaction.setGeometry(QtCore.QRect(260, 120, 111, 21))
        self.l_prodaction.setObjectName("l_prodaction")
        self.lcd_production = QtWidgets.QLCDNumber(self.gb_week)
        self.lcd_production.setGeometry(QtCore.QRect(270, 150, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lcd_production.setFont(font)
        self.lcd_production.setSmallDecimalPoint(False)
        self.lcd_production.setDigitCount(3)
        self.lcd_production.setProperty("value", 100.0)
        self.lcd_production.setObjectName("lcd_production")
        self.tb_difference_sum_week = QtWidgets.QTextBrowser(self.gb_week)
        self.tb_difference_sum_week.setGeometry(QtCore.QRect(150, 240, 111, 41))
        self.tb_difference_sum_week.setObjectName("tb_difference_sum_week")
        self.l_difference_sum_week = QtWidgets.QLabel(self.gb_week)
        self.l_difference_sum_week.setGeometry(QtCore.QRect(150, 210, 121, 21))
        self.l_difference_sum_week.setObjectName("l_difference_sum_week")
        self.gb_day = QtWidgets.QGroupBox(self.gb_output)
        self.gb_day.setGeometry(QtCore.QRect(20, 440, 421, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_day.setFont(font)
        self.gb_day.setCheckable(False)
        self.gb_day.setObjectName("gb_day")
        self.l_time_presence = QtWidgets.QLabel(self.gb_day)
        self.l_time_presence.setGeometry(QtCore.QRect(40, 40, 151, 21))
        self.l_time_presence.setObjectName("l_time_presence")
        self.tb_time_presence = QtWidgets.QTextBrowser(self.gb_day)
        self.tb_time_presence.setGeometry(QtCore.QRect(50, 70, 111, 41))
        self.tb_time_presence.setObjectName("tb_time_presence")
        self.tb_difference = QtWidgets.QTextBrowser(self.gb_day)
        self.tb_difference.setGeometry(QtCore.QRect(270, 70, 111, 41))
        self.tb_difference.setObjectName("tb_difference")
        self.l_difference = QtWidgets.QLabel(self.gb_day)
        self.l_difference.setGeometry(QtCore.QRect(290, 40, 61, 21))
        self.l_difference.setObjectName("l_difference")
        self.gb_month = QtWidgets.QGroupBox(self.gb_output)
        self.gb_month.setGeometry(QtCore.QRect(20, 20, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_month.setFont(font)
        self.gb_month.setCheckable(False)
        self.gb_month.setObjectName("gb_month")
        self.l_difference_sum_month = QtWidgets.QLabel(self.gb_month)
        self.l_difference_sum_month.setGeometry(QtCore.QRect(150, 20, 121, 21))
        self.l_difference_sum_month.setObjectName("l_difference_sum_month")
        self.tb_difference_sum_month = QtWidgets.QTextBrowser(self.gb_month)
        self.tb_difference_sum_month.setGeometry(QtCore.QRect(150, 50, 111, 41))
        self.tb_difference_sum_month.setObjectName("tb_difference_sum_month")
        TimeManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(TimeManager)
        QtCore.QMetaObject.connectSlotsByName(TimeManager)

    def retranslateUi(self, TimeManager):
        _translate = QtCore.QCoreApplication.translate
        TimeManager.setWindowTitle(_translate("TimeManager", "MainWindow"))
        self.b_apply.setText(_translate("TimeManager", "Применить"))
        self.l_time_arr.setText(_translate("TimeManager", "Время прибытия"))
        self.l_time_dep.setText(_translate("TimeManager", "Время убытия"))
        self.chb_dinner.setText(_translate("TimeManager", "Обед"))
        self.gb_additional_param.setTitle(_translate("TimeManager", "Доп. параметры"))
        self.l_reason.setText(_translate("TimeManager", "Причина неявки"))
        self.l_time_absense_start.setText(_translate("TimeManager", "Отсутствовал с"))
        self.l_time_absense_stop.setText(_translate("TimeManager", "Отсутствовал до"))
        self.l_comment.setText(_translate("TimeManager", "Комментарий"))
        self.b_cur_time_arr.setText(_translate("TimeManager", "Текущее время"))
        self.b_cur_time_dep.setText(_translate("TimeManager", "Текущее время"))
        self.chb_remotely.setText(_translate("TimeManager", "Удаленно"))
        self.l_user.setText(_translate("TimeManager", "Пользователь"))
        self.b_clear.setText(_translate("TimeManager", "Очистить"))
        self.gb_output.setTitle(_translate("TimeManager", "Статистика"))
        self.gb_week.setTitle(_translate("TimeManager", "За неделю:"))
        self.l_time_arr_avg.setText(_translate("TimeManager", "Время прибытия (сред.)"))
        self.l_time_dep_avg.setText(_translate("TimeManager", "Время убытия (сред.)"))
        self.l_time_presence_sum.setText(_translate("TimeManager", "Время присутствия (сумм.)"))
        self.l_prodaction.setText(_translate("TimeManager", "Выработка (%)"))
        self.l_difference_sum_week.setText(_translate("TimeManager", "Разница (сумм.)"))
        self.gb_day.setTitle(_translate("TimeManager", "За день:"))
        self.l_time_presence.setText(_translate("TimeManager", "Время присутствия"))
        self.l_difference.setText(_translate("TimeManager", "Разница"))
        self.gb_month.setTitle(_translate("TimeManager", "За месяц:"))
        self.l_difference_sum_month.setText(_translate("TimeManager", "Разница (сумм.)"))
