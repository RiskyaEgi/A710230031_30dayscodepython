def apakah_prima(bilangan):
    if bilangan > 1:
        for i in range(2, bilangan):
            if (bilangan % i) == 0:
                print("Bukan Bilangan Prima")
                break
        else:
            print("Bilangan Prima")
    else:
        print("Bukan Bilangan Prima")

bilangan = int(input("Masukkan bilangan: "))
apakah_prima(bilangan)