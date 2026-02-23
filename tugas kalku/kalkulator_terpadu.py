import os
import datetime

# Import modul-modul yang telah dibuat sebelumnya
import kalkulator_aritmatika as aritmatika
import kalkulator_suhu as suhu
import kalkulator_bilangan as bilangan

# =================================================================
# SOAL 4: INTEGRASI SISTEM (MASTER MENU)
# FITUR: RIWAYAT 10 PERHITUNGAN, EXPORT HASIL, & VALIDASI ROBUST
# =================================================================

# List untuk menyimpan riwayat perhitungan (global dalam scope main)
riwayat_perhitungan = []

def simpan_ke_riwayat(isi):
    """
    Menyimpan hasil ke riwayat. Maksimal 10 item (FIFO).
    """
    global riwayat_perhitungan
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {isi}"
    riwayat_perhitungan.append(entry)
    # Jika lebih dari 10, hapus yang tertua
    if len(riwayat_perhitungan) > 10:
        riwayat_perhitungan.pop(0)

def tampilkan_riwayat():
    """
    Menampilkan 10 perhitungan terakhir.
    """
    print("\n=== RIWAYAT 10 PERHITUNGAN TERAKHIR ===")
    if not riwayat_perhitungan:
        print("Belum ada riwayat.")
    else:
        for i, item in enumerate(riwayat_perhitungan, 1):
            print(f"{i}. {item}")
    print("=========================================")

def export_history():
    """
    Menyimpan riwayat ke dalam file teks (.txt).
    """
    if not riwayat_perhitungan:
        print("Error: Tidak ada data untuk diekspor.")
        return
        
    filename = "hasil_kalkulasi.txt"
    try:
        with open(filename, "w") as f:
            f.write("=== LOG RIWAYAT PERHITUNGAN KALKULATOR ===\n")
            for item in riwayat_perhitungan:
                f.write(item + "\n")
        print(f"Berhasil mengekspor ke {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Gagal mengekspor: {e}")

def main_menu():
    """
    Menu utama aplikasi terpadu sesuai struktur Soal 4 Bagian C.
    """
    while True:
        print("\n" + "╔" + "═"*39 + "╗")
        print("║     SISTEM KALKULATOR MULTI-FUNGSI    ║")
        print("╠" + "═"*39 + "╣")
        print("║  1. Kalkulator Aritmatika             ║")
        print("║  2. Kalkulator Suhu                   ║")
        print("║  3. Kalkulator Konversi Bilangan      ║")
        print("║  4. Riwayat Perhitungan               ║")
        print("║  5. Export Hasil ke File              ║")
        print("║  0. Keluar                            ║")
        print("╚" + "═"*39 + "╝")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '0':
            print("Terima kasih telah menggunakan sistem ini!")
            break
            
        elif pilihan == '1':
            # Integrasi Aritmatika
            aritmatika.menu_aritmatika()
            # Simulasi simpan hasil ke riwayat (bisa dikembangkan di dalam modul)
            simpan_ke_riwayat("Menggunakan Kalkulator Aritmatika")

        elif pilihan == '2':
            # Integrasi Suhu
            suhu.menu_suhu()
            simpan_ke_riwayat("Menggunakan Kalkulator Suhu")

        elif pilihan == '3':
            # Integrasi Konversi Bilangan
            bilangan.menu_bilangan()
            simpan_ke_riwayat("Menggunakan Kalkulator Bilangan")

        elif pilihan == '4':
            tampilkan_riwayat()

        elif pilihan == '5':
            export_history()

        else:
            print("Pilihan tidak valid! Masukkan angka 0-5.")

if __name__ == "__main__":
    # Menjalankan menu utama
    main_menu()
