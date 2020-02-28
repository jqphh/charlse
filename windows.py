# _*_ coding:utf-8 _*_

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from functools import partial
import sys

from jDownStory import jDownStory
from spider import Ui_MainWindow
from httpRequest import httpRequest
from jThread import jThread


download_thread = None


def download_story(story_site, story_name, story_dir, win_ui):
    story = jDownStory(name=story_name, path=story_dir, ui=win_ui, url=story_site)
    story.download_story()


def click1():
    if download_thread is not None:
        download_thread.exit()


def click2(ui_win):
    story_name = ui_win.lineEdit.text()
    story_site = ui_win.lineEdit_2.text()
    story_dir = ui_win.lineEdit_3.text()

    ui_win.textBrowser.append('开始从' + story_site + '下载《' + story_name + '》')
    ui_win.textBrowser.append('文件将被保存到' + story_dir + '\\' + story_name + '.txt')
    download_thread = jThread('Download Thread', download_story, (story_site, story_name, story_dir, ui_win))
    # 设置守护线程(分离)，防止阻塞主界面
    download_thread.setDaemon(True)
    download_thread.start()


def click3(ui_win):
    file_path = QFileDialog.getExistingDirectory(ui_win, "请选择文件路径...", ".")


'''class downloadStory(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def click2(self, ui):
        pass'''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(click1)
    ui.pushButton_2.clicked.connect(partial(click2, ui))
    ui.toolButton.clicked.connect(partial(click3, ui))
    ui.pushButton_3.clicked.connect(partial(click3, ui))
    sys.exit(app.exec_())


