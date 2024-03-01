import wx
from paint import *

class homepage(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='ETeach', size=(700, 500),name='Homepage',style=541072960)
		self.Homepage = wx.Panel(self)
		self.Homepage.SetOwnBackgroundColour((255, 255, 255, 255))
		self.Centre()
		self.header = wx.StaticText(self.Homepage,size=(700, 40),pos=(0, 0),label='ETeach - 首页',name='staticText',style=2321)
		header_字体 = wx.Font(20,74,90,400,False,'Microsoft YaHei UI',28)
		self.header.SetFont(header_字体)
		self.header.SetForegroundColour((255, 255, 255, 255))
		self.header.SetOwnBackgroundColour((12, 199, 12, 255))
		self.ToPaint = wx.Button(self.Homepage,size=(120, 80),pos=(0, 40),label='白板',name='ToPaint')
		ToPaint_字体 = wx.Font(16,74,90,400,False,'Microsoft YaHei UI',28)
		self.ToPaint.SetFont(ToPaint_字体)
		self.ToPaint.Bind(wx.EVT_BUTTON,self.ToPaint_按钮被单击)
		self.SpaceSim = wx.Button(self.Homepage,size=(120, 80),pos=(0, 120),label='太空模拟',name='button')
		SpaceSim_字体 = wx.Font(16,74,90,400,False,'Microsoft YaHei UI',28)
		self.SpaceSim.SetFont(SpaceSim_字体)
		self.SpaceSim.Bind(wx.EVT_BUTTON,self.SpaceSim_按钮被单击)


	def ToPaint_按钮被单击(self,event):
		self.frame = SketchFrame()
		self.frame.Show(True)
		SketchFrame.Show(True)


	def SpaceSim_按钮被单击(self,event):
		exec(open("space.py", encoding='utf-8', errors='ignore').read())
