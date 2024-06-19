import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Label
        self.labelHarga = QtWidgets.QLabel("Harga:", self)
        self.labelPajak = QtWidgets.QLabel("Pajak:", self)
        self.labelTotalHarga = QtWidgets.QLabel("Total harga beserta Pajak Adalah:", self)

        # Input
        self.inputHarga = QtWidgets.QLineEdit("10000", self)
        self.inputPajak = QtWidgets.QLineEdit(self)

        # ComboBox
        self.comboBoxPajak = QtWidgets.QComboBox(self)
        self.comboBoxPajak.addItem("5%")
        self.comboBoxPajak.addItem("10%")
        self.comboBoxPajak.addItem("15%")

        # Button
        self.buttonHitungPajak = QtWidgets.QPushButton("Hitung Pajak", self)

        # Layout
        grid = QtWidgets.QGridLayout(self)

        grid.addWidget(self.labelHarga, 0, 0)
        grid.addWidget(self.inputHarga, 0, 1)

        grid.addWidget(self.labelPajak, 1, 0)
        grid.addWidget(self.inputPajak, 1, 1)

        grid.addWidget(self.labelTotalHarga, 2, 0)
        grid.addWidget(self.labelTotalHarga, 2, 1)

        grid.addWidget(self.comboBoxPajak, 3, 0)
        grid.addWidget(self.buttonHitungPajak, 3, 1)

        self.setLayout(grid)

        # Koneksi
        self.buttonHitungPajak.clicked.connect(self.hitungPajak)

    def hitungPajak(self):
        try:
            # Dapatkan nilai dari input
            harga = float(self.inputHarga.text())
            pajak_persen = float(self.comboBoxPajak.currentText().replace("%", ""))

            # Hitung pajak
            pajak = harga * (pajak_persen / 100)

            # Hitung total harga
            total_harga = harga + pajak

            # Tampilkan hasil perhitungan
            self.labelTotalHarga.setText(f"Total Harga Beserta Pajak Adalah: {total_harga:.2f}")
        except ValueError:
            # Tampilkan pesan error jika input tidak valid
            self.labelTotalHarga.setText("Masukan nilai yang valid!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
