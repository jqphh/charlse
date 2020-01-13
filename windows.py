# _*_ coding:utf-8 _*_

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from jWindow import jWindow
import sys


class window(jWindow):

    def run(self):
        self.create_win()
        self.set_icon()
        self.locate_center()
        self.start_win()

    def set_icon(self):
        self.setWindowIcon(QIcon('./resource/cat.jpg'))


app = QApplication(sys.argv)
win = window('Charlse', 800, 600)
win.run()
sys.exit(app.exec_())