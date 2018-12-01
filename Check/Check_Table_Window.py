# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
from Check_Database import Check_Database
###########################################################################
## Class MyFrame1
###########################################################################
class MyFrame23(wx.Frame):
    def __init__(self, parent):
        #初始化框架
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(191, 799),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Window类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #布局控制器
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        #用于显示特定数据库的数据表，多行，只读
        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(300, 1000)
                                       , style=wx.TE_READONLY|wx.TE_MULTILINE)
        #位于布局控制器1中
        bSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)
        #Window类的方法
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        #查询并显示特定数据库的数据表
        check_database=Check_Database('show tables')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl1.SetValue(show)
    def __del__(self):
        pass

#编入测试模块
if __name__=='__main__':
    app=wx.App()
    window=MyFrame23(None)
    window.Show()
    app.MainLoop()