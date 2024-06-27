class Penjumlahan:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def jumlah(self):
        return self.angka1 + self.angka2
    

class Perkalian():
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def kali(self):
        return self.angka1 * self.angka2


class Pembagian(Penjumlahan, Perkalian):

    def bagi(self):
        return self.angka1 / self.angka2
    
hitung = Pembagian(8, 2)
print(hitung.kali())
print(hitung.bagi())
print(hitung.jumlah())
