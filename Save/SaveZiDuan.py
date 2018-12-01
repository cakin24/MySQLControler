# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
from CreateTable import CreateTable
from Notice import MyFrame3
###########################################################################
## Class MyFrame5
###########################################################################
class MyFrame5(wx.Frame):
    def __init__(self, parent):
        #框架初始化
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(763, 477),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Window类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        #垂直和水平布局控制器
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        #提示信息，位于布局控制器2
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY,
                                           u"请输入第一个字段和数据类型",
                                           wx.DefaultPosition, wx.Size(130, 50), 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)
        #第一个字段的名称，位于布局控制器2
        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(130, 50), 0)
        bSizer2.Add(self.m_textCtrl1, 0, wx.ALL, 5)
        #第一个字段的类型，位于布局控制器2
        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer2.Add(self.m_textCtrl7, 0, wx.ALL, 5)
        #主键复选框，位于布局控制器2
        self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, u"PRIMARY KEY",
                                       wx.DefaultPosition, wx.Size(130, 50), 0)
        bSizer2.Add(self.m_checkBox1, 0, wx.ALL, 5)
        #自增复选框，位于布局控制器2
        self.m_checkBox2 = wx.CheckBox(self, wx.ID_ANY, u"AUTO_INCREMENT",
                                       wx.DefaultPosition, wx.Size(-1, 50), 0)
        bSizer2.Add(self.m_checkBox2, 0, wx.ALL, 5)
        #布局控制器2位于布局控制器1
        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)
        #水平布局控制器
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        #提示信息，位于布局控制器3
        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"请输入第二个字段和数据类型",
                                           wx.DefaultPosition, wx.Size(130, 50), 0)
        self.m_staticText2.Wrap(-1)
        bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)
        #第2个字段名称，位于布局控制器3
        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(130, 50), 0)
        bSizer3.Add(self.m_textCtrl2, 0, wx.ALL, 5)
        #第2个字段的类型，位于布局控制器3
        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer3.Add(self.m_textCtrl8, 0, wx.ALL, 5)
        #选择列表，主键或自增量，位于布局控制器3
        m_comboBox3Choices = [u"PRIMARY KEY", u"AUTO_INCREMENT"]
        self.m_comboBox3 = wx.ComboBox(self, wx.ID_ANY, u"主键、自增",
                                       wx.DefaultPosition, wx.Size(130, 50),
                                       m_comboBox3Choices, 0)
        bSizer3.Add(self.m_comboBox3, 0, wx.ALL, 5)
        #控制器3位于控制器1
        bSizer1.Add(bSizer3, 0, wx.EXPAND, 5)
        #第3个字段
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY,
                                           u"请输入第三个字段和数据类型",
                                           wx.DefaultPosition, wx.Size(130, 50), 0)
        self.m_staticText3.Wrap(-1)
        bSizer4.Add(self.m_staticText3, 0, wx.ALL, 5)
        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(130, 50), 0)
        bSizer4.Add(self.m_textCtrl3, 0, wx.ALL, 5)
        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer4.Add(self.m_textCtrl9, 0, wx.ALL, 5)
        bSizer1.Add(bSizer4, 0, wx.EXPAND, 5)
        #第4个字段
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY,
                                           u"请输入第四个字段和数据类型",
                                           wx.DefaultPosition, wx.Size(130, 50), 0)
        self.m_staticText4.Wrap(-1)
        bSizer5.Add(self.m_staticText4, 0, wx.ALL, 5)
        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(130, 50), 0)
        bSizer5.Add(self.m_textCtrl4, 0, wx.ALL, 5)
        self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer5.Add(self.m_textCtrl10, 0, wx.ALL, 5)
        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY,
                                           u"如果字段数量或者关键字不匹配请使用首页的SQL语句传入",
                                           wx.DefaultPosition, wx.Size(300, 50), 0)
        self.m_staticText9.Wrap(-1)
        self.m_staticText9.SetFont(wx.Font(13, 74, 90, 90, False, "Sans"))
        bSizer5.Add(self.m_staticText9, 0, wx.ALL, 5)
        bSizer1.Add(bSizer5, 0, wx.EXPAND, 5)
        #第5个字段
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY,
                                           u"请输入第五个字段和数据类型",
                                           wx.DefaultPosition, wx.Size(130, 50), 0)
        self.m_staticText5.Wrap(-1)
        bSizer6.Add(self.m_staticText5, 0, wx.ALL, 5)
        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(130, 50), 0)
        bSizer6.Add(self.m_textCtrl5, 0, wx.ALL, 5)
        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer6.Add(self.m_textCtrl11, 0, wx.ALL, 5)
        bSizer1.Add(bSizer6, 0, wx.EXPAND, 5)
        #表名
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"请输入表名",
                                           wx.DefaultPosition, wx.Size(130, 50), 0)
        self.m_staticText7.Wrap(-1)
        bSizer7.Add(self.m_staticText7, 0, wx.ALL, 5)
        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(130, 50), 0)
        bSizer7.Add(self.m_textCtrl6, 0, wx.ALL, 5)
        bSizer1.Add(bSizer7, 0, wx.EXPAND, 5)
        #空白标签
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.Size(300, 50), 0)
        self.m_staticText8.Wrap(-1)
        bSizer8.Add(self.m_staticText8, 0, wx.ALL, 5)
        #确认按钮
        self.m_button2 = wx.Button(self, wx.ID_ANY, u"确定",
                                   wx.DefaultPosition, wx.Size(130, 50), 0)
        bSizer8.Add(self.m_button2, 0, wx.ALL, 5)
        bSizer1.Add(bSizer8, 1, wx.EXPAND, 5)
        #Window类的方法
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        # 控件和事件绑定
        self.m_checkBox1.Bind(wx.EVT_CHECKBOX, self.m_checkBox1OnCheckBox)
        self.m_checkBox2.Bind(wx.EVT_CHECKBOX, self.m_checkBox2OnCheckBox)
        self.m_comboBox3.Bind(wx.EVT_COMBOBOX, self.m_comboBox3OnCombobox)
        self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
        ##################################
        #主键复选框选择次数
        self.count1=0
        #自增量复选框选择次数
        self.count2=0

        self.check_box1=''
        self.check_box2 = ''
        self.combo_box=''
    def __del__(self):
        pass
    # 当选择为奇数时，表示选择上，否则表示未选择上
    def m_checkBox1OnCheckBox(self, event):
        self.count1+=1
        if(self.count1%2==1):
            self.check_box1 = 'PRIMARY KEY'
        else:
            self.check_box1 = ''

    # 当选择为奇数时，表示选择上，否则表示未选择上
    def m_checkBox2OnCheckBox(self, event):
        self.count2+=1
        if(self.count2%2==1):
            self.check_box2 = 'AUTO_INCREMENT'
        else:
            self.check_box2 = ''
    # 获取列表选择框的值
    def m_comboBox3OnCombobox(self, event):
        self.combo_box = self.m_comboBox3.GetValue()
    '''
    分6种情况来创建表
    '''
    def m_button2OnButtonClick(self, event):
        if(self.m_textCtrl1.GetValue()!='' and self.m_textCtrl2.GetValue()!=''
           and self.m_textCtrl3.GetValue()!='' and self.m_textCtrl4.GetValue()!=''
           and self.m_textCtrl5.GetValue()!=''):
            sql = "create table %s(%s %s %s %s,%s %s %s,%s %s,%s %s,%s %s);" \
                  % (self.m_textCtrl6.GetValue(),
                    self.m_textCtrl1.GetValue(),self.m_textCtrl7.GetValue(),
                     self.check_box1,self.check_box2,
                   self.m_textCtrl2.GetValue(),self.m_textCtrl8.GetValue(),self.combo_box,
                   self.m_textCtrl3.GetValue(),self.m_textCtrl9.GetValue(),
                   self.m_textCtrl4.GetValue(),self.m_textCtrl10.GetValue(),
                   self.m_textCtrl5.GetValue(),self.m_textCtrl11.GetValue()
                   )
            create=CreateTable(sql)
            notice=MyFrame3(None)
            notice.Show()
        elif(self.m_textCtrl1.GetValue()!='' and self.m_textCtrl2.GetValue()!=''
             and self.m_textCtrl3.GetValue()!='' and self.m_textCtrl4.GetValue()!=''):
            sql = "create table %s(%s %s %s %s,%s %s %s,%s %s,%s %s);" \
                  % (self.m_textCtrl6.GetValue(),
                   self.m_textCtrl1.GetValue(),self.m_textCtrl7.GetValue(),self.check_box1,
                     self.check_box2,
                   self.m_textCtrl2.GetValue(),self.m_textCtrl8.GetValue(),self.combo_box,
                   self.m_textCtrl3.GetValue(),self.m_textCtrl9.GetValue(),
                   self.m_textCtrl4.GetValue(),self.m_textCtrl10.GetValue()
                   )
            create=CreateTable(sql)
            notice=MyFrame3(None)
            notice.Show()
        elif(self.m_textCtrl1.GetValue()!='' and self.m_textCtrl2.GetValue()!=''
             and self.m_textCtrl3.GetValue()!=''):
            sql = "create table %s(%s %s %s %s,%s %s %s,%s %s);" \
                  % (self.m_textCtrl6.GetValue(),
                    self.m_textCtrl1.GetValue(),self.m_textCtrl7.GetValue(),self.check_box1,
                     self.check_box2,
                    self.m_textCtrl2.GetValue(),self.m_textCtrl8.GetValue(),self.combo_box,
                    self.m_textCtrl3.GetValue(),self.m_textCtrl9.GetValue()
                       )
            create=CreateTable(sql)
            notice=MyFrame3(None)
            notice.Show()

        elif(self.m_textCtrl1.GetValue()!='' and self.m_textCtrl2.GetValue()!=''):
            sql = "create table %s(%s %s %s %s,%s %s %s);" \
                  % (self.m_textCtrl6.GetValue(),
                    self.m_textCtrl1.GetValue(),self.m_textCtrl7.GetValue(),self.check_box1,
                     self.check_box2,
                    self.m_textCtrl2.GetValue(),self.m_textCtrl8.GetValue(),self.combo_box
                    )
            create=CreateTable(sql)
            notice=MyFrame3(None)
            notice.Show()

        elif(self.m_textCtrl1.GetValue()!=''):
            sql = "create table %s(%s %s %s %s);" \
                  % (self.m_textCtrl6.GetValue(),
                    self.m_textCtrl1.GetValue(),self.m_textCtrl7.GetValue(),
                     self.check_box1,self.check_box2
                    )
            create=CreateTable(sql)
            notice=MyFrame3(None)
            notice.Show()

        elif(not (self.m_textCtrl1.GetValue()!='' and self.m_textCtrl2.GetValue()!=''
                  and self.m_textCtrl3.GetValue()!='' and self.m_textCtrl4.GetValue()!=''
                  and self.m_textCtrl5.GetValue()!='')):
            notice = MyFrame3(None,"请检查是否输入了字段！")
            notice.Show()
if __name__=='__main__':
    app=wx.App()
    window=MyFrame5(None)
    window.Show()
    app.MainLoop()