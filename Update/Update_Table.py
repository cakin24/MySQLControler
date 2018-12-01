# -*- coding: UTF-8 -*-
import MySQLdb
from ReadCode import ReadCode
from Notice import MyFrame3
class Update_Table():
    def __init__(self,sql):
        readcode=ReadCode()
        Line=readcode.return_line()
        try:
            db = MySQLdb.connect("localhost","%s"%Line[0],
                                 "%s"%Line[1],"%s"%Line[2])
        except:
            notice=MyFrame3(None,'请检查主面板的用户名、'
                                 '密码、DATABASE是否输入！')
            notice.Show()
        else:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            try:
               # 执行SQL语句
               cursor.execute(sql)
               # 提交到数据库执行
               db.commit()
            except:
               # 发生错误时回滚
               db.rollback()
            # 关闭数据库连接
            db.close()