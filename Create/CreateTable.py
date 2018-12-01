# -*- coding: UTF-8 -*-
# import wx
# import wx.xrc
import MySQLdb
from ReadCode import ReadCode
from Notice import MyFrame3
class CreateTable():
    def __init__(self,sql):
        readcode = ReadCode()
        Line = readcode.return_line()
        # 打开数据库连接
        try:
            db = MySQLdb.connect("localhost", "%s" % Line[0],
                                 "%s" % Line[1], "%s" % Line[2])
        except:
            notice = MyFrame3(None, '请检查主面板的用户名、'
                                    '密码、DATABASE是否输入！')
            notice.Show()
        else:
            try:
                # 使用cursor()方法获取操作游标
                cursor = db.cursor()
                cursor.execute(sql)
            except:
                notice = MyFrame3(None, '请检查表名等是否重复、出错！')
                notice.Show()
            # 关闭数据库连接
            db.close()

# if __name__=='__main__':
#     app=wx.App()
#     window=MyFrame3(None)
#     test = CreateTable( "CREATE TABLE `sys_permission_test` (`id` int(11) NOT NULL AUTO_INCREMENT,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;")
#     #window.Show()
#     app.MainLoop()
