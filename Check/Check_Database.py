# -*- coding: UTF-8 -*-
import MySQLdb
from Notice import MyFrame3
from ReadCode import ReadCode
class Check_Database():
    # 打开数据库连接
    def __init__(self,sql,database='0'):
        if(not int(database)):
            readcode=ReadCode()
            Line=readcode.return_line()
            try:
                db = MySQLdb.connect("localhost",
                    "%s"%Line[0],"%s"%Line[1],
                    "%s"%Line[2])
            except:
                notice=MyFrame3(None,
                    '请检查主面板的用户名、密码'
                    '、DATABASE是否输入！')
                notice.Show()
            else:
                # 使用cursor()方法获取操作游标
                cursor = db.cursor()
                self.return_result=[]
                try:
                   # 执行SQL语句
                   cursor.execute(sql)
                   # 获取所有记录列表
                   results = cursor.fetchall()
                   for row in results:
                        for i in range(0,len(row)):
                            self.return_result.append(row[i])
                        self.return_result.append('\n')
                except:
                    notice = MyFrame3(None,
                            "Error: unable to fecth data")
                    notice.Show()
                # 关闭数据库连接
                db.close()
        else:
            readcode = ReadCode()
            Line = readcode.return_line()
            try:
                db = MySQLdb.connect("localhost", "%s" % Line[0]
                                     , "%s" % Line[1])
            except:
                pass
            else:
                # 使用cursor()方法获取操作游标
                cursor = db.cursor()
                self.return_result = []
                try:
                    # 执行SQL语句
                    cursor.execute(sql)
                    # 获取所有记录列表
                    results = cursor.fetchall()
                    for row in results:
                        for i in range(0, len(row)):
                            self.return_result.append(row[i])
                        self.return_result.append('\n')
                except:
                    notice=MyFrame3(None,
                              "Error: unable to fecth data")
                    notice.Show()
                # 关闭数据库连接
                db.close()
    def return_result(self):
        return self.return_result
if __name__=='__main__':
    check_database=Check_Database('show databases','1')
    for i in range(0,len(check_database.return_result)):
        print check_database.return_result[i]