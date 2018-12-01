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
###########################################################################
## Class MyFrame27
###########################################################################
class MyFrame27(wx.Frame):
    def __init__(self, parent):
        #初始化框架
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(692, 523),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Windows类方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直布局控制器
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        #水平布局控制器
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        #表名输入提示框
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"请输入想要查询结构的表名",
                                           wx.DefaultPosition, wx.Size(250, 50), 0)
        self.m_staticText4.Wrap(-1)
        #提示框在布局器7中
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)
        #输入提示框
        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(120, 50), 0)
        #输入提示框在布局器7中
        bSizer7.Add(self.m_textCtrl5, 0, wx.ALL, 5)
        #确认按钮
        self.m_button3 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition,
                                   wx.Size(120, 50), 0)
        #确认按钮在布局7中
        bSizer7.Add(self.m_button3, 0, wx.ALL, 5)
        #布局器7在布局器6中
        bSizer6.Add(bSizer7, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        #用于显示数据表的框，只读，多行，在布局器8中
        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(250, 800),
                                       style=wx.TE_READONLY|wx.TE_MULTILINE)
        bSizer8.Add(self.m_textCtrl6, 0, wx.ALL, 5)
        #用于显示结果，只读，多行，在布局器8中
        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(600, 800),
                                       style=wx.TE_READONLY|wx.TE_MULTILINE)
        bSizer8.Add(self.m_textCtrl7, 0, wx.ALL, 5)
        #布局器8在布局器6中
        bSizer6.Add(bSizer8, 0, wx.EXPAND, 5)
        #Window类属性
        self.SetSizer(bSizer6)
        self.Layout()
        self.Centre(wx.BOTH)
        # 按钮绑定事件
        self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)
        #######################Check_DATABASE#############################
        #获取数据库的数据表
        check_database=Check_Database('show tables')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        #显示数据库的数据表
        self.m_textCtrl6.SetValue(show)
    def __del__(self):
        pass
    # 获得对应数据库的数据表的表描述信息
    def m_button3OnButtonClick(self, event):
        check=Check_Desc(self.m_textCtrl5.GetValue())
        result=''
        for i in range(0,len(check.return_result)):
            result+=(str(check.return_result[i])+'\t')
        self.m_textCtrl7.SetValue(result)

#编入测试模块
if __name__=='__main__':
    app=wx.App()
    window=MyFrame27(None)
    window.Show()
    app.MainLoop()