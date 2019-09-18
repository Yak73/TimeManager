import sys
from PyQt5 import QtWidgets

from TimeManager import funcsGUI

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = funcsGUI.TimeManagerApp()
    window.show()
    app.exec_()
