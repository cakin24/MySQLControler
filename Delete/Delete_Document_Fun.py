# -*- coding:utf-8 -*-
import MySQLdb
from ReadCode import ReadCode
from Notice import MyFrame3
class Delete_Document_Fun():
    def __init__(self,sql):
        readcode = ReadCode()
        Line = readcode.return_line()
        try:
            db = MySQLdb.connect("localhost", "%s" % Line[0],
                                 "%s" % Line[1], "%s" % Line[2])
        except:
            notice = MyFrame3(None, '请检查主面板的用户名、'
                                    '密码、DATABASE是否输入！')
            notice.Show()
        else:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            try:
                # 执行SQL语句
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                notice = MyFrame3(None, "执行SQL语句出错！")
                notice.Show()
            # 关闭数据库连接
        db.close()