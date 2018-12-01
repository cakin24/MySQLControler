# -*- coding: UTF-8 -*-
import MySQLdb
from ReadCode import ReadCode
from Notice import MyFrame3
class SaveDocument():
    def __init__(self,sql):
        readcode = ReadCode()
        Line = readcode.return_line()
        # 打开数据库连接
        db = MySQLdb.connect("localhost", "%s" % Line[0],
                             "%s" % Line[1], "%s" % Line[2])
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        try:
           # 执行SQL语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except:
            db.rollback()
            window=MyFrame3(None,"失败！")
            window.Show()
        # 关闭数据库连接
        db.close()