# Peta Lokasi Cangkringan

Aplikasi visualisasi interaktif berbasis Streamlit untuk menampilkan lokasi-lokasi penting di Kecamatan Cangkringan, Yogyakarta.

## Tentang Aplikasi

Aplikasi ini menyediakan peta interaktif menampilkan berbagai lokasi di Kecamatan Cangkringan menggunakan data koordinat geografis (latitude dan longitude). Pengguna dapat melihat setiap lokasi pada peta dan mendapatkan informasi tambahan saat mengklik marker lokasi.

## Fitur

- Visualisasi data lokasi dalam bentuk tabel
- Peta interaktif berbasis Folium
- Marker untuk setiap lokasi dengan popup informasi
- Tampilan responsif yang kompatibel dengan berbagai perangkat

## Teknologi

Aplikasi ini dibangun menggunakan:
- [Streamlit](https://streamlit.io/) - Framework untuk aplikasi data berbasis Python
- [Folium](https://python-visualization.github.io/folium/) - Library Python untuk visualisasi data geospasial
- [Pandas](https://pandas.pydata.org/) - Library Python untuk analisis data

## Instalasi

1. Clone repositori ini:
   ```
   git clone https://github.com/username/cangkringan.git
   cd cangkringan
   ```

2. Buat virtual environment (disarankan):
   ```
   python -m venv venv
   source venv/bin/activate  # Di Windows gunakan: venv\\Scripts\\activate
   ```

3. Install dependensi:
   ```
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi:
   ```
   streamlit run peta.py
   ```

## Struktur File

```
cangkringan/
├── peta.py                # File utama aplikasi
├── data_cangkringan.csv   # Dataset lokasi
├── README.md              # Dokumentasi
└── requirements.txt       # Dependensi proyek
```

## Penggunaan

Setelah menjalankan aplikasi, Streamlit akan membuka browser secara otomatis. Anda dapat:
- Melihat data dalam bentuk tabel
- Berinteraksi dengan peta untuk melihat lokasi
- Mengklik marker untuk melihat nama lokasi

## Dataset

File `data_cangkringan.csv` berisi informasi lokasi dengan struktur:
- `nama_lokasi`: Nama tempat
- `latitude`: Koordinat lintang lokasi
- `longitude`: Koordinat bujur lokasi

## Pembaruan Terakhir

Data terakhir diperbarui: April 2025

## Kontribusi

Kontribusi untuk meningkatkan dataset atau fungsionalitas aplikasi sangat diapresiasi. Silakan buat pull request atau diskusikan ide pengembangan melalui issue.

## Lisensi

[MIT](https://choosealicense.com/licenses/mit/)
