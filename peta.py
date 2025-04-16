import pandas as pd
import folium
from folium.plugins import MarkerCluster
import os
import streamlit as st
from streamlit_folium import st_folium
import datetime
import matplotlib.pyplot as plt
import numpy as np
from branca.element import Figure

# Get current directory for file paths
current_dir = os.path.dirname(os.path.abspath(__file__))

# This MUST be the first st.* call in your script
st.set_page_config(
    page_title="Data Sapi Perah di Cangkringan",
    page_icon="🐄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Get current year for the footer
current_year = datetime.datetime.now().year

# Custom CSS styling (must come AFTER st.set_page_config)
st.markdown("""
<style>
    .main {
        background-color: #f5f7f9;
        padding: 2rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #2e7d32;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton button {
        background-color: #2e7d32;
        color: white;
        border-radius: 5px;
    }
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    /* Card styling */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    /* Cow themed styling */
    .cow-pattern {
        background-color: white;
        border: 3px solid #6d4c41;
        border-radius: 10px;
        padding: 15px;
        position: relative;
    }
    .cow-pattern::before {
        content: "🐄";
        position: absolute;
        right: 10px;
        top: 10px;
        font-size: 24px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for navigation and filters
with st.sidebar:
    st.title("Navigasi")
    
    # Navigation options
    page = st.radio(
        "Pilih Halaman:",
        ["Beranda", "Peta Interaktif", "Statistik", "Tentang"]
    )
    
    st.markdown("""<div class="cow-pattern" style="color: black;">
    <h3>Tentang Aplikasi</h3>
    <p style="color: black;">Aplikasi ini menampilkan data persebaran sapi perah di Kecamatan Cangkringan, Yogyakarta.</p>
    </div>""", unsafe_allow_html=True)

# Main content
if page == "Beranda":
    # Create two columns for the header
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.title("Peta Lokasi Sapi Perah Cangkringan")
        st.markdown("""
        <div class="card">
        <p><p style="color: black;">Visualisasi interaktif persebaran dan data peternakan sapi perah di Kecamatan Cangkringan, Yogyakarta. 
        Data ini dikumpulkan pada April 2025 dan mencakup informasi tentang lokasi peternakan serta jumlah sapi.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Could be a logo or quick stats
        st.markdown("""
        <div style="text-align:center; padding:20px;">
            <span style="font-size:60px;">🐄</span>
            <h3>Data April 2025</h3>
        </div>
        """, unsafe_allow_html=True)
    
    # Dapatkan path absolut direktori script saat ini
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Baca data dari file CSV dengan path absolut
    csv_file = os.path.join(current_dir, 'data_cangkringan.csv')
    data = pd.read_csv(csv_file)
    
    # Quick stats in cards
    st.markdown("<h2>Statistik Ringkas</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <h1><p><p style="color: black;">{len(data)}</h1>
            <p><p style="color: black;">Jumlah Lokasi Peternakan</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Assuming your data has a 'jumlah_sapi' column, if not, you'll need to modify this
        if 'jumlah_sapi' in data.columns:
            total_sapi = data['jumlah_sapi'].sum()
        else:
            total_sapi = "N/A"
            
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <h1><p><p style="color: black;">{total_sapi}</h1>
            <p><p style="color: black;">Total Sapi Perah</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Assuming data has 'desa' column, if not, you'll need to modify this
        if 'desa' in data.columns:
            total_desa = data['desa'].nunique()
        else:
            total_desa = "N/A"
            
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <h1><p><p style="color: black;">{total_desa}</h1>
            <p><p style="color: black;">Total Desa</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Table with improved styling
    st.markdown("<h2>Data Peternakan</h2>", unsafe_allow_html=True)
    
    # Add search functionality
    search = st.text_input("Cari lokasi peternakan:")
    if search:
        filtered_data = data[data['nama_lokasi'].str.contains(search, case=False)]
    else:
        filtered_data = data
    
    # Display table with custom styling
    st.dataframe(
        filtered_data,
        use_container_width=True,
        height=400
    )

elif page == "Peta Interaktif":
    st.title("Peta Interaktif Lokasi Sapi Perah Kecamatan Cangkringan")
    
    # Dapatkan path absolut direktori script saat ini
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Baca data dari file CSV dengan path absolut
    csv_file = os.path.join(current_dir, 'data_cangkringan.csv')
    data = pd.read_csv(csv_file)
    
    # Buat peta terpusat di Kecamatan Cangkringan, Yogyakarta
    m = folium.Map(location=[-7.6079, 110.4415], zoom_start=12)

    # Tambahkan marker untuk setiap lokasi pada data CSV dengan informasi lengkap
    for idx, row in data.iterrows():
        # Pastikan latitude negatif (karena di selatan ekuator)
        lat = -abs(row['latitude'])  # Memastikan nilai latitude negatif
        lon = row['longitude']
        
        # Buat popup dengan informasi lengkap dari data CSV
        popup_html = f"""
        <div style="width:250px">
            <h4 style="color:#2e7d32; margin-bottom:10px">{row['nama_lokasi']}</h4>
            <p><b>Alamat:</b> {row['alamat']}</p>
            <p><b>Desa:</b> {row['desa']}</p>
            <p><b>Jumlah Sapi:</b> {row['jumlah_sapi']} ekor</p>
            <p><b>Produksi Susu:</b> {row['produksi_susu']} liter/hari</p>
            <p><b>Koordinat:</b> {lat}, {lon}</p>
        </div>
        """
        
        # Buat popup dengan custom styling
        popup = folium.Popup(popup_html, max_width=300)
        
        # Tambahkan marker ke peta
        folium.Marker(
            location=[lat, lon],
            popup=popup,
            tooltip=row['nama_lokasi']
        ).add_to(m)
    
    # Tambahkan kontrol layer
    folium.LayerControl().add_to(m)
    
    # Display the map in Streamlit
    st_folium(
        m, 
        width=800,
        height=600
    )

elif page == "Statistik":
    st.title("Statistik Peternakan Sapi Perah")
    
    # Dapatkan path absolut direktori script saat ini
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Baca data dari file CSV dengan path absolut
    csv_file = os.path.join(current_dir, 'data_cangkringan.csv')
    data = pd.read_csv(csv_file)
    
    # Check if necessary columns exist, create example columns if they don't
    if 'jumlah_sapi' not in data.columns:
        st.warning("Data tidak memiliki kolom jumlah_sapi, menggunakan data contoh.")
        data['jumlah_sapi'] = pd.Series([5, 10, 15, 8, 12] * (len(data) // 5 + 1))[:len(data)]
    
    if 'desa' not in data.columns:
        st.warning("Data tidak memiliki kolom desa, menggunakan data contoh.")
        data['desa'] = pd.Series(['Argomulyo', 'Glagaharjo', 'Kepuharjo', 'Umbulharjo', 'Wukirsari'] * (len(data) // 5 + 1))[:len(data)]
    
    if 'produksi_susu' not in data.columns:
        st.warning("Data tidak memiliki kolom produksi_susu, menggunakan data contoh.")
        data['produksi_susu'] = data['jumlah_sapi'] * 15 + pd.Series(pd.np.random.randint(-20, 50, size=len(data)))
    
    # Create tabs for different types of visualizations
    tab1, tab2, tab3 = st.tabs(["Distribusi Sapi per Desa", "Produksi Susu", "Peternakan Terbesar"])
    
    with tab1:
        st.subheader("Distribusi Sapi Perah per Desa")
        
        # Calculate distribution by village
        desa_distribution = data.groupby('desa')['jumlah_sapi'].sum().reset_index()
        
        # Create a bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(desa_distribution['desa'], desa_distribution['jumlah_sapi'], color='#2e7d32')
        ax.set_xlabel('Desa')
        ax.set_ylabel('Jumlah Sapi')
        ax.set_title('Distribusi Sapi Perah per Desa')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        st.pyplot(fig)
        
        # Display the data as a table as well
        st.dataframe(desa_distribution, use_container_width=True)
    
    with tab2:
        st.subheader("Produksi Susu per Peternakan")
        
        # Add a slider to filter the data
        min_produksi = int(data['produksi_susu'].min())
        max_produksi = int(data['produksi_susu'].max())
        
        produksi_threshold = st.slider(
            "Filter berdasarkan produksi susu minimal (liter/hari):",
            min_produksi, max_produksi, min_produksi
        )
        
        # Filter data based on the threshold
        filtered_data = data[data['produksi_susu'] >= produksi_threshold]
        
        # Create a horizontal bar chart
        fig, ax = plt.subplots(figsize=(10, 8))
        bars = ax.barh(filtered_data['nama_lokasi'], filtered_data['produksi_susu'], color='#8bc34a')
        ax.set_xlabel('Produksi Susu (liter/hari)')
        ax.set_ylabel('Nama Peternakan')
        ax.set_title('Produksi Susu per Peternakan')
        
        # Add the values at the end of each bar
        for i, v in enumerate(filtered_data['produksi_susu']):
            ax.text(v + 5, i, str(int(v)), va='center')
            
        plt.tight_layout()
        
        st.pyplot(fig)
    
    with tab3:
        st.subheader("10 Peternakan Terbesar")
        
        # Sort data by number of cows
        largest_farms = data.sort_values('jumlah_sapi', ascending=False).head(10)
        
        # Create a pie chart
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.pie(
            largest_farms['jumlah_sapi'], 
            labels=largest_farms['nama_lokasi'], 
            autopct='%1.1f%%',
            startangle=90,
            shadow=True,
            colors=plt.cm.Greens(np.linspace(0.35, 0.65, len(largest_farms)))
        )
        ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
        plt.title('Persentase Sapi di 10 Peternakan Terbesar')
        
        st.pyplot(fig)
        
        # Display the data as a table as well
        st.markdown("##### Detail 10 Peternakan Terbesar")
        st.dataframe(
            largest_farms[['nama_lokasi', 'jumlah_sapi', 'produksi_susu']], 
            use_container_width=True
        )

else:  # About page
    st.title("Tentang Aplikasi")
    
    st.markdown("""
    <div class="card">
        <h3><p style="color: black;">Peta Lokasi Sapi Perah Cangkringan</h3>
        
        Aplikasi ini dikembangkan untuk memvisualisasikan persebaran peternakan sapi perah di Kecamatan Cangkringan, Yogyakarta. 
        Dengan memanfaatkan teknologi pemetaan interaktif, aplikasi ini memudahkan pemangku kepentingan dalam melihat distribusi
        peternakan sapi perah dan menganalisis potensi pengembangan industri susu di wilayah tersebut.</p>
        
        Fitur:
        Visualisasi data peternakan dalam bentuk tabel interaktif
        Peta interaktif dengan marker lokasi peternakan
        Statistik dan diagram persebaran sapi perah per desa
        Analisis produksi susu dari setiap peternakan
        Informasi tentang peternakan terbesar di wilayah Cangkringan
        
        Sumber Data:
        Data dalam aplikasi ini dikumpulkan melalui survei lapangan dan koordinasi dengan Dinas Peternakan setempat 
        pada bulan April 2025.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card cow-pattern">
        <h3><p style="color: black;">Kontak</h3>
        <p style="color: black;">Untuk informasi lebih lanjut atau pertanyaan terkait data, silakan hubungi:</p>
        <p style="color: black;"><b>Email:</b> info@sapiperancangkringan.id</p>
        <p style="color: black;"><b>Telepon:</b> +62 274 123456</p>
    </div>
    """, unsafe_allow_html=True)

# Footer section
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

# Hide default Streamlit style elements
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
