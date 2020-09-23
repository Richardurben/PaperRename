# -*- coding:utf-8 -*-
#依赖库PyPDF2和wxpython
#原文排版出现的格式，特殊符号会影响题目转化
import os
import PyPDF2
import wx
import sys

class Rename_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'PDF File Rename', size=(400, 350))
        panel = wx.Panel(self, -1)

        self.Text1 = wx.StaticText(panel, label=u'Folder address ', pos=(13, 80), size=(100, 60))
        self.TextCtrl1 = wx.TextCtrl(panel, pos=(107, 80), size=(250, 25))

        self.Button1 = wx.Button(panel, -1, u'START', pos=(90, 200), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.begin_click, self.Button1)

        self.Button2 = wx.Button(panel, -1, u'CANCEL', pos=(205, 200), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.cancel_click, self.Button2)

    def begin_click(self, event):
        folder_address = self.TextCtrl1.GetValue()
        abs_address = os.path.abspath(folder_address)
        for file_name in os.listdir(folder_address):
            file_list = [os.path.join(abs_address, index) for index in os.listdir(abs_address) if index.endswith('.pdf')]
        for file_name in file_list:       #将路径改为双\\形式，才能使用open()打开
            target_pdf = open(file_name, 'rb')
            try:
                pdf_title = PyPDF2.PdfFileReader(target_pdf).getDocumentInfo().title + '.pdf'
                pdf_title=os.path.join(abs_address, pdf_title)
            except:
                print("不能转化为绝对路径")
                pdf_title = '0_' + file_name
            print("原题目转化为绝对路径格式：",pdf_title)
            target_pdf.close()
            try:
                os.rename(file_name, pdf_title)
            except:
                print(file_name,pdf_title,"格式错误等问题",sep="\n")
        self.Destroy()
        sys.exit()

    def cancel_click(self, event):
        self.Destroy()
        sys.exit()

def main():
    app = wx.App()
    win = Rename_Frame()

    win.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()