# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
from Update_Table_Window import MyFrame37
from Update_Document_Window import MyFrame39
from Update_ZiDuan import MyFrame41
###########################################################################
## Class MyFrame33
###########################################################################
class MyFrame33(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(536, 151),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY,
                                           wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(130, 50), 0)
        self.m_staticText8.Wrap(-1)
        bSizer9.Add(self.m_staticText8, 0, wx.ALL, 5)
        self.m_button3 = wx.Button(self, wx.ID_ANY, u"更新TABLE名称",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer9.Add(self.m_button3, 0, wx.ALL, 5)
        self.m_button4 = wx.Button(self, wx.ID_ANY, u"更新数据",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer9.Add(self.m_button4, 0, wx.ALL, 5)
        bSizer8.Add(bSizer9, 0, wx.EXPAND, 5)
        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.Size(130, 50), 0)
        self.m_staticText9.Wrap(-1)
        bSizer10.Add(self.m_staticText9, 0, wx.ALL, 5)
        self.m_button5 = wx.Button(self, wx.ID_ANY, u"更新TABLE字段",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer10.Add(self.m_button5, 0, wx.ALL, 5)
        self.m_button6 = wx.Button(self, wx.ID_ANY, u"退出",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer10.Add(self.m_button6, 0, wx.ALL, 5)
        bSizer8.Add(bSizer10, 0, wx.EXPAND, 5)
        self.SetSizer(bSizer8)
        self.Layout()
        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)
        self.m_button4.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)
        self.m_button5.Bind(wx.EVT_BUTTON, self.m_button5OnButtonClick)
        self.m_button6.Bind(wx.EVT_BUTTON, self.m_button6OnButtonClick)
    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class
    def m_button3OnButtonClick(self, event):
        window = MyFrame37(None)
        window.Show()
    def m_button4OnButtonClick(self, event):
        window = MyFrame39(None)
        window.Show()
    def m_button5OnButtonClick(self, event):
        window = MyFrame41(None)
        window.Show()
    def m_button6OnButtonClick(self, event):
        exit()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame33(None)
    window.Show()
    app.MainLoop()