import pandas as pd
import folium
import os
import streamlit as st
from streamlit_folium import st_folium
import datetime

# Get current year for the footer
current_year = datetime.datetime.now().year

st.set_page_config(
    page_title="Data Sapi Perah di Cangkringan",
    page_icon="./assets/sapi_favicon.png",
)

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
st_folium(m, width=725)

# Tampilkan informasi tambahan
st.info("Data terakhir diperbarui: April 2025")

# Footer with LinkedIn profile link and improved styling
st.markdown("""
<hr style="height:1px;border:none;color:#333;background-color:#333;margin-top:30px;margin-bottom:20px">
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center; padding:15px; margin-top:10px; margin-bottom:20px">
    <p style="font-size:16px; color:#555">
        © {current_year} Developed by: 
        <a href="https://www.linkedin.com/in/galuh-adi-insani-1aa0a5105/" target="_blank" 
           style="text-decoration:none; color:#0077B5; font-weight:bold">
            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" 
                 width="16" height="16" style="vertical-align:middle; margin-right:5px">
            Galuh Adi Insani
        </a> 
        with <span style="color:#e25555">❤️</span>
    </p>
    <p style="font-size:12px; color:#777">All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

# Hide Streamlit style
hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)
