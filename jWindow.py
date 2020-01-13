# _*_ coding:utf-8 _*_

from PyQt5.QtWidgets import QWidget, QDesktopWidget


class jWindow(QWidget):
    def __init__(self, title='Title', long=800, wide=600):
        super().__init__()
        self.title = title
        self.long = long
        self.wide = wide

    def create_win(self):
        self.resize(self.long, self.wide)
        self.setWindowTitle(self.title)
        self.show()

    def locate_center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start_win(self):
        self.show()
