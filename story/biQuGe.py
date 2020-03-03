# _*_ coding:utf-8 _*_
import threading

from bs4 import BeautifulSoup

from httpRequest import httpRequest
from jStoppableThread import jStoppableThread


class biQuGe(jStoppableThread):
    """
    This class is used to download story from a website.
    :param name: The story name
    :param path: The path used to store story on the disk
    :param ui: The ui handle of the user tool, if ui is None, this class with use standard function to print log
    :param url: The home page of the story
    """
    def __init__(self, name=None, path=None, ui=None, url=None):
        super().__init__()
        self.story_source = None
        self.story_name = name
        self.story_path = path
        self.story_url = url
        self.ui = ui
        self.directory_num = 0
        self.directory = []

    def log_print(self, log):
        if self.ui is not None:
            self.ui.textBrowser.append(log)
        else:
            print(log)

    def get_story_directory(self):
        self.story_source = httpRequest.super_http(self.story_url)
        if self.story_source is None:
            return

        self.log_print('读取《' + self.story_name + '》目录')
        content = self.story_source
        soup = BeautifulSoup(content, 'html.parser')
        # 查找第一个dl标签
        dl = soup.find('dl')
        # 查找dl下所有a标签
        aa = dl.find_all('a')
        # 将所有章节信息保存到数组
        for a in aa:
            chapter = [a['href'], a.string]
            self.directory.append(chapter)
            self.directory_num += 1
        '''for item in dl.children:
            a = item.find('a')'''
        self.log_print('读取《%s》目录完成，共有%d章节' % (self.story_name, self.directory_num))

    def download_story_content(self,):
        file = self.story_path + '\\' + self.story_name + '.txt'
        try:
            f = open(file, 'a+', errors='ignore')

            for chapter in self.directory:
                if self.is_stopped():
                    self.log_print('终止下载')
                    break
                else:
                    chapter_url = self.story_url + '/' + chapter[0]
                    chapter_tile = chapter[1]
                    self.log_print('下载章节： ' + chapter_tile)
                    content = httpRequest.super_http(chapter_url)
                    if content is None:
                        self.log_print("获取章节内容失败")
                        continue
                    else:
                        soup = BeautifulSoup(content, 'html.parser')
                        div = soup.find('div', attrs={'id': 'content'})
                        # [s.extract() for s in soup('script')]
                        story_content = str(div).replace('<br/>', '\n').replace('<div id="content">', '').replace('</div>', '').strip()

                        f.writelines(chapter_tile + '\n')
                        f.writelines(story_content + '\n')

            f.close()
        except Exception as e:
            print(e)

    def run(self):
        self.get_story_directory()
        self.download_story_content()
