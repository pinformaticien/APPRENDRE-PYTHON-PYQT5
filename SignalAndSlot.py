import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QMessageBox
from PyQt5.QtCore import QCoreApplication

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

		button = QPushButton("Close", self)
		button.move(200, 200)
		button.setToolTip("<h3>Close The Window</h3>")
		button.clicked.connect(self.CloseApp)

		self.InitUI()


	def InitUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()

	def CloseApp(self):
		reply = QMessageBox.question(self, "Close Message", "Are You Sure To Close Window", QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())