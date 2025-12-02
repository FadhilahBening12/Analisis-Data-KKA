📊 Analisis Data Nilai Siswa

Proyek ini merupakan praktikum analisis dan visualisasi data nilai siswa menggunakan Python, Pandas, Matplotlib, dan Seaborn.

📁 Struktur Proyek

```
PraktikumAnalisis/
├── nilai_siswa.csv         # Dataset nilai siswa
├── praktikumanalisis.py    # Script utama analisis data
└── README.md               # Dokumentasi proyek
```

---

🎯 Tujuan Praktikum

1. Menganalisis data nilai siswa dari berbagai mata pelajaran.
2. Membuat visualisasi data untuk memahami pola dan distribusi nilai.
3. Menggunakan statistik deskriptif untuk mendapatkan insight dari dataset.
4. Mengembangkan kemampuan penggunaan Pandas & Matplotlib/Seaborn dalam analisis data.

---

📄 Dataset: `nilai_siswa.csv`

Dataset ini berisi data nilai siswa dengan kolom sebagai berikut:

* **Nama** — Nama siswa
* **Matpel** — Mata pelajaran (Matematika, Bahasa Indonesia, Bahasa Inggris, Produktif, dll.)
* **Nilai** — Nilai akhir siswa

Format contoh:

| Nama  | Matpel           | Nilai |
| ----- | ---------------- | ----- |
| Andi  | Matematika       | 85    |
| Bunga | Bahasa Indonesia | 78    |
| Cahya | Produktif        | 92    |

---

🛠 Persiapan & Instalasi

Pastikan library berikut sudah terinstall di Python:

```
pip install pandas
pip install matplotlib
pip install seaborn
```

---

🧠 Alur Pengerjaan Praktikum (di VS Code)

1. Buka folder praktikum di VS Code.

2. Pastikan file berikut ada:

   ✔ `nilai_siswa.csv`
   ✔ `praktikumanalisis.py`

3. Jalankan program dengan:

```
python praktikumanalisis.py
```

4. Program akan menampilkan:

* Informasi dataset
* Data awal
* Statistik deskriptif
* Rata-rata, median, modus
* Nilai maksimum & minimum per mapel
* Grafik rata-rata per mapel
* Boxplot sebaran nilai

---

🧾 Script Utama: `praktikumanalisis.py`

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Baca dataset
data = pd.read_csv('nilai_siswa.csv')

# 2. Tampilkan informasi dataset
print("=== Informasi Dataset ===")
print(data.info())

# 3. Tampilkan 5 data pertama
print("\n=== 5 Data Pertama ===")
print(data.head())

# 4. Statistik deskriptif
print("\n=== Statistik Deskriptif ===")
print(data.describe())

# 5. Hitung rata-rata, median, modus
print("\n=== Rata-rata, Median, Modus ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# 6. Contoh: Ambil nilai Matematika saja
print("\n=== Nilai Matematika ===")
matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

# 7. Nilai maksimum & minimum tiap mata pelajaran
print("\n=== Nilai Maksimum & Minimum per Mapel ===")
print(data.groupby('Matpel')['Nilai'].agg(['max','min']))

# 8. Grafik rata-rata nilai
plt.figure(figsize=(8,5))
data.groupby('Matpel')['Nilai'].mean().plot(kind='bar')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

# 9. Boxplot sebaran nilai
plt.figure(figsize=(8,5))
sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()
```

---

📝 Kesimpulan yang Diharapkan

Dalam laporan, mahasiswa diharapkan menuliskan:

* Pola nilai per mata pelajaran
* Mata pelajaran dengan nilai tertinggi & terendah
* Persebaran nilai (apakah merata atau menyebar jauh)
* Insight dari grafik

---

✔ Status Praktikum

Dokumentasi, analisis, dan visualisasi **sudah lengkap dan sesuai** dengan kebutuhan praktikum.

---
