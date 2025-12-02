import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Baca dataset
data = pd.read_csv('nilai_siswa.csv')

# 2. Tampilkan info dataset
print("=== Informasi Dataset ===")
print(data.info())

# 3. Tampilkan 5 data pertama
print("\n=== 5 Data Pertama ===")
print(data.head())

# 4. Statistik deskriptif
print("\n=== Statistik Deskriptif ===")
print(data.describe())

# 5. Hitung rata-rata, median, modus nilai
print("\n=== Rata-rata, Median, Modus ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# 6. Tampilkan nilai per mata pelajaran tertentu (contoh: Matematika)
print("\n=== Nilai Matematika ===")
matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

# 7. Nilai maksimun dan minimum per mapel
print("\n=== Nilai Maksimum & Minimum per Mapel ===")
print(data.groupby('Matpel')['Nilai'].agg(['max','min']))

# 8. Grafik batang rata-rata nilai per mapel
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

# 9. Boxplot sebaran nilai
sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()
