# =================================================================
# SOAL 2: KALKULATOR KONVERSI SUHU
# FITUR: KONVERSI 2-ARAH, TABEL KONVERSI, & KLASIFIKASI SUHU
# =================================================================

def konversi_suhu(nilai, dari, ke):
    """
    Fungsi inti untuk konversi suhu antar 4 skala utama.
    Semua konversi menggunakan Celsius sebagai perantara (base).
    """
    # 1. Konversi dari asal ke Celsius
    if dari == "Celsius": c = nilai
    elif dari == "Fahrenheit": c = (nilai - 32) * 5/9
    elif dari == "Kelvin": c = nilai - 273.15
    elif dari == "Reaumur": c = nilai * 5/4
    else: return None

    # 2. Konversi dari Celsius ke tujuan
    if ke == "Celsius": return round(c, 2)
    elif ke == "Fahrenheit": return round((c * 9/5) + 32, 2)
    elif ke == "Kelvin": return round(c + 273.15, 2)
    elif ke == "Reaumur": return round(c * 4/5, 2)
    else: return None

def klasifikasi_suhu(c):
    """
    Klasifikasi suhu berdasarkan nilai dalam Celsius sesuai Soal 2 Bagian B.
    """
    if c <= 0: return "Beku"
    elif 1 <= c <= 15: return "Dingin"
    elif 16 <= c <= 25: return "Normal"
    elif 26 <= c <= 35: return "Panas"
    else: return "Sangat Panas"

def tampilkan_tabel():
    """
    Menampilkan tabel konversi 0-100 C dengan step 10 C.
    """
    print("\n=== TABEL KONVERSI (0C - 100C) ===")
    print(f"{'Celsius':<10} | {'Fahr':<10} | {'Kelvin':<10} | {'Reaumur':<10} | {'Status':<15}")
    print("-" * 65)
    for c in range(0, 101, 10):
        f = (c * 9/5) + 32
        k = c + 273.15
        r = c * 4/5
        status = klasifikasi_suhu(c)
        print(f"{c:<10} | {f:<10.1f} | {k:<10.2f} | {r:<10.1f} | {status:<15}")

def menu_suhu():
    while True:
        print("\n=== KALKULATOR SUHU ===")
        print("1. Konversi Satuan (2-Arah + Klasifikasi)")
        print("2. Tabel Konversi (0-100 C)")
        print("0. Kembali ke Menu Utama")
        print("=========================")
        
        pilih = input("Pilih menu: ")
        
        if pilih == '0':
            break
            
        if pilih == '1':
            options = ["Celsius", "Fahrenheit", "Kelvin", "Reaumur"]
            print("Pilihan Skala: " + ", ".join(options))
            
            dari = input("Dari: ").capitalize()
            ke = input("Ke: ").capitalize()
            
            if dari in options and ke in options:
                try:
                    nilai = float(input("Nilai: "))
                    hasil = konversi_suhu(nilai, dari, ke)
                    
                    # Dapatkan nilai celsius untuk klasifikasi
                    if dari == "Celsius": c_val = nilai
                    else:
                        # Konversi balik ke celsius jika input bukan celsius
                        if dari == "Fahrenheit": c_val = (nilai - 32) * 5/9
                        elif dari == "Kelvin": c_val = nilai - 273.15
                        elif dari == "Reaumur": c_val = nilai * 5/4
                    
                    status = klasifikasi_suhu(c_val)
                    
                    print(f"\nHasil: {nilai}{dari[0]} = {hasil}{ke[0]}")
                    print(f"Klasifikasi: {status}")
                except ValueError:
                    print("Error: Harap masukkan angka yang valid!")
            else:
                print("Skala tidak valid! Gunakan nama lengkap (contoh: Celsius).")

        elif pilih == '2':
            tampilkan_tabel()
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_suhu()
