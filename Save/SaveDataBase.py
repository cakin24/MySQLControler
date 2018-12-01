# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
from CreateDatabase import CreateDatabase
from Notice import MyFrame3
###########################################################################
## Class MyFrame9
###########################################################################
class MyFrame9(wx.Frame):
    def __init__(self, parent):
        #初始化框架
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Windows类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直和水平布局控制器
        bSizer10 = wx.BoxSizer(wx.VERTICAL)
        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)
        #输入数据库名提示，位于布局控制器11
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY,
                                           u"请输入DATABASE名称",
                                           wx.DefaultPosition, wx.Size(150, 50), 0)
        self.m_staticText8.Wrap(-1)
        bSizer11.Add(self.m_staticText8, 0, wx.ALL, 5)
        #要添加的数据库名，位于布局控制器11
        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY,
                                       wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(120, 50), 0)
        bSizer11.Add(self.m_textCtrl6, 0, wx.ALL, 5)
        #布局控制器11在布局控制器10中
        bSizer10.Add(bSizer11, 1, wx.EXPAND, 5)
        #水平布局控制器
        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)
        #空白标签，位于布局控制器12
        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY,
                                           wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(150, 50), 0)
        self.m_staticText9.Wrap(-1)
        bSizer12.Add(self.m_staticText9, 0, wx.ALL, 5)
        #确认按钮，位于布局控制器12
        self.m_button6 = wx.Button(self, wx.ID_ANY, u"确定",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer12.Add(self.m_button6, 0, wx.ALL, 5)
        #布局控制器12位于布局控制器10
        bSizer10.Add(bSizer12, 1, wx.EXPAND, 5)
        #Window类的方法
        self.SetSizer(bSizer10)
        self.Layout()
        self.Centre(wx.BOTH)
        # 按钮绑定事件
        self.m_button6.Bind(wx.EVT_BUTTON, self.m_button6OnButtonClick)
    def __del__(self):
        pass
    # 点击按钮，新建一个数据库
    def m_button6OnButtonClick(self, event):
        dataname=self.m_textCtrl6.GetValue()
        sql='create database %s'%dataname
        createdatabase=CreateDatabase(sql)
        if(dataname):
            window=MyFrame3(None)
            window.Show()
        else:
            window=MyFrame3(None,'请检查DATABASE名称是否输入！')
            window.Show()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame9(None)
    window.Show()
    app.MainLoop()