from PyQt5.QtWidgets import QApplication, QMainWindow
from timer_ui import Ui_MainWindow

class TimerApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(TimerApp, self).__init__(parent)
        self.setupUi(self)

app = QApplication([])
window = TimerApp()
window.show()
app.exec_()