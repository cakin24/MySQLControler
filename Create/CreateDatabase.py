# -*-coding:utf-8 -*-
import MySQLdb
from ReadCode import ReadCode
class CreateDatabase():
    def __init__(self,sql):
        readcode=ReadCode()
        name=readcode.return_line()[0]
        code=readcode.return_line()[1]
        db=MySQLdb.connect("localhost","%s"%name,"%s"%code)
        cursor=db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()
if __name__=='__main__':
    test=CreateDatabase("create database test2")