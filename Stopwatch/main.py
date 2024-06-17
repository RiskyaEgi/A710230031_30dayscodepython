import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 772)
        self.jam = QtWidgets.QTextBrowser(Dialog)
        self.jam.setGeometry(QtCore.QRect(150, 160, 151, 101))
        self.jam.setObjectName("jam")
        self.menit = QtWidgets.QTextBrowser(Dialog)
        self.menit.setGeometry(QtCore.QRect(310, 160, 151, 101))
        self.menit.setObjectName("menit")
        self.detik = QtWidgets.QTextBrowser(Dialog)
        self.detik.setGeometry(QtCore.QRect(470, 160, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.detik.setFont(font)
        self.detik.setObjectName("detik")
        self.Lap = QtWidgets.QPushButton(Dialog)
        self.Lap.setGeometry(QtCore.QRect(80, 330, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Lap.setFont(font)
        self.Lap.setObjectName("Lap")
        self.Mulaistop = QtWidgets.QPushButton(Dialog)
        self.Mulaistop.setGeometry(QtCore.QRect(540, 330, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Mulaistop.setFont(font)
        self.Mulaistop.setObjectName("Mulaistop")
        self.LayarLap = QtWidgets.QTextBrowser(Dialog)
        self.LayarLap.setGeometry(QtCore.QRect(80, 430, 601, 291))
        self.LayarLap.setObjectName("LayarLap")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stopwatch"))
        self.Lap.setText(_translate("Dialog", "Lap"))
        self.Mulaistop.setText(_translate("Dialog", "Mulai/Stop"))

class Stopwatch(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

        self.Mulaistop.clicked.connect(self.start_stop)
        self.Lap.clicked.connect(self.lap)

    def start_stop(self):
        if self.running:
            self.timer.stop()
            self.running = False
        else:
            if not self.start_time:
                self.start_time = QtCore.QTime.currentTime()
            self.timer.start(10)
            self.running = True

    def lap(self):
        if self.running:
            current_time = QtCore.QTime.currentTime()
            elapsed = self.start_time.msecsTo(current_time) + self.elapsed_time
            self.LayarLap.append(self.format_time(elapsed))

    def update_time(self):
        current_time = QtCore.QTime.currentTime()
        elapsed = self.start_time.msecsTo(current_time) + self.elapsed_time
        hours, remainder = divmod(elapsed, 3600000)
        minutes, remainder = divmod(remainder, 60000)
        seconds, milliseconds = divmod(remainder, 1000)

        self.jam.setText(f"{hours:02d}")
        self.menit.setText(f"{minutes:02d}")
        self.detik.setText(f"{seconds:02d}.{milliseconds:03d}")

    def format_time(self, msecs):
        hours, remainder = divmod(msecs, 3600000)
        minutes, remainder = divmod(remainder, 60000)
        seconds, milliseconds = divmod(remainder, 1000)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Stopwatch()
    Dialog.show()
    sys.exit(app.exec_())
