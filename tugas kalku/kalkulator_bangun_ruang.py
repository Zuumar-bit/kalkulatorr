import math

def kubus(s):
    return s**3, 6 * s**2

def balok(p, l, t):
    return p*l*t, 2 * (p*l + p*t + l*t)

def tabung(r, t):
    return math.pi * r**2 * t, 2 * math.pi * r * (r + t)

def bola(r):
    return (4/3) * math.pi * r**3, 4 * math.pi * r**2

def tampilkan_menu():
    print("\n" + "="*30)
    print(" KALKULATOR BANGUN RUANG ")
    print("="*30)
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Bola")
    print("5. Keluar")
    print("="*30)

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih bangun ruang (1-5): ")

        if pilihan == '5':
            break

        try:
            if pilihan == '1':
                s = float(input("Masukkan sisi: "))
                vol, lp = kubus(s)
                print(f"Volume: {vol}, Luas Permukaan: {lp}")
            elif pilihan == '2':
                p = float(input("Masukkan panjang: "))
                l = float(input("Masukkan lebar: "))
                t = float(input("Masukkan tinggi: "))
                vol, lp = balok(p, l, t)
                print(f"Volume: {vol}, Luas Permukaan: {lp}")
            elif pilihan == '3':
                r = float(input("Masukkan jari-jari: "))
                t = float(input("Masukkan tinggi: "))
                vol, lp = tabung(r, t)
                print(f"Volume: {vol:.2f}, Luas Permukaan: {lp:.2f}")
            elif pilihan == '4':
                r = float(input("Masukkan jari-jari: "))
                vol, lp = bola(r)
                print(f"Volume: {vol:.2f}, Luas Permukaan: {lp:.2f}")
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Error: Input harus angka!")

if __name__ == "__main__":
    main()
