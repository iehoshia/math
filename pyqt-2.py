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

	layout = QVBoxLayout()
	layout.addWidget(QPushButton('Top'))
	layout.addWidget(QPushButton('Center'))
	layout.addWidget(QPushButton('Bottom'))

	window.setLayout(layout)

	window.show()
	sys.exit(app.exec_())