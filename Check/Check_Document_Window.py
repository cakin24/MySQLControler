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
###########################################################################
## Class MyFrame25
###########################################################################
class MyFrame25(wx.Frame):
    def __init__(self, parent):
        #框架初始化
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(783, 665),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Window的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直布局控制器
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        #水平布局控制器
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        #输入表名提示框
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"请输入想要查询的表名",
                                           wx.DefaultPosition, wx.Size(250, 50), 0)
        self.m_staticText1.Wrap(-1)
        #设置字体
        self.m_staticText1.SetFont(wx.Font(15, 74, 90, 90, False, "Sans"))
        #提示框位于布局器3中
        bSizer3.Add(self.m_staticText1, 0, wx.ALL, 5)
        #用于输入表名
        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(250, 50), 0)
        #表名编辑框位于布局器3中
        bSizer3.Add(self.m_textCtrl2, 0, wx.ALL, 5)
        #确认按钮
        self.m_button1 = wx.Button(self, wx.ID_ANY, u"确定",
                                   wx.DefaultPosition, wx.Size(100, 50), 0)
        #确认按钮位于布局器3中
        bSizer3.Add(self.m_button1, 0, wx.ALL, 5)
        #布局器3位于布局器2中
        bSizer2.Add(bSizer3, 0, wx.EXPAND, 5)
        #布局器4是水平布局器
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        #表名列表，只读，多行
        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(250, 800),
                                       style=wx.TE_MULTILINE|wx.TE_READONLY)
        #表名列表位于布局器4中
        bSizer4.Add(self.m_textCtrl3, 0, wx.ALL, 5)
        #用于显示结果
        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(800, 800),
                                       style=wx.TE_MULTILINE|wx.TE_READONLY)
        #位于布局器4中
        bSizer4.Add(self.m_textCtrl4, 0, wx.ALL, 5)
        #布局器位于布局器2中
        bSizer2.Add(bSizer4, 1, wx.EXPAND, 5)
        #以下3个方法是Window类的方法
        self.SetSizer(bSizer2)
        self.Layout()
        self.Centre(wx.BOTH)
        # 绑定事件
        self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)
        ################################################
        #检查数据表实例
        check_database=Check_Database('show tables')
        #显示特定数据库的数据表列表
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl3.SetValue(show)
    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class
    def m_button1OnButtonClick(self, event):
        result=''
        #定义数据表结果实例，并显示结果
        check_database = Check_Document('%s'%self.m_textCtrl2.GetValue())
        for i in range(0, len(check_database.return_result)):
            result+=check_database.return_result[i]
        self.m_textCtrl4.SetValue(result)

#编入测试模块
if __name__=='__main__':
    app=wx.App()
    window=MyFrame25(None)
    window.Show()
    app.MainLoop()