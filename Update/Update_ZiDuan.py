# -*- coding: utf-8 -*-
##############################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
##############################################################
import wx
import wx.xrc
from Check_Database import Check_Database
from Check_Desc import Check_Desc
from Save_Document import SaveDocument
from Notice import MyFrame3
#############################################################
## Class MyFrame41
#############################################################
class MyFrame41(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=wx.EmptyString,
                          pos=wx.DefaultPosition,
                          size=wx.Size(560, 521),
                          style=wx.DEFAULT_FRAME_STYLE
                                | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer23 = wx.BoxSizer(wx.VERTICAL)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"所有的表名如下：",
                                           wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetFont(wx.Font(14, 74, 90, 90,
                                           False, "Sans"))
        bSizer7.Add(self.m_staticText5, 0, wx.ALL, 5)
        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY,
                                       wx.EmptyString,
                                       wx.DefaultPosition,
                                       wx.Size(800, 150),
                                       style=wx.TE_MULTILINE
                                             |wx.TE_READONLY)
        bSizer7.Add(self.m_textCtrl5, 0, wx.ALL, 5)
        bSizer23.Add(bSizer7, 0, wx.EXPAND, 5)
        bSizer24 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY,
                                            u"请输入表名查看字段",
                                            wx.DefaultPosition,
                                            wx.Size(200, 50), 0)
        self.m_staticText21.Wrap(-1)
        self.m_staticText21.SetFont(wx.Font(14, 74, 90, 90,
                                            False, "Sans"))
        bSizer24.Add(self.m_staticText21, 0, wx.ALL, 5)
        self.m_textCtrl17 = wx.TextCtrl(self, wx.ID_ANY,
                                        wx.EmptyString,
                                        wx.DefaultPosition,
                                        wx.Size(150, 50), 0)
        bSizer24.Add(self.m_textCtrl17, 0, wx.ALL, 5)
        self.m_button11 = wx.Button(self, wx.ID_ANY, u"确定",
                                    wx.DefaultPosition,
                                    wx.Size(100, 50), 0)
        bSizer24.Add(self.m_button11, 0, wx.ALL, 5)
        bSizer23.Add(bSizer24, 0, wx.EXPAND, 5)
        bSizer25 = wx.BoxSizer(wx.VERTICAL)
        self.m_textCtrl19 = wx.TextCtrl(self, wx.ID_ANY,
                                        wx.EmptyString,
                                        wx.DefaultPosition,
                                        wx.Size(800, 50),
                                        style=wx.TE_MULTILINE
                                              |wx.TE_READONLY)
        bSizer25.Add(self.m_textCtrl19, 0, wx.ALL, 5)
        bSizer23.Add(bSizer25, 0, wx.EXPAND, 5)
        bSizer26 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY,
                                            u"请输入想要更新的字段",
                                            wx.DefaultPosition,
                                            wx.Size(150, 50), 0)
        self.m_staticText22.Wrap(-1)
        bSizer26.Add(self.m_staticText22, 0, wx.ALL, 5)
        self.m_textCtrl20 = wx.TextCtrl(self, wx.ID_ANY,
            wx.EmptyString,wx.DefaultPosition,wx.Size(150, 50), 0)
        bSizer26.Add(self.m_textCtrl20, 0, wx.ALL, 5)
        bSizer23.Add(bSizer26, 0, wx.EXPAND, 5)
        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY,
                    u"请输入更新后字段的名称与数据类型、主键、自增等",
                                            wx.DefaultPosition,
                                            wx.Size(150, 50), 0)
        self.m_staticText23.Wrap(-1)
        bSizer27.Add(self.m_staticText23, 0, wx.ALL, 5)
        self.m_textCtrl21 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition,
                                        wx.Size(300, 50), 0)
        bSizer27.Add(self.m_textCtrl21, 0, wx.ALL, 5)
        bSizer23.Add(bSizer27, 0, wx.EXPAND, 5)
        bSizer28 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY,
                                            wx.EmptyString,
                                            wx.DefaultPosition, wx.Size(200, 50), 0)
        self.m_staticText24.Wrap(-1)
        bSizer28.Add(self.m_staticText24, 0, wx.ALL, 5)
        self.m_button12 = wx.Button(self, wx.ID_ANY, u"确定",
                                    wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer28.Add(self.m_button12, 0, wx.ALL, 5)
        bSizer23.Add(bSizer28, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer23)
        self.Layout()
        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button11.Bind(wx.EVT_BUTTON, self.m_button11OnButtonClick)
        self.m_button12.Bind(wx.EVT_BUTTON, self.m_button12OnButtonClick)
        ####################Check_Database#######################
        check_database=Check_Database('show tables')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl5.SetValue(show)
    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class
    def m_button11OnButtonClick(self, event):
        table_name=self.m_textCtrl17.GetValue()
        check=Check_Desc(table_name)
        result=''
        for i in range(0,len(check.return_result)):
            result+=check.return_result[i]
        self.m_textCtrl19.SetValue(result)
    def m_button12OnButtonClick(self, event):
        sql="alter table %s change %s %s"%(self.m_textCtrl17.GetValue(),
                                           self.m_textCtrl20.GetValue(),
                                           self.m_textCtrl21.GetValue())
        save=SaveDocument(sql)
        notice=MyFrame3(None)
        notice.Show()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame41(None)
    window.Show()
    app.MainLoop()