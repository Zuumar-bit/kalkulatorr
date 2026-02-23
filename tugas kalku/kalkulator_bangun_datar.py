import math

def persegi(s):
    return s*s, 4*s

def persegi_panjang(p, l):
    return p*l, 2*(p+l)

def lingkaran(r):
    return math.pi * r**2, 2 * math.pi * r

def segitiga(a, t, s1, s2, s3):
    return 0.5 * a * t, s1 + s2 + s3

def tampilkan_menu():
    print("\n" + "="*30)
    print(" KALKULATOR BANGUN DATAR ")
    print("="*30)
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")
    print("4. Segitiga")
    print("5. Keluar")
    print("="*30)

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih bangun datar (1-5): ")

        if pilihan == '5':
            break

        try:
            if pilihan == '1':
                s = float(input("Masukkan sisi: "))
                luas, kel = persegi(s)
                print(f"Luas: {luas}, Keliling: {kel}")
            elif pilihan == '2':
                p = float(input("Masukkan panjang: "))
                l = float(input("Masukkan lebar: "))
                luas, kel = persegi_panjang(p, l)
                print(f"Luas: {luas}, Keliling: {kel}")
            elif pilihan == '3':
                r = float(input("Masukkan jari-jari: "))
                luas, kel = lingkaran(r)
                print(f"Luas: {luas:.2f}, Keliling: {kel:.2f}")
            elif pilihan == '4':
                a = float(input("Masukkan alas: "))
                t = float(input("Masukkan tinggi: "))
                s1 = float(input("Masukkan sisi 1: "))
                s2 = float(input("Masukkan sisi 2: "))
                s3 = float(input("Masukkan sisi 3: "))
                luas, kel = segitiga(a, t, s1, s2, s3)
                print(f"Luas: {luas}, Keliling: {kel}")
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Error: Input harus angka!")

if __name__ == "__main__":
    main()
