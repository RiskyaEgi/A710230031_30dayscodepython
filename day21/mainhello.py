import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from hello import Ui_Form

class HelloWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWindow()
    window.show()
    sys.exit(app.exec_())
