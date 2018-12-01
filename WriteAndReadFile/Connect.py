# -*-coding:utf-8 -*-
import MySQLdb
from ReadCode import ReadCode
class Connect():
    def __init__(self,database,sql):
        readcode=ReadCode()
        name=readcode.return_line()[0]
        code=readcode.return_line()[1]
        db=MySQLdb.connect("localhost","%s"%name,"%s"%code,"%s"%database)
        cursor=db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()
if __name__=='__main__':
    test=Connect("test","insert into create_user(email) "
                        "VALUES('798103176@qq.com')")