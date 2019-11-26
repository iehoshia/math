import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        #self._updateStatusBar()

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def _updateStatusBar(self):
        status = QStatusBar()
        status.showMessage('Josias')
        self.setStatusBar(status)

    def _createMenu(self):
        # Create new action
        openAction = QAction(QIcon('open.png'), '&Josias', self)
        openAction.setShortcut('Ctrl+J')
        openAction.setStatusTip('Print Josias')
        openAction.triggered.connect(self._updateStatusBar)

        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction(openAction)
        self.menu.addAction('&Exit', self.close)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())