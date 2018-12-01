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
from Check_Desc import Check_Desc
from Save_Document import SaveDocument
from Notice import MyFrame3
###########################################################################
## Class MyFrame31
###########################################################################
class MyFrame31(wx.Frame):
    def __init__(self, parent):
        #初始化框架
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(652, 585),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Windows类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直布局管理器
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        #提示信息，位于布局控制器3
        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"所有的表如下",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(22, 74, 90, 90, False, "Sans"))
        bSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)
        #用于存放特定数据库的表，位于布局控制器3
        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(800, 100),
                                       style=wx.TE_MULTILINE|wx.TE_READONLY)
        bSizer3.Add(self.m_textCtrl3, 0, wx.ALL, 5)
        #布局控制器位于布局控制器1
        bSizer1.Add(bSizer3, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        #提示信息，位于布局控制器2
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"请输入想要输入数据的表名",
                                           wx.DefaultPosition, wx.Size(200, 50), 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)
        #要输入的表名，位于布局控制器2
        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(200, 50), 0)
        bSizer2.Add(self.m_textCtrl2, 0, wx.ALL, 5)
        #确定按钮，位于布局控制器2
        self.m_button1 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition
                                   , wx.Size(100, 50), 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)
        #布局控制器2位于布局控制1
        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)
        #垂直布局控制器
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        #表的自段信息提示
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"表中所有字段如下",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer4.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(800, 50),
                                       style=wx.TE_MULTILINE|wx.TE_READONLY)
        bSizer4.Add(self.m_textCtrl4, 0, wx.ALL, 5)
        bSizer1.Add(bSizer4, 0, wx.EXPAND, 5)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"请输入想要存入的字段名（用“,”隔开）",
                                           wx.DefaultPosition, wx.DefaultSize,0)
        self.m_staticText5.Wrap(-1)
        bSizer5.Add(self.m_staticText5, 0, wx.ALL, 5)
        # 要存的字段名
        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(800, 50), 0)
        bSizer5.Add(self.m_textCtrl5, 0, wx.ALL, 5)
        bSizer1.Add(bSizer5, 0, wx.EXPAND, 5)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"请输入想要存入的字段的VALUES",
                                           wx.DefaultPosition, wx.Size(-1, -1),0)
        self.m_staticText6.Wrap(-1)
        bSizer6.Add(self.m_staticText6, 0, wx.ALL, 5)
        # 要存字段名的值
        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(800, 50), 0)
        bSizer6.Add(self.m_textCtrl6, 0, wx.ALL, 5)
        bSizer1.Add(bSizer6, 0, wx.EXPAND, 5)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.Size(240, 50), 0)
        self.m_staticText7.Wrap(-1)
        bSizer7.Add(self.m_staticText7, 0, wx.ALL, 5)
        self.m_button2 = wx.Button(self, wx.ID_ANY, u"确定",
                                   wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer7.Add(self.m_button2, 0, wx.ALL, 5)
        bSizer1.Add(bSizer7, 0, wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        # 按钮绑定事件
        self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)
        self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
        #################################################################
        #显示数据表
        check_database=Check_Database('show tables')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl3.SetValue(show)
    def __del__(self):
        pass
    # 表结构
    def m_button1OnButtonClick(self, event):
        table_name=self.m_textCtrl2.GetValue()
        desc=Check_Desc(table_name)
        result=''
        for i in range(0,len(desc.return_result)):
            result+=desc.return_result[i]
        self.m_textCtrl4.SetValue('%s'%result)
    def m_button2OnButtonClick(self, event):
        #获取字段
        insert_ziduan = self.m_textCtrl5.GetValue()
        #获得数据
        insert_values=self.m_textCtrl6.GetValue()
        sql="insert into %s(%s) VALUES(%s);"%(self.m_textCtrl2.GetValue(),
                                             insert_ziduan,insert_values)
        print sql
        save_document=SaveDocument(sql)
        notice=MyFrame3(None)
        notice.Show()
#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame31(None)
    window.Show()
    app.MainLoop()