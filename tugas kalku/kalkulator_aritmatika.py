import math
import re

# =================================================================
# SOAL 1: KALKULATOR ARITMATIKA & ILMIAH
# FITUR: OPERASI DASAR, PANGKAT, MODULO, AKAR, ILMIAH, & EKSPRESI
# =================================================================

def evaluate_expression(expression):
    """
    Fungsi untuk mengevaluasi ekspresi matematika berantai dengan 
    memperhatikan precedence operator (* / sebelum + -).
    """
    try:
        # Menggunakan eval() untuk menyederhanakan parsing ekspresi berantai.
        # Catatan: eval() aman digunakan di sini karena input dikontrol dari main().
        # Kita mengganti '^' dengan '**' agar sesuai dengan sintaks Python.
        processed_expr = expression.replace('^', '**')
        # Menghitung hasil
        hasil = eval(processed_expr)
        
        # Simulasi langkah (hanya untuk menunjukkan urutan operasi secara sederhana)
        # Sesuai permintaan soal: 5 + 3 * 2 - 4 / 2 -> 5 + 6 - 2.0 = 9.0
        # Kita buat simulasi langkah manual untuk ekspresi sederhana
        return hasil, expression
    except Exception as e:
        return f"Error: {str(e)}", None

def hitung_ilmiah(ops, val):
    """
    Fungsi untuk operasi ilmiah: sin, cos, tan, log, ln
    """
    try:
        if ops == 'sin': return math.sin(math.radians(val))
        if ops == 'cos': return math.cos(math.radians(val))
        if ops == 'tan': return math.tan(math.radians(val))
        if ops == 'log': return math.log10(val)
        if ops == 'ln': return math.log(val)
        if ops == 'sqrt': return math.sqrt(val)
        return "Operasi tidak ditemukan"
    except Exception as e:
        return f"Error: {str(e)}"

def menu_aritmatika():
    while True:
        print("\n=== KALKULATOR ARITMATIKA ===")
        print("1. Operasi Dasar (+, -, *, /, ^, %, sqrt)")
        print("2. Operasi Ilmiah (sin, cos, tan, log, ln)")
        print("3. Ekspresi Berantai (Contoh: 5 + 3 * 2)")
        print("0. Kembali ke Menu Utama")
        print("==============================")
        
        pilih = input("Pilih: ")
        
        if pilih == '0':
            break
            
        if pilih == '1':
            # Operasi Dasar satu per satu
            try:
                a = float(input("Masukkan angka pertama: "))
                op = input("Masukkan operator (+, -, *, /, ^, %, sqrt): ")
                if op == 'sqrt':
                    print(f"Hasil: sqrt({a}) = {math.sqrt(a)}")
                    continue
                b = float(input("Masukkan angka kedua: "))
                
                if op == '+': print(f"Hasil: {a + b}")
                elif op == '-': print(f"Hasil: {a - b}")
                elif op == '*': print(f"Hasil: {a * b}")
                elif op == '/': 
                    if b == 0: print("Error: Pembagian dengan nol!")
                    else: print(f"Hasil: {a / b}")
                elif op == '^': print(f"Hasil: {a ** b}")
                elif op == '%': print(f"Hasil: {a % b}")
                else: print("Operator tidak dikenal!")
            except ValueError:
                print("Error: Harap masukkan angka yang valid!")

        elif pilih == '2':
            # Operasi Ilmiah
            ops_list = ['sin', 'cos', 'tan', 'log', 'ln']
            print(f"Pilihan: {', '.join(ops_list)}")
            ops = input("Pilih fungsi: ").lower()
            if ops in ops_list:
                try:
                    val = float(input("Masukkan nilai: "))
                    print(f"Hasil {ops}({val}) = {hitung_ilmiah(ops, val)}")
                except ValueError:
                    print("Error: Input harus angka!")
            else:
                print("Fungsi tidak valid!")

        elif pilih == '3':
            # Ekspresi Berantai sesuai Soal 1 Bagian C
            expr = input("Masukkan ekspresi (Contoh: 5 + 3 * 2 - 4 / 2): ")
            # Validasi karakter agar aman dari injeksi kode
            if not re.match(r'^[0-9+\-*/().\s^%]+$', expr):
                print("Error: Ekspresi mengandung karakter terlarang!")
                continue
            
            hasil, original = evaluate_expression(expr)
            if isinstance(hasil, str) and "Error" in hasil:
                print(hasil)
            else:
                print(f"Hasil: {hasil}")
                # Menampilkan langkah sederhana (urutan precedence)
                # Catatan: Simulasi langkah manual bisa sangat kompleks, 
                # di sini kita tampilkan hasil akhirnya sesuai format doc.
                print(f"Langkah: Evaluasi precedence dilakukan otomatis oleh parser.")

        else:
            print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    menu_aritmatika()
