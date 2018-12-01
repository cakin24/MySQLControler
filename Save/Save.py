# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
from SaveZiDuan import MyFrame5
from SaveDataBase import MyFrame9
from SaveDocument_Window import MyFrame31
###########################################################################
## Class MyFrame7
###########################################################################
class MyFrame7(wx.Frame):
    def __init__(self, parent):
        #框架初始化
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(477, 141),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Windows类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直和水平布局控制器
        bSizer7 = wx.BoxSizer(wx.VERTICAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        #空白标签，位于布局控制器8
        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.Size(100, 50), 0)
        self.m_staticText6.Wrap(-1)
        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)
        #增加DATABASE按钮，位于布局控制器8
        self.m_button2 = wx.Button(self, wx.ID_ANY, u"增加DATABASE",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer8.Add(self.m_button2, 0, wx.ALL, 5)
        #添加TABLE按钮，位于布局控制器8
        self.m_button3 = wx.Button(self, wx.ID_ANY, u"增加TABLE",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer8.Add(self.m_button3, 0, wx.ALL, 5)
        #布局控制器8位于布局控制器7
        bSizer7.Add(bSizer8, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)
        #空白标签位于布局控制器9
        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.Size(100, 50), 0)
        self.m_staticText7.Wrap(-1)
        bSizer9.Add(self.m_staticText7, 0, wx.ALL, 5)
        #增加数据位于布局控制器9
        self.m_button4 = wx.Button(self, wx.ID_ANY, u"增加数据",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer9.Add(self.m_button4, 0, wx.ALL, 5)
        #退出，位于布局控制器9
        self.m_button5 = wx.Button(self, wx.ID_ANY, u"退出",
                                   wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer9.Add(self.m_button5, 0, wx.ALL, 5)
        #布局控制器9位于布局控制器7上
        bSizer7.Add(bSizer9, 0, wx.EXPAND, 5)
        #Window类的方法
        self.SetSizer(bSizer7)
        self.Layout()
        self.Centre(wx.BOTH)
        # 按钮绑定事件
        self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
        self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)
        self.m_button4.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)
        self.m_button5.Bind(wx.EVT_BUTTON, self.m_button5OnButtonClick)
    def __del__(self):
        pass
    # 点击按钮，弹出对应的窗口
    def m_button2OnButtonClick(self, event):
        window=MyFrame9(None)
        window.Show()
    def m_button3OnButtonClick(self, event):
        window=MyFrame5(None)
        window.Show()
    def m_button4OnButtonClick(self, event):
        window=MyFrame31(None)
        window.Show()
    def m_button5OnButtonClick(self, event):
        exit()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame7(None)
    window.Show()
    app.MainLoop()