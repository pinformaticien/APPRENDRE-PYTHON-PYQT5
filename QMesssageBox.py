from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys

class Window(QMainWindow):
	"""docstring for Window"""
	def __init__(self):
		super(Window, self).__init__()

		# Initialisation du titre et les coordonnees de notre fenetre
		self.title = "Welcome to PyQt5 framework"
		self.top = 200
		self.left = 300
		self.width = 400
		self.height = 400
        
        #methode qui permet d'inserer l'icone de notre fenetre
		self.setWindowIcon(QtGui.QIcon("icon.png"))

		# creation de bouton
		button = QPushButton("AboutBox", self)
		button.move(200, 200)

		button2 = QPushButton("QuestionMessage", self)
		button2.move(100, 100)

		#bouton connecter a la methode AboutMessage()
		button.clicked.connect(self.AboutMessage)

		#bouton connecter a la methode QuestionMessage
		button2.clicked.connect(self.QuestionMessage)
    	
    	# Appel de la methode InitWindow() dans le constructeur
		self.InitWindow()

	# methode qui permet d'afficher notre fenetre root
	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.show()

	# methode pour qui permet d'afficher le message box
	def AboutMessage(self):
		QMessageBox.about(self, "About Message", "This Is About Message Box")



	def QuestionMessage(self):
		message = QMessageBox.question(self, "Question Message", "Have You Subscribed My Chanenel?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if message == QMessageBox.Yes:
			print("Yes I Have Subscribed")
		else:
			print("No I Have Not Subscribed")



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())