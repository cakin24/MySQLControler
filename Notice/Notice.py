# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
###########################################################################
## Class MyFrame3
###########################################################################
#继承wx.Frame类
class MyFrame3(wx.Frame):
    def __init__(self, parent,word='Success!'):
        '''
        parent:窗口的父类。如果“None”被选择的对象是在顶层窗口。
        id:窗口标识。通常-1为了让标识符自动生成.
        title:标题出现在标题栏
        pos:Frame的开始位置。wxDefaultPosition是由操作系统决定.
        size:窗口的尺寸。 wxDefaultSize 是由操作系统决定
        style:窗口的外观按样式风格常数控制.
        参考：https://www.yiibai.com/wxpython/wx_frame_class.html

        '''
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                          pos=wx.DefaultPosition,size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #Window 类的方法
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        '''
        布局管理器，这里表示控件垂直布局
        参考：https://blog.csdn.net/igolang/article/details/9397175
        '''
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        '''
        wx.TextCtrl显示文本和编辑的控制。
        构造函数参数同wx.Frame构造函数参数

        '''
        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.Size(500, 400),
                                       style=wx.TE_READONLY | wx.TE_MULTILINE)
        #将m_textCtrl4添加到布局管理器中
        bSizer6.Add(self.m_textCtrl4, 0, wx.ALL, 5)
        #下面3个都是Windows类的方法
        self.SetSizer(bSizer6)
        self.Layout()
        self.Centre(wx.BOTH)
        #给控件设置显示的值
        self.m_textCtrl4.SetValue('%s'%word)
    def __del__(self):
        pass
if __name__=='__main__':
    app=wx.App()
    window=MyFrame3(None)
    window.Show()
    app.MainLoop()