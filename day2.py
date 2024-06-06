class car:
    def __init__(self,merk,model,tahun):
        self.merk=merk
        self.model=model
        self.tahun=tahun
        self.odometer = 0

    def keterangan(self):
        print(f"Mobil baru saya {self.merk} {self.model}tahun{self.tahun} kilometer masih {self.odometer}")

mobil_baru = car('honda','city',2021)
mobil_baru.keterangan()