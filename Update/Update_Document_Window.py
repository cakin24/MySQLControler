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
from Check_Document import Check_Document
from Check_Desc import Check_Desc
from Save_Document import SaveDocument
from Notice import MyFrame3
###########################################################################
## Class MyFrame39
###########################################################################
class MyFrame39(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(605, 716),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer16 = wx.BoxSizer(wx.VERTICAL)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"所有的表如下：",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer8.Add(self.m_staticText7, 0, wx.ALL, 5)
        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(800, 100),
                                       style=wx.TE_READONLY|wx.TE_MULTILINE)
        bSizer8.Add(self.m_textCtrl6, 0, wx.ALL, 5)
        bSizer16.Add(bSizer8, 0, wx.EXPAND, 5)
        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"请输入想要更新数据的表名",
                                            wx.DefaultPosition, wx.Size(200, 50), 0)
        self.m_staticText20.Wrap(-1)
        bSizer22.Add(self.m_staticText20, 0, wx.ALL, 5)
        self.m_textCtrl16 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer22.Add(self.m_textCtrl16, 0, wx.ALL, 5)
        self.m_button10 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition,
                                    wx.Size(100, 50), 0)
        bSizer22.Add(self.m_button10, 0, wx.ALL, 5)
        bSizer16.Add(bSizer22, 0, wx.EXPAND, 5)
        bSizer17 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"表的数据如下",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        self.m_staticText15.SetFont(wx.Font(13, 74, 90, 90, False, "Sans"))
        bSizer17.Add(self.m_staticText15, 0, wx.ALL, 5)
        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(800, 200),
                                        style=wx.TE_READONLY|wx.TE_MULTILINE)
        bSizer17.Add(self.m_textCtrl12, 0, wx.ALL, 5)
        bSizer16.Add(bSizer17, 0, wx.EXPAND, 5)
        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY,
                                            u"请输入想要更新的数据的唯一条件",
                                            wx.DefaultPosition, wx.Size(230, 50), 0)
        self.m_staticText16.Wrap(-1)
        bSizer18.Add(self.m_staticText16, 0, wx.ALL, 5)
        self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(150, 50), 0)
        bSizer18.Add(self.m_textCtrl13, 0, wx.ALL, 5)
        bSizer16.Add(bSizer18, 0, wx.EXPAND, 5)
        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY,
                                            u"请输入想要更新的的数据的相应字段",
                                            wx.DefaultPosition, wx.Size(230, 50), 0)
        self.m_staticText17.Wrap(-1)
        bSizer19.Add(self.m_staticText17, 0, wx.ALL, 5)
        self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(150, 50), 0)
        bSizer19.Add(self.m_textCtrl14, 0, wx.ALL, 5)
        bSizer16.Add(bSizer19, 0, wx.EXPAND, 5)
        bSizer20 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY,
                                            u"请输入想更新后数据值",
                                            wx.DefaultPosition, wx.Size(230, 50), 0)
        self.m_staticText18.Wrap(-1)
        bSizer20.Add(self.m_staticText18, 0, wx.ALL, 5)
        self.m_textCtrl15 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(150, 50), 0)
        bSizer20.Add(self.m_textCtrl15, 0, wx.ALL, 5)
        bSizer16.Add(bSizer20, 0, wx.EXPAND, 5)
        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_staticText19.Wrap(-1)
        bSizer21.Add(self.m_staticText19, 0, wx.ALL, 5)
        self.m_button9 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition,
                                   wx.Size(100, 50), 0)
        bSizer21.Add(self.m_button9, 0, wx.ALL, 5)
        bSizer16.Add(bSizer21, 0, wx.EXPAND, 5)
        self.SetSizer(bSizer16)
        self.Layout()
        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button10.Bind(wx.EVT_BUTTON, self.m_button10OnButtonClick)
        self.m_button9.Bind(wx.EVT_BUTTON, self.m_button9OnButtonClick)
        ####################Check_Database##########################
        check_database=Check_Database('show tables')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl6.SetValue(show)
    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class
    def m_button10OnButtonClick(self, event):
        table_name=self.m_textCtrl16.GetValue()
        check1=Check_Document(table_name)
        check2=Check_Desc(table_name)
        result=''
        for j in range(0,len(check2.return_result)):
            result+=check2.return_result[j]
        for i in range(0,len(check1.return_result)):
            result+=str(check1.return_result[i])
        self.m_textCtrl12.SetValue(result)
    def m_button9OnButtonClick(self, event):
        TiaoJian=self.m_textCtrl13.GetValue()
        ZiDuan=self.m_textCtrl14.GetValue()
        Values=self.m_textCtrl15.GetValue()
        sql="update %s set %s=%s where %s"%(self.m_textCtrl16.GetValue(),
                                            ZiDuan,Values,TiaoJian)
        save=SaveDocument(sql)
        notice=MyFrame3(None)
        notice.Show()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame39(None)
    window.Show()
    app.MainLoop()