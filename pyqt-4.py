import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.setWindowTitle('PyQt5 App')

	layout = QFormLayout()
	layout.addRow('Name:', QLineEdit())
	layout.addRow('Age:', QLineEdit())
	layout.addRow('Job:', QLineEdit())
	layout.addRow('Hobbies:', QLineEdit())
	window.setLayout(layout)

	window.show()
	sys.exit(app.exec_())