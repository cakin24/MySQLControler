# -*- coding: utf-8 -*-
#####################################
## Python code generated with wxFormBuilder
## http://www.wxformbuilder.org/
## Check模块显示窗口
## PLEASE DO "NOT" EDIT THIS FILE!
###################################
import wx
import wx.xrc
#导入查看数据库窗口模块
from Check_Database_Window import MyFrame21
#导入查看数据库中表模块
from Check_Table_Window import MyFrame23
#导入查看数据记录模块（数据）
from Check_Document_Window import MyFrame25
#导入查看表结构模块
from Check_Desc_Window import MyFrame27
####################
## Class MyFrame19
####################
class MyFrame19(wx.Frame):
    #初始化函数，需要在初始化是传入父面板
    def __init__(self, parent):
        #主框架初始化
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
            title=wx.EmptyString,pos=wx.DefaultPosition,
            size=wx.Size(500, 155),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直布局管理器
        bSizer7 = wx.BoxSizer(wx.VERTICAL)
        #水平布局管理器
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        #添加一个空白文本框
        self.m_staticText6 = wx.StaticText(self,
            wx.ID_ANY, wx.EmptyString,
            wx.DefaultPosition, wx.Size(100, 50), 0)
        self.m_staticText6.Wrap(-1)
        #布局控制器8中加入文本框6
        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)
        #查看DATABASE按钮
        self.m_button10 = wx.Button(self, wx.ID_ANY,
            u"查看DATABASE",
            wx.DefaultPosition, wx.Size(120, 50), 0)
        # 布局控制器8中加入查看Database
        bSizer8.Add(self.m_button10, 0, wx.ALL, 5)
        #查看TABLE按钮
        self.m_button11 = wx.Button(self, wx.ID_ANY,
            u"查看TABLE",wx.DefaultPosition,
            wx.Size(120, 50), 0)
        # 布局控制器8中加入查看数据表按钮
        bSizer8.Add(self.m_button11, 0, wx.ALL, 5)
        # 布局控制器8在布局控制7中
        bSizer7.Add(bSizer8, 0, wx.EXPAND, 5)
        #水平布局管理器
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)
        # 添加一个空白文本框
        self.m_staticText7 = wx.StaticText(self,
            wx.ID_ANY, wx.EmptyString,
            wx.DefaultPosition, wx.Size(100, 50), 0)
        self.m_staticText7.Wrap(-1)
        # 布局控制器9中加入文本框7
        bSizer9.Add(self.m_staticText7, 0, wx.ALL, 5)
        #查看记录按钮
        self.m_button12 = wx.Button(self,
            wx.ID_ANY, u"查看记录",
            wx.DefaultPosition, wx.Size(120, 50), 0)
        #将查看按钮添加到布局控制器9中
        bSizer9.Add(self.m_button12, 0, wx.ALL, 5)
        #描述按钮
        self.m_button13 = wx.Button(self, wx.ID_ANY,
            u"Desc",
            wx.DefaultPosition, wx.Size(120, 50), 0)
        # 将描述按钮添加到布局控制器9中
        bSizer9.Add(self.m_button13, 0, wx.ALL, 5)
        #将布局控制器9添加到布局控制器7中
        bSizer7.Add(bSizer9, 0, wx.EXPAND, 5)
        #以下三个方法是Window类的方法
        self.SetSizer(bSizer7)
        self.Layout()
        self.Centre(wx.BOTH)
        # 给各个按钮绑定事件
        self.m_button10.Bind(wx.EVT_BUTTON,
            self.m_button10OnButtonClick)
        self.m_button11.Bind(wx.EVT_BUTTON,
            self.m_button11OnButtonClick)
        self.m_button12.Bind(wx.EVT_BUTTON,
            self.m_button12OnButtonClick)
        self.m_button13.Bind(wx.EVT_BUTTON,
            self.m_button13OnButtonClick)
    #
    def __del__(self):
        pass
    # 点击按钮，显示各按钮对应的窗口
    def m_button10OnButtonClick(self, event):
        #
        window=MyFrame21(None)
        window.Show()
    def m_button11OnButtonClick(self, event):
        #
        window=MyFrame23(None)
        window.Show()
    def m_button12OnButtonClick(self, event):
        #
        window=MyFrame25(None)
        window.Show()
    def m_button13OnButtonClick(self, event):
        #
        window=MyFrame27(None)
        window.Show()
#测试代码
if __name__=='__main__':
    app=wx.App()
    window=MyFrame19(None)
    window.Show()
    app.MainLoop()