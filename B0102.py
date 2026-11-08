# --- 1. DEKLARASI DATA DIRI MAHASISWA ---
nim = "23010199"
nama_mahasiswa = "Ahmad Rian"
semester = 3
is_aktif = True # Status registrasi ulang

# --- 2. DATA NILAI MENTAH (Simulasi input dari Form Web / Database) ---
# Catatan: Input dari form seringkali terbaca sebagai String
str_nilai_algoritma         = "85.5"
str_nilai_basis_data        = "78.0"
str_nilai_pemrograman_web   = "90.2"
sks_per_matkul              = 3 # Integer

# Tampilkan data awal
print(f"Data Mahasiswa: {nama_mahasiswa} (NIM: {nim})")
print(f"Semester: {semester}")
print("Status Aktif :", is_aktif)

# --- 3. KONVERSI TIPE DATA (Type Casting) ---
nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)

# --- 4. KALKULASI MENGGUNAKAN VARIABEL ---
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul

# Penentuan status kelulusan semester (Boolean)
# Lulus jika rata-rata >= 75.0 dan status mahasiswa aktif
is_lulus_semester = (rata_rata_nilai >= 75.0) and is_aktif

print("\n--- HASIL EVALUASI AWAL ---")
print("Total Nilai      :", total_nilai)
print("Rata-Rata Nilai  :", round(rata_rata_nilai, 2))
print("Total SKS        :", total_sks_diambil)
print("Status Lulus     :", is_lulus_semester)

# --- 5. TIPE DATA KOLEKSI ---
# List daftar mata kuliah yang diambil
daftar_matkul = ["Algoritma dan Pemrograman", "Basis Data", "Pemrograman Web"]

# Dictionary untuk menyimpan Nilai Mutu (KRS/KHS)
transkrip_nilai = {
    "Algoritma dan Pemrograman": 4.0,   # Nilai A
    "Basis Data": 3.0,                  # Nilai B
    "Pemrograman Web": 4.0              # Nilai A
}

print("\nDaftar Mata Kuliah Diambil :", daftar_matkul)
print("Detail Transkrip Mutu        :", transkrip_nilai)

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