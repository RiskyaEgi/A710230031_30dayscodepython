from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditNama = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNama.setObjectName("lineEditNama")
        self.horizontalLayout.addWidget(self.lineEditNama)
        self.lineEditAlamat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAlamat.setObjectName("lineEditAlamat")
        self.horizontalLayout.addWidget(self.lineEditAlamat)
        self.lineEditUmur = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUmur.setObjectName("lineEditUmur")
        self.horizontalLayout.addWidget(self.lineEditUmur)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_2.addWidget(self.btnAdd)
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setObjectName("btnEdit")
        self.horizontalLayout_2.addWidget(self.btnEdit)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_2.addWidget(self.btnDelete)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Penduduk Desa"))
        self.lineEditNama.setPlaceholderText(_translate("MainWindow", "Nama"))
        self.lineEditAlamat.setPlaceholderText(_translate("MainWindow", "Alamat"))
        self.lineEditUmur.setPlaceholderText(_translate("MainWindow", "Umur"))
        self.btnAdd.setText(_translate("MainWindow", "Tambah"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnDelete.setText(_translate("MainWindow", "Hapus"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
