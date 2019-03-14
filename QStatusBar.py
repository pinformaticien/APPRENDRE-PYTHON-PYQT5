import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar

class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		super(Window, self).__init__()

		self.title = "QStatus Bar"
		self.top = 200
		self.left = 200
		self.width = 600
		self.height = 500

		self.setWindowIcon(QtGui.QIcon("icon.png"))

		self.InitUI()

	def InitUI(self):

		# Creation de StatusBar 
		self.statusBar().showMessage("This is simple status bar")

		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



		
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

		
