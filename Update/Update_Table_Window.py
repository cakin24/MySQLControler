# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
from Update_Table import Update_Table
from Check_Database import Check_Database
from Notice import MyFrame3
###########################################################################
## Class MyFrame37
###########################################################################
class MyFrame37(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(571, 459),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer11 = wx.BoxSizer(wx.VERTICAL)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"所有的TABLE",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        self.m_staticText10.SetFont(wx.Font(15, 74, 90, 90, False, "Sans"))
        bSizer12.Add(self.m_staticText10, 0, wx.ALL, 5)
        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(800, 200),
                                       style=wx.TE_READONLY|wx.TE_MULTILINE)
        bSizer12.Add(self.m_textCtrl7, 0, wx.ALL, 5)
        bSizer11.Add(bSizer12, 0, wx.EXPAND, 5)
        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"输入原TABLE",
                                            wx.DefaultPosition, wx.Size(200, 50), 0)
        self.m_staticText11.Wrap(-1)
        bSizer13.Add(self.m_staticText11, 0, wx.ALL, 5)
        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(150, 50), 0)
        bSizer13.Add(self.m_textCtrl8, 0, wx.ALL, 5)
        bSizer11.Add(bSizer13, 0, wx.EXPAND, 5)
        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY,
                                            u"输入修改后的TABLE", wx.DefaultPosition,
                                            wx.Size(200, 50), 0)
        self.m_staticText12.Wrap(-1)
        bSizer14.Add(self.m_staticText12, 0, wx.ALL, 5)
        self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(150, 50), 0)
        bSizer14.Add(self.m_textCtrl10, 0, wx.ALL, 5)
        bSizer11.Add(bSizer14, 0, wx.EXPAND, 5)
        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.Size(220, -1), 0)
        self.m_staticText14.Wrap(-1)
        bSizer15.Add(self.m_staticText14, 0, wx.ALL, 5)
        self.m_button8 = wx.Button(self, wx.ID_ANY, u"确定",
                                   wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer15.Add(self.m_button8, 0, wx.ALL, 5)
        bSizer11.Add(bSizer15, 0, wx.EXPAND, 5)
        self.SetSizer(bSizer11)
        self.Layout()
        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button8.Bind(wx.EVT_BUTTON, self.m_button8OnButtonClick)
        #######################Check_Database###############################
        check_database=Check_Database('show tables')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl7.SetValue(show)
    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class
    def m_button8OnButtonClick(self, event):
        sql="rename table %s to %s"%(self.m_textCtrl8.GetValue(),
                                     self.m_textCtrl10.GetValue())
        update=Update_Table(sql)
        notice=MyFrame3(None)
        notice.Show()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame37(None)
    window.Show()
    app.MainLoop()