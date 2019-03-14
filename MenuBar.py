import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction

class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		super(Window, self).__init__()

		self.title = "QMenuBar"
		self.top = 200
		self.left = 200
		self.width = 600
		self.height = 500

		self.setWindowIcon(QtGui.QIcon("icon.png"))

		self.InitUI()

	def InitUI(self):

		#Creation de Menu avec PyQt5
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("File")
		viewMenu = mainMenu.addMenu("View")
		editMenu = mainMenu.addMenu("Edit")
		searchMenu = mainMenu.addMenu("Search")
		toolMenu = mainMenu.addMenu("Tool")
		helpMenu= mainMenu.addMenu("Help")

		#Creation d'Action connecter avec le menu
		exitButton = QAction(QIcon("exit.png"), 'Exit', self)
		exitButton.setShortcut("Ctrl+E")
		exitButton.setStatusTip("Exit Application")
		exitButton.triggered.connect(self.close)
		fileMenu.addAction(exitButton)


		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()



		
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

		
