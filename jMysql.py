# _*_ coding:utf-8 _*_

import mysql.connector


class jMysql:
    def __init__(self, host, user, passwd, db=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.mysql_client = None

    def start_mysql_client(self):
        print('Connecting mysql %s......' % self.host)
        try:
            self.mysql_client = mysql.connector.connect(host=self.host,
                                                        user=self.user,
                                                        passwd=self.passwd,
                                                        db=self.db,
                                                        auth_plugin='mysql_native_password')
        except Exception as e:
            print(e)

        if self.mysql_client is not None:
            print('Connected to mysql %s.' % self.host)

    def execute_sql(self, sql, val=None):
        self.start_mysql_client()
        mysql_cursor = None

        if self.mysql_client is not None:
            try:
                mysql_cursor = self.mysql_client.cursor()
                mysql_cursor.execute(sql, val)
            except Exception as e:
                print(e)

        return mysql_cursor
