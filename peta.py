import pandas as pd
import folium
import os
import streamlit as st
from streamlit_folium import folium_static

# Set judul aplikasi
st.title("Peta Lokasi Cangkringan")
st.write("Visualisasi peta lokasi di Kecamatan Cangkringan, Yogyakarta")

# Dapatkan path absolut direktori script saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Baca data dari file CSV dengan path absolut
csv_file = os.path.join(current_dir, 'data_cangkringan.csv')
data = pd.read_csv(csv_file)

# Tampilkan data dalam tabel
st.subheader("Data Lokasi")
st.dataframe(data)

# Buat peta terpusat di Kecamatan Cangkringan, Yogyakarta
st.subheader("Peta Lokasi")
m = folium.Map(location=[-7.6079, 110.4415], zoom_start=12)

# Tambahkan marker untuk setiap lokasi pada data CSV
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['nama_lokasi']
    ).add_to(m)

# Tampilkan peta di aplikasi Streamlit
folium_static(m)

# Tampilkan informasi tambahan
st.info("Data terakhir diperbarui: April 2025")
