# -*- coding:utf-8 -*-
class ReadCode():
    def __init__(self):
        self.rootdir = 'E:\Python\MySQLControler'
        File=open('%s/code'%self.rootdir,'r')
        self.Line=File.readline().split()
        File.close()
    def return_line(self):
        return self.Line
if __name__=='__main__':
    test=ReadCode()
    print test.return_line()