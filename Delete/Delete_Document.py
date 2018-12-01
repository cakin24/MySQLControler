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
from Notice import MyFrame3
from Delete_Document_Fun import Delete_Document_Fun
from Check_Desc import Check_Desc
###########################################################################
## Class MyFrame17
###########################################################################
class MyFrame17(wx.Frame):
    def __init__(self, parent):
        #初始化框架
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(617, 490),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Window类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直布局控制器和水平布局控制器
        bSizer14 = wx.BoxSizer(wx.VERTICAL)
        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)
        #提示信息，位于布局控制器15
        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY,
                                            u"请输入表名查看记录然后再进行删除",
                                            wx.DefaultPosition, wx.Size(-1, 50),0)
        self.m_staticText10.Wrap(-1)
        bSizer15.Add(self.m_staticText10, 0, wx.ALL, 5)
        #输入框位于布局控制器15
        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(150, 50), 0)
        bSizer15.Add(self.m_textCtrl9, 0, wx.ALL, 5)
        #确认按钮位于布局控制器15
        self.m_button15 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition,
                                    wx.Size(100, 50), 0)
        bSizer15.Add(self.m_button15, 0, wx.ALL, 5)
        #布局控制器15位于布局控制器14中
        bSizer14.Add(bSizer15, 0, wx.EXPAND, 5)
        #水平布局控制器16
        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)
        #数据列表，多行，只读，位于布局控制器16
        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(190, 300),
                                       style=wx.TE_MULTILINE|wx.TE_READONLY)
        bSizer16.Add(self.m_textCtrl4, 0, wx.ALL, 5)
        #绑定数据表的记录，位于布局控制器16
        self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(700, 300),
                                        style=wx.TE_MULTILINE|wx.TE_READONLY)
        bSizer16.Add(self.m_textCtrl10, 0, wx.ALL, 5)
        bSizer14.Add(bSizer16, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)
        #提示信息，位于布局控制器17
        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY,
                                            u"请输入需要删除的记录的条件(例如：ＩＤ＝３)",
                                            wx.DefaultPosition,wx.Size(-1, 50), 0)
        self.m_staticText11.Wrap(-1)
        bSizer17.Add(self.m_staticText11, 0, wx.ALL, 5)
        #删除条件，位于布局控制器17
        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(200, 50), 0)
        bSizer17.Add(self.m_textCtrl11, 0, wx.ALL, 5)

        #删除按钮，位于布局控制器17
        self.m_button17 = wx.Button(self, wx.ID_ANY, u"确定删除",
                                    wx.DefaultPosition, wx.Size(120, 50), 0)
        bSizer17.Add(self.m_button17, 0, wx.ALL, 5)
        #bSizer14.Add(bSizer18, 1, wx.EXPAND, 5)
        # 布局控制器17位于布局控制器14中
        bSizer14.Add(bSizer17, 0, wx.EXPAND, 5)
        #Window类的方法
        self.SetSizer(bSizer14)
        self.Layout()
        self.Centre(wx.BOTH)
        # 按钮绑定事件
        self.m_button15.Bind(wx.EVT_BUTTON, self.m_button15OnButtonClick)
        self.m_button17.Bind(wx.EVT_BUTTON, self.m_button17OnButtonClick)
        result=''
        #显示特定数据库的数据表列表
        check_database = Check_Database('show tables')
        for i in range(0, len(check_database.return_result)):
            result+=check_database.return_result[i]
        self.m_textCtrl4.SetValue(result)
    def __del__(self):
        pass
    # 按钮绑定事件
    # 显示表的详细信息
    def m_button15OnButtonClick(self, event):
        if(self.m_textCtrl9.GetValue()!=''):
            check1=Check_Document('%s'%self.m_textCtrl9.GetValue())
            check2=Check_Desc('%s'%self.m_textCtrl9.GetValue())
            print self.m_textCtrl9.GetValue()
            result=''
            for j in range(0,len(check2.return_result)):
                result+=str(check2.return_result[j])
            for i in range(0, len(check1.return_result)):
                result += str(check1.return_result[i])
                result += " "
            self.m_textCtrl10.SetValue(result)
        else:
            window=MyFrame3(None,"请输入TABLE")
            window.Show()
    #删除表数据
    def m_button17OnButtonClick(self, event):
        try:
            sql="delete from %s where %s"%(self.m_textCtrl9.GetValue(),
                                           self.m_textCtrl11.GetValue())
        except:
            window=MyFrame3(None,"请检查条件!")
            window.Show()
        else:
            check=Delete_Document_Fun(sql)
            window=MyFrame3(None)
            window.Show()

#测试
if __name__=='__main__':
    app=wx.App()
    window=MyFrame17(None)
    window.Show()
    app.MainLoop()