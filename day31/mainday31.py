import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from day31 import Ui_CarPurchaseForm

class CarPurchaseApp(QMainWindow, Ui_CarPurchaseForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submitButton.clicked.connect(self.submit_form)

    def submit_form(self):
        name = self.nameLineEdit.text()
        car_model = self.carModelComboBox.currentText()

        if not name:
            QMessageBox.warning(self, "Input Error", "Please enter your name.")
            return

        QMessageBox.information(self, "Purchase Confirmation", f"Thank you {name}! You have selected {car_model}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarPurchaseApp()
    window.show()
    sys.exit(app.exec_())