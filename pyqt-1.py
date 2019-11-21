import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.setWindowTitle('PyQt5 App')
	window.setGeometry(100, 100, 180, 280)
	window.move(60, 15)
	helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
	helloMsg.move(60, 15)

	window.show()
	sys.exit(app.exec_())