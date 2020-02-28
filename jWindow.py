# _*_ coding:utf-8 _*_
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QDesktopWidget


class jWindow(QWidget):
    def locate_center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_icon(self, file):
        self.setWindowIcon(QIcon(file))

    def start_win(self):
        self.show()
