import pandas as pd
import folium
import os

# Dapatkan path absolut direktori script saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Baca data dari file CSV dengan path absolut
csv_file = os.path.join(current_dir, 'data_cangkringan.csv')
data = pd.read_csv(csv_file)

# Buat peta terpusat di Kecamatan Cangkringan, Yogyakarta
m = folium.Map(location=[-7.6079, 110.4415], zoom_start=12)

# Tambahkan marker untuk setiap lokasi pada data CSV
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['nama_lokasi']
    ).add_to(m)

# Simpan peta ke file HTML dengan path absolut
target_file = os.path.join(current_dir, 'peta_cangkringan.html')
m.save(target_file)
print(f"Peta berhasil disimpan ke {target_file}")
