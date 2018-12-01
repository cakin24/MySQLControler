# -*- coding:utf-8 -*-
class CodeInFile():
    def __init__(self,name,code,database):
        self.rootdir='E:\Python\MySQLControler'
        File=open('%s/code'%self.rootdir,'w')
        File.write('%s\t'%name)
        File.write('%s\t'%code)
        File.write('%s'%database)
        File.close()
if __name__=='__main__':
    test=CodeInFile('root','123456','test')