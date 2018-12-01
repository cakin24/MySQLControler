# -*- coding: UTF-8 -*-
import MySQLdb
from Notice import MyFrame3
from ReadCode import ReadCode
class Check_Desc():
    # 打开数据库连接
    def __init__(self,table):
        readcode=ReadCode()
        Line=readcode.return_line()
        # 打开数据库连接
        db = MySQLdb.connect("localhost", "%s"%Line[0],
                             "%s"%Line[1], "%s"%Line[2])
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql="desc %s" % table
        self.return_result=[]
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                for i in range(0, len(row)):
                    self.return_result.append(str(row[i])+' ')
                self.return_result.append('\n')
        except:
            notice=MyFrame3(None,"Error: unable to fecth data111")
            notice.Show()
        # 关闭数据库连接
        db.close()
    def return_result(self):
        return self.return_result
if __name__=='__main__':
    check_database=Check_Desc('create_user')
    for i in range(0,len(check_database.return_result)):
        print check_database.return_result[i]