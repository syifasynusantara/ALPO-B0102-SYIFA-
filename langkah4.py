# --- 6. UPDATE VARIABEL DINAMIS ---
# Mahasiswa mengambil 1 mata kuliah susulan 
matkul_baru = "Jaringan Komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5 # Nilai AB

# A. Tambahkan ke List
daftar_matkul.append(matkul_baru)

# B. Tambahkan ke Dictionary
transkrip_nilai[matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi Variabel Total & Rata-rata
nilai_jk = float(nilai_matkul_baru_str)
total_nilai = total_nilai + nilai_jk    # Memperbarui nilai variabel total_nilai
jumlah_matkul = len(daftar_matkul)      # Memperbarui jumlah matkul menggunakan len(daftar_matkul)
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. Hitung Indeks Prestasi Kumulatif (IPK) dari Dictionary Mutu
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\n--- HASIL REKALKULASI SETELAH PENAMBAHAN MATKUL ---")
print("Daftar Matkul Terbaru    :", daftar_matkul)
print("Jumlah Matkul Total      :", jumlah_matkul)
print("Rata-Rata Angka Baru     :", round(rata_rata_terbaru, 2))
print("IPK Sementara (Skala 4)  :", round(ipk_sementara, 2))