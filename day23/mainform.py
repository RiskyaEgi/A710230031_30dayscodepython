from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox 
from form import Ui_Dialog

class Dialog(QDialog, Ui_Dialog): 
    def __init__(self, parent=None): 
        super(Dialog, self).__init__(parent) 
        self.setupUi(self) 
        self.showMessageButton.clicked.connect(self.show_message) 

    def show_message(self): 
        name = self.nameLineEdit.text() 
        QMessageBox.information(self, "Hello", f"Hello, {name}! ") 

app = QApplication([]) 
dialog = Dialog() 
dialog.show() 
app.exec_()