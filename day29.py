phone_number = {}
for i in range(2):
    nama = input(f"Masukkan nama teman {i + 1}:")
    nomer_handphone = input(f"masukkan nomor handphone temen {i + 1}: ")
    phone_number[nama] = nomer_handphone
    print("\nDaftar Nomer:")
for nama, nomer_handphone in phone_number.items():
    print(f"{nama}: {nomer_handphone}")