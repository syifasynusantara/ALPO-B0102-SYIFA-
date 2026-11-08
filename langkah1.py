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
print("Status Aktif :", is_aktif)