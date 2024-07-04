from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CarPurchaseForm(object):
    def setupUi(self, CarPurchaseForm):
        CarPurchaseForm.setObjectName("CarPurchaseForm")
        CarPurchaseForm.resize(400, 300)
        self.label = QtWidgets.QLabel(CarPurchaseForm)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.label.setObjectName("label")
        self.nameLineEdit = QtWidgets.QLineEdit(CarPurchaseForm)
        self.nameLineEdit.setGeometry(QtCore.QRect(120, 30, 241, 21))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.label_2 = QtWidgets.QLabel(CarPurchaseForm)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.label_2.setObjectName("label_2")
        self.carModelComboBox = QtWidgets.QComboBox(CarPurchaseForm)
        self.carModelComboBox.setGeometry(QtCore.QRect(120, 70, 241, 22))
        self.carModelComboBox.setObjectName("carModelComboBox")
        self.carModelComboBox.addItem("")
        self.carModelComboBox.addItem("")
        self.carModelComboBox.addItem("")
        self.submitButton = QtWidgets.QPushButton(CarPurchaseForm)
        self.submitButton.setGeometry(QtCore.QRect(150, 110, 93, 28))
        self.submitButton.setObjectName("submitButton")

        self.retranslateUi(CarPurchaseForm)
        QtCore.QMetaObject.connectSlotsByName(CarPurchaseForm)

    def retranslateUi(self, CarPurchaseForm):
        _translate = QtCore.QCoreApplication.translate
        CarPurchaseForm.setWindowTitle(_translate("CarPurchaseForm", "Car Purchase"))
        self.label.setText(_translate("CarPurchaseForm", "Name:"))
        self.label_2.setText(_translate("CarPurchaseForm", "Car Model:"))
        self.carModelComboBox.setItemText(0, _translate("CarPurchaseForm", "Sedan"))
        self.carModelComboBox.setItemText(1, _translate("CarPurchaseForm", "SUV"))
        self.carModelComboBox.setItemText(2, _translate("CarPurchaseForm", "Hatchback"))
        self.submitButton.setText(_translate("CarPurchaseForm", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CarPurchaseForm = QtWidgets.QWidget()
    ui = Ui_CarPurchaseForm()
    ui.setupUi(CarPurchaseForm)
    CarPurchaseForm.show()
    sys.exit(app.exec_())
