import sys
import os

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtWidgets, Qt, QtCore
from PyQt5.QtGui import QPixmap

from ui.main_scr import Ui_MainWindow
from ui.error_scr import Ui_error_scr
from ui.help_scr import Ui_HelpScr

from functions.calculations import calc_method_one, calc_method_two, PA
from functions.validator import *

"""
TODO: 
приделать видео + звук
добавить текст в справку 
"""


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.K_choose.addItems(["12,5", "13,5", "15"])
        self.ui.K_choose_1.addItems(["12,5", "13,5", "15"])

        self.ui.M1_btn.clicked.connect(self.calc_m1)
        self.ui.M2_btn.clicked.connect(self.calc_m2)
        self.ui.Start.clicked.connect(self.play)
        self.ui.Help.aboutToShow.connect(self.create_help_scr)

    def calc_m1(self):
        counter_of_errors = 0
        k = self.ui.K_choose.currentText().replace(",", ".")
        g = self.ui.G_Input.toPlainText().replace(",", ".")

        if validate(k):
            k = float(k)
        else:
            counter_of_errors = counter_of_errors + 1

        if validate(g):
            g = float(g)
        else:
            counter_of_errors += 1

        if counter_of_errors > 0:
            if counter_of_errors == 1:
                error_txt = f"Ошибка!\nВы не ввели {counter_of_errors} значение"
            else:
                error_txt = f"Ошибка!\nВы не ввели {counter_of_errors} значений"
            wng = ErrorMessage(error_txt)
            wng.show()
            wng.exec()

        else:
            lf, df = calc_method_one(k, g)
            self.ui.Lf1_Out.setText(f"{round(lf, 5)}")
            self.ui.Df1_Out.setText(f"{round(df, 5)}")

    def calc_m2(self):
        counter_of_errors = 0
        k = self.ui.K_choose_1.currentText().replace(",", ".")
        pv = self.ui.Pv_input.toPlainText().replace(",", ".")

        if validate(k):
            k = float(k)
        else:
            counter_of_errors = counter_of_errors + 1

        if validate(pv):
            pv = float(pv)
        else:
            counter_of_errors += 1

        if counter_of_errors > 0:
            if counter_of_errors == 1:
                error_txt = f"Ошибка!\nВы не ввели {counter_of_errors} значение"
            else:
                error_txt = f"Ошибка!\nВы не ввели {counter_of_errors} значений"
            wng = ErrorMessage(error_txt)
            wng.show()
            wng.exec()

        else:
            if pv < PA:
                error_txt = f"Ошибка!\nPv должно быть больше {PA}"
                wng = ErrorMessage(error_txt)
                wng.show()
                wng.exec()
            else:
                lf, df = calc_method_two(k, pv)
                self.ui.Lf2_Out.setText(f"{round(lf, 5)}")
                self.ui.Df2_Out.setText(f"{round(df, 5)}")

    @staticmethod
    def create_help_scr():
        help_screen = HelpScreen()
        help_screen.show()
        help_screen.exec()

    @staticmethod
    def play():
        current_file = os.path.realpath(__file__)
        path = os.path.dirname(current_file) + "\\bin\\visualization.mp4"
        os.startfile(path)


class HelpScreen(QtWidgets.QDialog):

    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(HelpScreen, self).__init__()
        self.ui = Ui_HelpScr()
        self.ui.setupUi(self)
        self.h = 359
        self.w = 569

        current_file = os.path.realpath(__file__)
        path = os.path.dirname(current_file) + "\\bin\\Text.Rmd"
        txt, tmp_txt = "", open(path, encoding="utf-8").readlines()
        for el in tmp_txt:
            txt += el

        self.lbl = QtWidgets.QTextBrowser()
        # self.lbl.setWordWrapMode(Qt.Qt.TextWordWrap)
        self.lbl.setMarkdown(txt)

        # self.lbl.setWordWrap(True)
        # self.lbl.setTextFormat(Qt.Qt.MarkdownText)
        # self.lbl.setText(txt)

        self.ui.scroll.setWidget(self.lbl)
        self.resized.connect(self.resize_widgets)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(HelpScreen, self).resizeEvent(event)

    def resize_widgets(self):
        self.h = self.size().height()
        self.w = self.size().width()
        self.lbl.setMaximumWidth(self.w - 7)
        self.ui.scroll.setGeometry(10, 2, self.w, self.h - 9)


class ErrorMessage(QtWidgets.QDialog):
    def __init__(self, err_txt=""):
        super().__init__()
        self.ui = Ui_error_scr()
        self.ui.setupUi(self)

        current_file = os.path.realpath(__file__)
        path = os.path.dirname(current_file) + "\\bin\\warning_.png"
        pixmap = QPixmap(path)
        self.ui.Warn_Ico.setPixmap(pixmap)
        self.ui.Btn.clicked.connect(self.ex)

        self.ui.Error_Out.setText(err_txt)

    def ex(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
