import wx
import os
from homepage import *
from paint import *
import wx.html2


class App(wx.App):
	def  OnInit(self):
		self.frame = homepage()
		self.frame.Show(True)
		return True

if __name__ == '__main__':
	app = App()
	app.MainLoop()
