import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip


class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		super(Window, self).__init__()
		
		self.title = "PyQt5 Push Button"
		self.top = 100
		self.left = 100
		self.width = 680
		self.height = 540

		self.setWindowIcon(QtGui.QIcon("icon.png"))

		button = QPushButton("Click Me", self)
		button.move(200, 200)
		button.setToolTip("<h3>This Is Click Button</h3>")

		self.InitUI()


	def InitUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())