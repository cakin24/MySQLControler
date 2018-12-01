# -*- coding: utf-8 -*-
##########################################
## Python code generated with wxFormBuilder
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
######################################
import wx
import wx.xrc
from Check_Database import Check_Database
#####################
## Class MyFrame21
####################
class MyFrame21(wx.Frame):
    def __init__(self, parent):
        #初始化框架
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                title=wx.EmptyString,
                pos=wx.DefaultPosition,
                size=wx.Size(191, 799),
                style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Windows类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #布局控制器
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        #文本控件
        self.m_textCtrl1 = wx.TextCtrl(self,
                    wx.ID_ANY, wx.EmptyString,
                    wx.DefaultPosition, wx.Size(300, 1000),
                    style=wx.TE_MULTILINE | wx.TE_READONLY)
        #文本控件加入到布局控制器中
        bSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)
        #Window类的属性
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        #定义一个检查数据库类
        check_database=Check_Database('show databases','1')
        #文本控件显示数据库结果
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl1.SetValue(show)
    def __del__(self):
        pass

#编入测试模块
if __name__=='__main__':
    app=wx.App()
    window=MyFrame21(None)
    window.Show()
    app.MainLoop()