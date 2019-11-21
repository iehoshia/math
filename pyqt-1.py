import sys

print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))

from PyQt5.QtWidgets import QApplication, \
	QLabel, QWidget

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.setWindowTitle('My First App - Josias')
	window.setGeometry(100, 100, 280, 280)
	window.move(600, 200)
	window.showMaximized()
	helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
	helloMsg.move(60, 15)

	window.show()
	sys.exit(app.exec_())