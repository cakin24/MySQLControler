# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##Main模块
## PLEASE DO "NOT" EDIT THIS FILE!
##本款软件致力于实现原来命令化的MySQL软件界面化
##本款软件主要有“增”，“删”，”改“，”查“四大模块，与命令分类相对应
##本款软件还可以实现查看即操作，免去了原来命令化的软件的重复的返回、查看操作
##同时还保留了命令行传入模块，防止有设计者考虑不周的地方
#########################################################################
import wx
import wx.xrc
#导入写入密码与用户名模块
from CodeInFile import CodeInFile
#导入提示框模块
from Notice import MyFrame3
#导入“增”对应的面板
from Save import MyFrame7
#导入连接模块
from Connect import Connect
#导入用户名、密码、选择数据库模块
from ReadCode import ReadCode
#导入”删“模块
from Delete import MyFrame11
#导入"查"面板
from Check import MyFrame19
#导入传输指令模块之一
from Check_Database import Check_Database
#导入查看表结构模块
from Check_Desc import Check_Desc
#导入“改模块面板”
from Update import MyFrame33
###########################################################################
## Class MyFrame1
###########################################################################
class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(603, 429),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        #软件标题显示，采用大字体
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"                 MySQL管理软件",
                                           wx.DefaultPosition, wx.Size(600, 50), 0)
        self.m_staticText1.Wrap(-1)
        #显示字体设置
        self.m_staticText1.SetFont(wx.Font(30, 70, 90, 90, False, wx.EmptyString))
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)
        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        # 提示输入用户名、密码
        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"请输入用户名和密码",
                                           wx.DefaultPosition, wx.Size(-1, 50), 0)
        self.m_staticText2.Wrap(-1)
        # 显示字体设置
        self.m_staticText2.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))
        bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)
        #输入用户名文本框
        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(150, 50), 0)
        bSizer3.Add(self.m_textCtrl1, 0, wx.ALL, 5)
        #输入密码提示框
        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(150, 50), 0)
        bSizer3.Add(self.m_textCtrl2, 0, wx.ALL, 5)
        #存入按钮
        self.m_button7 = wx.Button(self, wx.ID_ANY, u"存入", wx.DefaultPosition,
                                   wx.Size(100, 50), 0)
        bSizer3.Add(self.m_button7, 0, wx.ALL, 5)
        bSizer1.Add(bSizer3, 0, wx.EXPAND, 5)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        #显示所有数据库，供用户在右侧进行操作
        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(200, 150),
                                       style=wx.TE_MULTILINE | wx.TE_READONLY)
                                       #设置为多行、只读模式可以防止篡改
        bSizer6.Add(self.m_textCtrl4, 0, wx.ALL, 5)
        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        #提示用户输入DATABASE
        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"请输入选择的DTABASE",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        fgSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)
        #用户输入文本框
        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(200, 50), 0)
        fgSizer1.Add(self.m_textCtrl6, 0, wx.ALL, 5)
        #用来隔开文本框，使显示更美观、大方
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString,
                                           wx.DefaultPosition, wx.Size(0, 50), 0)
        self.m_staticText5.Wrap(-1)
        fgSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)
        #确定按钮，绑定数据传入事件
        self.m_button9 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition,
                                   wx.Size(100, 50), 0)
        fgSizer1.Add(self.m_button9, 0, wx.ALL, 5)
        bSizer6.Add(fgSizer1, 0, wx.EXPAND, 5)
        bSizer1.Add(bSizer6, 0, wx.EXPAND, 5)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        #ＳＱＬ语句传入文本框
        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(450, 50), 0)
        bSizer4.Add(self.m_textCtrl3, 0, wx.ALL, 5)
        #ＳＱＬ语句确定传入按钮
        self.m_button1 = wx.Button(self, wx.ID_ANY, u"SQl语句传入",
                                   wx.DefaultPosition, wx.Size(100, 50), 0)
        bSizer4.Add(self.m_button1, 0, wx.ALL, 5)
        bSizer1.Add(bSizer4, 0, wx.EXPAND, 5)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        #用来开启“增”模块
        self.m_button2 = wx.Button(self, wx.ID_ANY, u"增",
                                   wx.DefaultPosition, wx.Size(110, 50), 0)
        bSizer5.Add(self.m_button2, 0, wx.ALL, 5)
        #用来开启”删“
        self.m_button3 = wx.Button(self, wx.ID_ANY, u"删",
                                   wx.DefaultPosition, wx.Size(110, 50), 0)
        bSizer5.Add(self.m_button3, 0, wx.ALL, 5)
        #用来开启”改“模块
        self.m_button4 = wx.Button(self, wx.ID_ANY, u"改",
                                   wx.DefaultPosition, wx.Size(110, 50), 0)
        bSizer5.Add(self.m_button4, 0, wx.ALL, 5)
        #用来开启”查“模块
        self.m_button5 = wx.Button(self, wx.ID_ANY, u"查",
                                   wx.DefaultPosition, wx.Size(110, 50), 0)
        bSizer5.Add(self.m_button5, 0, wx.ALL, 5)
        #用来退出程序
        self.m_button6 = wx.Button(self, wx.ID_ANY, u"退出",
                                   wx.DefaultPosition, wx.Size(110, 50), 0)
        bSizer5.Add(self.m_button6, 0, wx.ALL, 5)
        bSizer1.Add(bSizer5, 0, wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        # Connect Events
        #给各个按钮绑定相应事件，完成不同功能
        self.m_button7.Bind(wx.EVT_BUTTON, self.m_button7OnButtonClick)
        self.m_button9.Bind(wx.EVT_BUTTON, self.m_button9OnButtonClick)
        self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)
        self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
        self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)
        self.m_button4.Bind(wx.EVT_BUTTON, self.m_button4OnButtonClick)
        self.m_button5.Bind(wx.EVT_BUTTON, self.m_button5OnButtonClick)
        self.m_button6.Bind(wx.EVT_BUTTON, self.m_button6OnButtonClick)
        #####################check_database##########################
        #用来在文本框self.m_textCtr4中显示所有的数据库
        check_database=Check_Database('show databases','1')
        show=''
        for i in range(0,len(check_database.return_result)):
            show+=check_database.return_result[i]
        self.m_textCtrl4.SetValue(show)
    #析构函数
    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class
    def m_button7OnButtonClick(self, event):
        #得到文本框中输入的姓名
        name=self.m_textCtrl1.GetValue()
        #得到文本框中输入的密码
        code=self.m_textCtrl2.GetValue()
        #得到文本框中输入的数据库名称
        database=self.m_textCtrl6.GetValue()
        #将用户名、密码、用户选择的数据库写入
        codeInFile=CodeInFile(name,code,database)
        #显示操作提示框
        #MyFrame中默认提示”Success!“
        window=MyFrame3(None)
        window.Show()
        #将传入完成后的文本框清空，方便下次输入
        self.m_textCtrl1.SetValue('')
        self.m_textCtrl2.SetValue('')
    def m_button9OnButtonClick(self, event):
        #从文件中读取用户名、密码、数据库名称
        readcode=ReadCode()
        Line=readcode.return_line()
        #检测文本框中是否输入DATABASE
        if(self.m_textCtrl6.GetValue()):
            try:
                #将非空的文本框内容传入文件并存储
                codeinfile=CodeInFile(Line[0],Line[1],self.m_textCtrl6.GetValue())
            except:
                #如果不成功则提示用户重试
                window=MyFrame3(None,'请检查用户名和密码是否输入！')
                window.Show()
            else:
                #成功则提示成功提示框
                window=MyFrame3(None)
                window.Show()
                #将数据输入文本框清空，方便下次输入
                self.m_textCtrl6.SetValue("")
        else:
            #如果没有输入会提示用户输入
            window=MyFrame3(None,"请检查DATABASE是否输入！")
            window.Show()
    def m_button1OnButtonClick(self, event):
        #SQL语句传入模块是这个系统的一大亮点，方便不同层次、使用习惯的用户
        #检测”SELECT“是否存在于输入的语句中
        if('select' not in self.m_textCtrl3.GetValue().split()):
            #如果不存在则继续
            while True:
                try:
                    #尝试读取文件中的数据库名称
                    readcode=ReadCode()
                    database=readcode.return_line()[2]
                except:
                    #如果文件中不存在数据库则提示用户返回重新输入
                    window=MyFrame3(None,'请检查是否事先输入DATABASE!')
                    window.Show()
                else:
                    try:
                        #用SQL语句开始操作数据库
                        connect=Connect(database,self.m_textCtrl3.GetValue())
                    except:
                        #失败则输出提示
                        window=MyFrame3(None,"失败！")
                        window.Show()
                    else:
                        #否则显示传入成功
                        window=MyFrame3(None)
                        window.Show()
                        #如果成功就将文本框清空
                        self.m_textCtrl3.SetValue('')
                        #终端输入循环
                        break
        else:
            #如果传入的语句中包含查询关键字，那么就要调用显示框显示查询数据
            result=''
            #准备SQL语句
            sql='%s'%self.m_textCtrl3.GetValue()
            #将SQL语句传入
            #Check_Database默认是不传数据库进入的，但是可以选择是否传入
            #如果不传入则使用文件中的数据库名称
            check_database=Check_Database(sql)
            #对返回结果进行字符化处理
            for i in range(0,len(check_database.return_result)):
                result+=check_database.return_result[i]
            #显示成功提示框
            window=MyFrame3(None,result)
            window.Show()
    def m_button2OnButtonClick(self, event):
        #显示增加面板
        window=MyFrame7(None)
        window.Show()
    def m_button3OnButtonClick(self, event):
        #显示删除面板
        window=MyFrame11(None)
        window.Show()
    def m_button4OnButtonClick(self, event):
        #显示修改面板
        window=MyFrame33(None)
        window.Show()
    def m_button5OnButtonClick(self, event):
        #显示查询面板
        window=MyFrame19(None)
        window.Show()
    def m_button6OnButtonClick(self, event):
        #退出程序运行
        exit()
#编入测试模块
if __name__=='__main__':
    app=wx.App()
    window=MyFrame1(None)
    window.Show()
    app.MainLoop()