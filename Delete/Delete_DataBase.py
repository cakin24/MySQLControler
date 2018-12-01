# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
from Notice import MyFrame3
from Check_Database import Check_Database
###########################################################################
## Class MyFrame13
###########################################################################
class MyFrame13(wx.Frame):
    def __init__(self, parent):
        #框架初始化
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(561, 365),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Window类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直以及水平布局控制器
        bSizer10 = wx.BoxSizer(wx.VERTICAL)
        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)
        #文本提示框，位于布局控制器11中
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY,
                                           u"请输入想要删除的DATABASE",
                                           wx.DefaultPosition, wx.Size(200, 50),0)
        self.m_staticText8.Wrap(-1)
        bSizer11.Add(self.m_staticText8, 0, wx.ALL, 5)
        #用户要删除的表，位于布局控制器11中
        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer11.Add(self.m_textCtrl7, 0, wx.ALL, 5)
        #布局控制器11位于布局控制器10中
        bSizer10.Add(bSizer11, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)
        #空白标签，位于布局控制器12中
        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.Size(200, 50), 0)
        self.m_staticText9.Wrap(-1)
        bSizer12.Add(self.m_staticText9, 0, wx.ALL, 5)
        #确定按钮位于布局控制器12中
        self.m_button14 = wx.Button(self, wx.ID_ANY, u"确定",
                                    wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer12.Add(self.m_button14, 0, wx.ALL, 5)
        #布局控制器12位于布局控制器10中
        bSizer10.Add(bSizer12, 0, wx.EXPAND, 5)
        #垂直布局控制器
        bSizer13 = wx.BoxSizer(wx.VERTICAL)
        #要删除的数据库列，多行，只读，位于布局控制器13中
        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(600, 500),
                                       style=wx.TE_READONLY|wx.TE_MULTILINE)
        bSizer13.Add(self.m_textCtrl8, 0, wx.ALL, 5)
        #布局控制器13位于布局控制器10中
        bSizer10.Add(bSizer13, 1, wx.EXPAND, 5)
        #Window类的三个方法
        self.SetSizer(bSizer10)
        self.Layout()
        self.Centre(wx.BOTH)
        # 按钮和事件绑定
        self.m_button14.Bind(wx.EVT_BUTTON, self.m_button14OnButtonClick)
        ##################check_database###############
        #显示数据库列表
        check_database=Check_Database('show databases','1')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl8.SetValue(show)
    def __del__(self):
        pass
    # 删除数据库
    def m_button14OnButtonClick(self, event):
        if(self.m_textCtrl7.GetValue()==''):
            window=MyFrame3(None,'请输入DATABASE!')
            window.Show()
        else:
            sql="drop database %s"%self.m_textCtrl7.GetValue()
            check_database=Check_Database(sql,'1')
            window=MyFrame3(None)
            window.Show()

#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame13(None)
    window.Show()
    app.MainLoop()