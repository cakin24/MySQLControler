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
from Notice import MyFrame3
###########################################################################
## Class MyFrame15
###########################################################################
class MyFrame15(wx.Frame):
    def __init__(self, parent):
        #初始化框架
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(561, 365),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #window的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直布局控制器
        bSizer10 = wx.BoxSizer(wx.VERTICAL)
        #水平布局控制器
        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)
        #提示输入数据表，位于布局控制器11中
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY,
                                           u"请输入想要删除的TABLE",
                                           wx.DefaultPosition, wx.Size(200, 50),0)
        self.m_staticText8.Wrap(-1)
        bSizer11.Add(self.m_staticText8, 0, wx.ALL, 5)
        #数据表输入框，位于布局控制器11中
        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY,
                                       wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(120, 50), 0)
        bSizer11.Add(self.m_textCtrl7, 0, wx.ALL, 5)
        #布局控制器11位于布局控制器10中
        bSizer10.Add(bSizer11, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)
        #空白框位于布局控制器12
        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY,
                                           wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(200, 50), 0)
        self.m_staticText9.Wrap(-1)
        bSizer12.Add(self.m_staticText9, 0, wx.ALL, 5)
        #确认按钮位于布局控制器12中
        self.m_button14 = wx.Button(self, wx.ID_ANY, u"确定",
                                    wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer12.Add(self.m_button14, 0, wx.ALL, 5)
        #布局控制器12位于布局控制器10中
        bSizer10.Add(bSizer12, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer13 = wx.BoxSizer(wx.VERTICAL)
        #数据表列表，只读，多行，位于布局控制器13中
        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(600, 500),
                                       style=wx.TE_READONLY|wx.TE_MULTILINE)
        bSizer13.Add(self.m_textCtrl8, 0, wx.ALL, 5)
        #布局控制器13位于布局控制器10中
        bSizer10.Add(bSizer13, 1, wx.EXPAND, 5)
        #window类的方法
        self.SetSizer(bSizer10)
        self.Layout()
        self.Centre(wx.BOTH)
        # 按钮绑定事件
        self.m_button14.Bind(wx.EVT_BUTTON, self.m_button14OnButtonClick)
        ######################Check_Database##############################
        #列表显示数据表
        check_database=Check_Database('show tables')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl8.SetValue(show)
    def __del__(self):
        pass
    # 控件绑定的事件
    def m_button14OnButtonClick(self, event):
        sql="drop table %s"%self.m_textCtrl7.GetValue()
        check=Check_Database(sql)
        window=MyFrame3(None)
        window.Show()

#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame15(None)
    window.Show()
    app.MainLoop()