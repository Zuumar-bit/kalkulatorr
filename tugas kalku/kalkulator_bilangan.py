# =================================================================
# SOAL 3: KALKULATOR KONVERSI BILANGAN
# FITUR: KONVERSI MANUAL BASIS & ARITMATIKA NON-DESIMAL
# =================================================================

def decimal_ke_basis(n, basis):
    """
    Konversi Desimal ke Basis X menggunakan algoritma pembagian beruntun.
    TIDAK menggunakan bin(), hex(), oct().
    """
    if n == 0: return "0", "0 / {} = 0 sisa 0".format(basis)
    
    chars = "0123456789ABCDEF"
    hasil = ""
    langkah = []
    temp_n = n
    
    while temp_n > 0:
        sisa = temp_n % basis
        langkah.append(f"{temp_n} / {basis} = {temp_n // basis} sisa {chars[sisa]}")
        hasil = chars[sisa] + hasil
        temp_n //= basis
        
    return hasil, "\n".join(langkah)

def basis_ke_decimal(s, basis):
    """
    Konversi Basis X ke Desimal menggunakan algoritma penjumlahan perpangkatan.
    """
    chars = "0123456789ABCDEF"
    s = s.upper()
    hasil = 0
    langkah = []
    n = len(s)
    
    for i in range(n):
        val = chars.index(s[i])
        pangkat = n - 1 - i
        term = val * (basis ** pangkat)
        langkah.append(f"{val} x {basis}^{pangkat} = {term}")
        hasil += term
        
    return hasil, " + ".join(langkah)

def hitung_kolom(a, b, op, basis):
    """
    Aritmatika (tambah/kurang) untuk basis non-desimal.
    Dilakukan dengan konversi ke desimal dulu, hitung, lalu balikkan.
    Namun menampilkan proses ala manual (kolom).
    """
    dec_a, _ = basis_ke_decimal(a, basis)
    dec_b, _ = basis_ke_decimal(b, basis)
    
    if op == '+': res_dec = dec_a + dec_b
    else: res_dec = dec_a - dec_b
    
    res_basis, _ = decimal_ke_basis(abs(res_dec), basis)
    if res_dec < 0: res_basis = "-" + res_basis
    
    # Simulasi tampilan kolom
    print(f"\nProses Perhitungan ({basis}):")
    print(f"{a:>10}")
    print(f"{b:>10} ({op})")
    print("-" * 12)
    print(f"{res_basis:>10}")
    return res_basis

def menu_bilangan():
    while True:
        print("\n=== KALKULATOR BILANGAN ===")
        print("1. Konversi Basis (Manual + Langkah)")
        print("2. Operasi Aritmatika (Biner/Oktal/Hex)")
        print("0. Kembali ke Menu Utama")
        print("============================")
        
        pilih = input("Pilih: ")
        
        if pilih == '0':
            break
            
        if pilih == '1':
            print("Basis: 2 (Biner), 8 (Oktal), 10 (Desimal), 16 (Heksadesimal)")
            try:
                b1 = int(input("Basis Asal (2/8/10/16): "))
                b2 = int(input("Basis Tujuan (2/8/10/16): "))
                val = input("Masukkan Nilai: ")
                
                # Alur: Asal -> Desimal -> Tujuan
                if b1 == 10:
                    dec_val = int(val)
                else:
                    dec_val, steps = basis_ke_decimal(val, b1)
                    print(f"\nLangkah ke Desimal: {steps} = {dec_val}")
                
                final_val, final_steps = decimal_ke_basis(dec_val, b2)
                print(f"\nLangkah Konversi:")
                print(final_steps)
                print(f"\nHasil Akhir: {final_val}")
                print(f"Verifikasi: {dec_val} (Desimal)")
            except Exception as e:
                print(f"Error: {e}")

        elif pilih == '2':
            try:
                basis = int(input("Pilih Basis (2/8/16): "))
                num1 = input("Angka Pertama: ")
                num2 = input("Angka Kedua: ")
                op = input("Operasi (+ / -): ")
                
                if op in ('+', '-'):
                    hasil = hitung_kolom(num1, num2, op, basis)
                    print(f"Hasil Akhir: {hasil}")
                else:
                    print("Operator tidak didukung.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_bilangan()
