class Tiket:
    def __init__(self, jenis_tiket, harga):
        self.jenis_tiket = jenis_tiket
        self.harga = harga

    def get_jenis_tiket(self):
        return self.jenis_tiket

    def get_harga(self):
        return self.harga

    def hitung_harga(self):
        if self.harga is None:
            raise NotImplementedError("Harga belum dihitung untuk tiket jenis ini")
        return self.harga

def main():
    tiket_biasa = Tiket("Biasa", 25000)
    tiket_vip = Tiket("VIP", 50000)
    tiket_gold = Tiket("Gold", 75000)

    print(f"Harga tiket {tiket_biasa.get_jenis_tiket()}: Rp. {tiket_biasa.hitung_harga()}")
    print(f"Harga tiket {tiket_vip.get_jenis_tiket()}: Rp. {tiket_vip.hitung_harga()}")
    print(f"Harga tiket {tiket_gold.get_jenis_tiket()}: Rp. {tiket_gold.hitung_harga()}")

if __name__ == "__main__":
    main()
