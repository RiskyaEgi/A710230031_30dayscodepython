import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from day25 import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.btnAdd.clicked.connect(self.add_data)
        self.btnEdit.clicked.connect(self.edit_data)
        self.btnDelete.clicked.connect(self.delete_data)
        
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Nama", "Alamat", "Umur"])
        
    def add_data(self):
        nama = self.lineEditNama.text()
        alamat = self.lineEditAlamat.text()
        umur = self.lineEditUmur.text()
        
        if not nama or not alamat or not umur:
            QMessageBox.warning(self, "Warning", "Semua field harus diisi!")
            return
        
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(nama))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(alamat))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(umur))
        
        self.lineEditNama.clear()
        self.lineEditAlamat.clear()
        self.lineEditUmur.clear()
        
    def edit_data(self):
        selected_row = self.tableWidget.currentRow()
        
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Pilih baris yang ingin diedit!")
            return
        
        nama = self.lineEditNama.text()
        alamat = self.lineEditAlamat.text()
        umur = self.lineEditUmur.text()
        
        if not nama or not alamat or not umur:
            QMessageBox.warning(self, "Warning", "Semua field harus diisi!")
            return
        
        self.tableWidget.setItem(selected_row, 0, QTableWidgetItem(nama))
        self.tableWidget.setItem(selected_row, 1, QTableWidgetItem(alamat))
        self.tableWidget.setItem(selected_row, 2, QTableWidgetItem(umur))
        
    def delete_data(self):
        selected_row = self.tableWidget.currentRow()
        
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Pilih baris yang ingin dihapus!")
            return
        
        self.tableWidget.removeRow(selected_row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())