import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.setWindowTitle('PyQt5 App')

	layout = QGridLayout()
	layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
	layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
	layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
	layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
	layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
	layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
	layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
	layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
	window.setLayout(layout)

	window.show()
	sys.exit(app.exec_())