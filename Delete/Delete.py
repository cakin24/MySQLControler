# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
from Delete_DataBase import MyFrame13
from Delete_Table import MyFrame15
from Delete_Document import MyFrame17
###########################################################################
## Class MyFrame11
###########################################################################
class MyFrame11(wx.Frame):
    def __init__(self, parent):
        #初始化框架
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(500, 155),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Window类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直布局控制器
        bSizer7 = wx.BoxSizer(wx.VERTICAL)
        #水平布局控制器
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        #空白标签，位于控制器8中
        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY,
                                           wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(100, 50), 0)
        self.m_staticText6.Wrap(-1)
        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)
        #删除DATABASE按钮，位于布局控制器8中
        self.m_button10 = wx.Button(self, wx.ID_ANY, u"删除DATABASE",
                                    wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer8.Add(self.m_button10, 0, wx.ALL, 5)
        #删除TABLE按钮，位于布局控制器8中
        self.m_button11 = wx.Button(self, wx.ID_ANY, u"删除TABLE",
                                    wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer8.Add(self.m_button11, 0, wx.ALL, 5)
        #布局控制器8位于布局控制器7中
        bSizer7.Add(bSizer8, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)
        #空白标签，用于布局控制器9中
        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.Size(100, 50), 0)
        self.m_staticText7.Wrap(-1)
        bSizer9.Add(self.m_staticText7, 0, wx.ALL, 5)
        #删除记录按钮，位于布局控制器9中
        self.m_button12 = wx.Button(self, wx.ID_ANY, u"删除记录",
                                    wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer9.Add(self.m_button12, 0, wx.ALL, 5)
        #退出按钮，位于布局控制器9中
        self.m_button13 = wx.Button(self, wx.ID_ANY, u"退出",
                                    wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer9.Add(self.m_button13, 0, wx.ALL, 5)
        #布局控制器9位于布局控制器7中
        bSizer7.Add(bSizer9, 0, wx.EXPAND, 5)
        #window类的方法
        self.SetSizer(bSizer7)
        self.Layout()
        self.Centre(wx.BOTH)
        # 按钮绑定事件
        self.m_button10.Bind(wx.EVT_BUTTON, self.m_button10OnButtonClick)
        self.m_button11.Bind(wx.EVT_BUTTON, self.m_button11OnButtonClick)
        self.m_button12.Bind(wx.EVT_BUTTON, self.m_button12OnButtonClick)
        self.m_button13.Bind(wx.EVT_BUTTON, self.m_button13OnButtonClick)
    def __del__(self):
        pass
    # 单击各按钮，显示对应窗口
    def m_button10OnButtonClick(self, event):
        window = MyFrame13(None)
        window.Show()
    def m_button11OnButtonClick(self, event):
        window = MyFrame15(None)
        window.Show()
    def m_button12OnButtonClick(self, event):
        window = MyFrame17(None)
        window.Show()
    def m_button13OnButtonClick(self, event):
        exit()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame11(None)
    window.Show()
    app.MainLoop()