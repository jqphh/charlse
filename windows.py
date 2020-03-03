# _*_ coding:utf-8 _*_

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from functools import partial
import sys

from story.biQuGe import biQuGe
from story.story import Ui_MainWindow


download_thread = None


def cancel_button_func():
    if download_thread is not None:
        download_thread.stop()


def download_story_button_func(ui_win):
    story_name = ui_win.lineEdit.text()
    story_site = ui_win.lineEdit_2.text()
    story_dir = ui_win.lineEdit_3.text()

    ui_win.textBrowser.append('开始从' + story_site + '下载《' + story_name + '》')
    ui_win.textBrowser.append('文件将被保存到' + story_dir + '\\' + story_name + '.txt')
    # 声明复用全局变量，防止冲突
    global download_thread
    download_thread = biQuGe(name=story_name, path=story_dir, ui=ui_win, url=story_site)
    # 设置守护线程(分离)，防止阻塞主界面
    download_thread.setDaemon(True)
    download_thread.start()


def choose_dir_button_func(ui_win):
    # getExistingDirectory第一个参数必须传入ui的widget，而不是ui本身
    file_path = QFileDialog.getExistingDirectory(ui_win.centralwidget, '请选择文件路径...', '')
    ui_win.lineEdit_3.setText(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(cancel_button_func)
    ui.pushButton_2.clicked.connect(partial(download_story_button_func, ui))
    ui.toolButton.clicked.connect(partial(choose_dir_button_func, ui))
    sys.exit(app.exec_())


