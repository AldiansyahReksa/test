# -*- coding: utf-8 -*-
"""data_analytic_kunjungan_wisata_2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1syJe8rQEqyTAzGPMfHrhUcPCtwep7oqE

#Data wrangling

# Gathering data

kunjungan wisata lewat jalur laut
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File paths
file_path_laut = 'kunjungan_wisata_mancanegara_laut.csv'
file_path_darat = 'kunjungan_wisata_mancanegara_darat.csv'
file_path_udara = 'kunjungan_wisata_mancanegara_udara.csv'

# Load data (menggunakan read_csv untuk file CSV)
jalur_laut = pd.read_csv(file_path_laut)
jalur_darat = pd.read_csv(file_path_darat)
jalur_udara = pd.read_csv(file_path_udara)


pd.set_option('display.max_rows', None)
jalur_laut.head()

"""jalur darat"""

# data kunjungan darat
jalur_darat.head()

"""Jalur Udara"""

# data kunjungan Udara
jalur_udara.head()

"""# Assesing Data

menilai tabel jalur laut
"""

jalur_laut.info()

jalur_laut.isna().sum()

print("jumlah duplikasi : ",jalur_laut.duplicated().sum())

jalur_laut.describe()

"""Menilai tabel jalur darat"""

jalur_darat.info()

print("jumlah duplikasi : ",jalur_darat.duplicated().sum())

jalur_darat.describe()

"""Menilai Tabel jalur Udara"""

jalur_udara.info()

jalur_udara.isna().sum()

print("jumlah duplikasi : ",jalur_udara.duplicated().sum())

jalur_udara.describe()

"""# Cleaning Data

Cleaning Jalur Laut

Missing value
"""

jalur_laut.isna().sum()

jalur_laut[jalur_laut.Tahunan.isna()]

"""drop misssing value"""

jalur_laut['Tahunan'] =jalur_laut.loc[:, 'Januari':'Agustus'].sum(axis=1)

jalur_laut.head(8)

jalur_laut.isna().sum()

"""duplicate data"""

jalur_laut.duplicated().sum()

"""Cleaning Jalur Darat

Missing value
"""

jalur_darat.isna().sum()

jalur_darat['Tahunan'] =jalur_darat.loc[:, 'Januari':'Agustus'].sum(axis=1)

jalur_darat.head()

"""duplicated data"""

print("jumlah duplikasi : ",jalur_darat.duplicated().sum())

"""Jalur Udara

Missing Value
"""

jalur_udara.isna().sum()

jalur_udara['Tahunan'] =jalur_udara.loc[:, 'Januari':'Agustus'].sum(axis=1)

jalur_udara.head()

"""Duplikasi Data"""

print("jumlah duplikasi : ", jalur_udara.duplicated().sum())

"""# Exploratory data"""

jalur_laut.sample(3)

# pd.options.display.float_format = '{:.0f}'.format

jalur_laut.head(8)

jalur_laut.describe()

"""Berdasarkan data diatas dapat disimpulkan bahwa total pengunjung lewat jalur laut di tahun 2024(januari - Agustus) adalah 1840000 dengan nilai  rata-rat adalah  460000,dengan nilai maksimum 261000 yang terjadi di bulan juni"""

# prompt: grup data jalur laut berdasarkan jalur masuk laut

# Grouping data jalur laut berdasarkan jalur masuk laut (assuming 'Pelabuhan' is the column representing the entry point)
grouped_jalur_laut = jalur_laut.groupby('Jalur masuk Laut')

# Example: Calculating the total number of visitors for each entry point
total_visitors_by_entry_point = grouped_jalur_laut['Tahunan'].sum()

# You can then analyze the grouped data further, such as:
# - Calculating average visitors per month for each entry point
# - Finding the entry point with the highest number of visitors
# - Plotting the distribution of visitors across different entry points

total_visitors_by_entry_point

# prompt: Plotting the distribution of visitors across different entry points untuk jalur laut

filtered_data = jalur_laut[jalur_laut['Jalur masuk Laut'].str.lower() != 'total']  # pastikan 'Total' tidak sensitif huruf besar-kecil

# Mengelompokkan data yang sudah difilter berdasarkan 'Jalur masuk Darat' dan menghitung total wisatawan
grouped_filtered_data = filtered_data.groupby('Jalur masuk Laut')['Tahunan'].sum()
# Plotting the distribution of visitors across different entry points for sea route
plt.figure(figsize=(12, 6))
sns.barplot(x=grouped_filtered_data.index, y=grouped_filtered_data.values)
plt.title('Distribusi Wisatawan Melalui Berbagai Jalur Masuk (Laut)')
plt.xlabel('Jalur masuk')
plt.ylabel('Total Wisatawan')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

"""Berdasarkan data di atas Batam merupakan penyumbang terbanyak untuk jalur masuk laut sebesar 822422 orang

jalur Darat
"""

jalur_darat.describe()

"""Berdasarkan data diatas dapat disimpulkan bahwa total pengunjung lewat jalur darat di tahun 2024(januari - Agustus) adalah 817200 dengan nilai rata -rata  adalah 233486,dan nilai maksimum 115122 orang yang terjadi di bulan juni"""

# Buat filter untuk menghilangkan baris 'Total' hanya untuk visualisasi
filtered_data = jalur_darat[jalur_darat['Jalur masuk Darat'].str.lower() != 'total']  # pastikan 'Total' tidak sensitif huruf besar-kecil

# Mengelompokkan data yang sudah difilter berdasarkan 'Jalur masuk Darat' dan menghitung total wisatawan
grouped_filtered_data = filtered_data.groupby('Jalur masuk Darat')['Tahunan'].sum()
print(grouped_filtered_data)
# Visualisasi Data tanpa baris 'Total'
plt.figure(figsize=(12, 6))
sns.barplot(x=grouped_filtered_data.index, y=grouped_filtered_data.values)
plt.title('Distribusi Wisatawan Melalui Berbagai Jalur Masuk (Darat)')
plt.xlabel('Jalur Masuk')
plt.ylabel('Total Wisatawan')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""Berdasarkan data di atas jalur darat lainnya pintu darurat lainnya merupakan  penyumbang terbanyak untuk jalur masuk darat sebesar 621794 orang

Jalur Udara
"""

jalur_udara.head(17)

jalur_udara['Tahunan'] =jalur_udara.loc[:, 'Januari':'Agustus'].sum(axis=1)

pd.options.display.float_format = '{:.0f}'.format

jalur_udara.describe()

"""Berdasarkan data diatas dapat disimpulkan bahwa total pengunjung lewat jalur udara di tahun 2024(januari - Agustus) adalah 6439063 dengan nilai rata -rata adalah 757537,dan nilai maksimum 994583 orang yang terjadi di bulan juli"""



grouped_jalur_udara = jalur_udara.groupby('Jalur masuk Udara')
total_visitors_by_entry_point = grouped_jalur_udara['Tahunan'].sum()
total_visitors_by_entry_point

filtered_data = jalur_udara[jalur_udara['Jalur masuk Udara'].str.lower() != 'total']  # pastikan 'Total' tidak sensitif huruf besar-kecil

# Mengelompokkan data yang sudah difilter berdasarkan 'Jalur masuk Darat' dan menghitung total wisatawan
grouped_filtered_data = filtered_data.groupby('Jalur masuk Udara')['Tahunan'].sum()
print(grouped_filtered_data)
# Visualisasi Data tanpa baris 'Total'
plt.figure(figsize=(12, 6))
sns.barplot(x=grouped_filtered_data.index, y=grouped_filtered_data.values)
plt.title('Distribusi Wisatawan Melalui Berbagai Jalur Masuk (Darat)')
plt.xlabel('Jalur Masuk')
plt.ylabel('Total Wisatawan')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""Berdasarkan data di atas pintu masuk Ngurah Rai merupakan penyumbang terbanyak untuk jalur masuk udara sebesar 4140402 orang"""

# print(merged_df)

# Contoh penggabungan menggunakan indeks
# df1 = pd.DataFrame({'Nama': ['A', 'B', 'C']})
# df2 = pd.DataFrame({'Nilai': [80, 85, 90]})
# # hasil_merge = pd.merge(df1, df2, left_index=True, right_index=True)

# hasil_concat = pd.concat([df1, df2], axis=1)
# print(hasil_concat)
df1 = jalur_udara
df2 = jalur_darat
# hasil_merge = pd.merge(df1, df2, left_index=True, right_index=True)

hasil_concat = pd.concat([df1, df2], axis=1)
hasil_concat_dropped = hasil_concat.drop(['September', 'Oktober', 'November','Desember'], axis=1)
pd.options.display.width = 100  # Menyesuaikan lebar tampilan
pd.options.display.max_columns = None  # Menampilkan semua kolom
display(hasil_concat_dropped)

# hasil_concat_dropped.dropna(inplace=True)
# Mengganti NaN dengan teks tertentu
hasil_concat_dropped = hasil_concat_dropped.fillna('Tidak Ada Data')

# Menampilkan hasil
print(hasil_concat_dropped)

# Menambahkan sufiks untuk kolom 'Tahunan' pada masing-masing DataFrame
df1 = jalur_udara.rename(columns={'Tahunan': 'Tahunan_Udara'})
df2 = jalur_darat.rename(columns={'Tahunan': 'Tahunan_Darat'})
df3 = jalur_laut.rename(columns={'Tahunan': 'Tahunan_Laut'})

# Gabungkan kedua DataFrame dengan concat
hasil_concat = pd.concat([df1, df2,df3], axis=1)

# Menghapus kolom bulanan yang berulang agar lebih rapi (opsional)
hasil_concat_dropped = hasil_concat.drop(columns=['September', 'Oktober', 'November', 'Desember'], errors='ignore')

# Konversi kolom 'Tahunan' menjadi numerik
hasil_concat_dropped['Tahunan_Udara'] = pd.to_numeric(hasil_concat_dropped['Tahunan_Udara'], errors='coerce')
hasil_concat_dropped['Tahunan_Darat'] = pd.to_numeric(hasil_concat_dropped['Tahunan_Darat'], errors='coerce')
hasil_concat_dropped['Tahunan_Laut'] = pd.to_numeric(hasil_concat_dropped['Tahunan_Laut'], errors='coerce')

# Hitung total kunjungan untuk masing-masing jalur
total_jalur_udara = hasil_concat_dropped['Tahunan_Udara'].sum()
total_jalur_darat = hasil_concat_dropped['Tahunan_Darat'].sum()
total_jalur_laut = hasil_concat_dropped['Tahunan_Laut'].sum()

# Tampilkan hasil
print("Total Kunjungan Jalur Udara:", total_jalur_udara)
print("Total Kunjungan Jalur Darat:", total_jalur_darat)
print("Total Kunjungan Jalur Laut:", total_jalur_laut)

# ubah nan jadi 0
hasil_concat_dropped = hasil_concat_dropped.fillna(0)
# tampilkan data  kolom total


# Tampilkan hasil
display(hasil_concat_dropped)

"""Total kunjungan per tahun(januari-agustus) untuk masing-masing jalur"""

import matplotlib.pyplot as plt

# Data untuk grafik
total_kunjungan = [total_jalur_udara, total_jalur_darat, total_jalur_laut]
jalur_masuk = ['Udara', 'Darat', 'Laut']
print(total_kunjungan)
print(jalur_masuk)
# Membuat grafik bar
plt.figure(figsize=(8, 5))
plt.bar(jalur_masuk, total_kunjungan, color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Total Kunjungan Tahunan per Jalur Masuk')
plt.xlabel('Jalur Masuk')
plt.ylabel('Total Kunjungan')
plt.show()

"""Rata-rata dari seluruh pengunjung"""

# prompt: tampilkan rata-rata nya berapa pengunjung dari ketiga jalur masuk

# Hitung rata-rata pengunjung dari ketiga jalur
rata_rata_pengunjung = hasil_concat_dropped[['Tahunan_Udara', 'Tahunan_Darat', 'Tahunan_Laut']].mean()

# Tampilkan rata-rata pengunjung
print("Rata-rata Pengunjung dari Ketiga Jalur:")
rata_rata_pengunjung
# Menyederhanakan tampilan dengan membulatkan ke bilangan bulat
# Membulatkan ke dua angka desimal
mean_keseluruhan = round(rata_rata_pengunjung, 2)

# Tampilkan hasil yang disederhanakan ke dua angka desimal
print("Rata-rata Keseluruhan Kunjungan dari Ketiga Jalur:", mean_keseluruhan)

import matplotlib.pyplot as plt

# Data untuk rata-rata pengunjung
mean_values = rata_rata_pengunjung.values
jalur_labels = ['Udara', 'Darat', 'Laut']

# Membuat grafik batang untuk rata-rata pengunjung dari ketiga jalur
plt.figure(figsize=(8, 5))
plt.bar(jalur_labels, mean_values, color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Rata-rata Pengunjung dari Ketiga Jalur')
plt.xlabel('Jalur Masuk')
plt.ylabel('Rata-rata Pengunjung')
plt.show()

"""jalur mana yang punya bulan dengan lonjakan paling tinggi"""

import matplotlib.pyplot as plt
import seaborn as sns

# Pilih kolom-kolom bulan untuk analisis lonjakan tertinggi
kolom_bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus']

# Temukan bulan dengan nilai tertinggi pada setiap jalur
bulan_tertinggi_udara = hasil_concat_dropped[kolom_bulan].loc[hasil_concat_dropped['Tahunan_Udara'].idxmax()]
bulan_tertinggi_darat = hasil_concat_dropped[kolom_bulan].loc[hasil_concat_dropped['Tahunan_Darat'].idxmax()]
bulan_tertinggi_laut = hasil_concat_dropped[kolom_bulan].loc[hasil_concat_dropped['Tahunan_Laut'].idxmax()]

# Buat DataFrame untuk menyimpan hasil bulan lonjakan tertinggi
lonjakan_tertinggi = {
    'Jalur': ['Udara', 'Darat', 'Laut'],
    'Bulan': [bulan_tertinggi_udara.idxmax(), bulan_tertinggi_darat.idxmax(), bulan_tertinggi_laut.idxmax()],
    'Jumlah Kunjungan': [bulan_tertinggi_udara.max(), bulan_tertinggi_darat.max(), bulan_tertinggi_laut.max()]
}

df_lonjakan_tertinggi = pd.DataFrame(lonjakan_tertinggi)

# Visualisasi grafik lonjakan tertinggi per jalur
plt.figure(figsize=(10, 6))
sns.barplot(data=df_lonjakan_tertinggi, x='Jalur', y='Jumlah Kunjungan', hue='Bulan')
plt.title("Bulan dengan Lonjakan Tertinggi pada Setiap Jalur Masuk")
plt.xlabel("Jalur Masuk")
plt.ylabel("Jumlah Kunjungan")
plt.show()

"""Berdasarkan data di atas dapat disimpulkan bahwa para pengunjung lebih memilih untuk masuk ke indonesia lewat jalur udara yang mana pengunjung paling banyak ada di bulan juli"""

import pandas as pd

# Misalkan df1, df2, dan df3 sudah terdefinisi sebelumnya
df1 = jalur_udara  # DataFrame jalur_udara
df2 = jalur_darat  # DataFrame jalur_darat
df3 = jalur_laut   # DataFrame jalur_laut

# Mengganti nama kolom
df1 = df1.rename(columns={'Jalur masuk Udara': 'Jalur Masuk'})
df2 = df2.rename(columns={'Jalur masuk Darat': 'Jalur Masuk'})
df3 = df3.rename(columns={'Jalur masuk Laut': 'Jalur Masuk'})

# Menggabungkan DataFrame
df_merged = pd.concat([df1, df2, df3], ignore_index=True)

# Menambahkan kolom "Label"
df_merged.loc[df_merged['Jalur Masuk'].isin(df1['Jalur Masuk']), 'Label'] = 'Udara'
df_merged.loc[df_merged['Jalur Masuk'].isin(df2['Jalur Masuk']), 'Label'] = 'Darat'
df_merged.loc[df_merged['Jalur Masuk'].isin(df3['Jalur Masuk']), 'Label'] = 'Laut'

# Menyusun DataFrame dalam format yang diinginkan
result = df_merged[['Jalur Masuk', 'Label', 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus']]

# Menghapus baris yang berlabel 'total' dan 'total '
result = result[~result['Jalur Masuk'].isin(['total', 'total '])]

# Menampilkan DataFrame yang sudah digabung dengan cara bersih
print(result.to_string(index=False))

