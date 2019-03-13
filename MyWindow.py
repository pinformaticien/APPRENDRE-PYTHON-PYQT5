from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		super(Window, self).__init__()

		self.title = "Welcome to PyQt5 framework"
		self.top = 200
		self.left = 300
		self.width = 400
		self.height = 400

		self.setWindowIcon(QtGui.QIcon("icon.png"))

		self.InitWindow()

	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())