# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots

color_scheme = px.colors.qualitative.Pastel

st.set_page_config(
    page_title="Prediksi Tingkat Adaptivitas Siswa dalam Pendidikan secara Online",
    page_icon="📊",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Baca dataset
dataset1 = 'students_adaptability_level_online_education.csv'
df = pd.read_csv(dataset1)

dataset = 'Data Cleaned_new.csv'
df1 = pd.read_csv(dataset)

# Sidebar untuk navigasi
with st.sidebar:
    st.header("Prediksi Tingkat Adaptivitas Siswa dalam Pendidikan secara Online")
    page_names = ['Pengenalan', 'Visualisasi Data', "Prediksi"]
    page = st.radio('Main Menu', page_names)

# Halaman Home
if page == "Pengenalan":
    st.title("Prediksi Tingkat Adaptivitas Siswa dalam Pendidikan secara Online")
    st.image('gambar.png', use_column_width=True)
    st.write("""
            <div style="text-align: justify">
            Dashboard ini berisi tentang data-data siswa yang ada pada dataset terkait faktor-faktor yang sekiranya memengaruhi adaptivitas siswa pada pendidikan secara online. 
            Data tersebut kemudian diolah atau diproses untuk membuat prediksi tingkat adaptivitas siswa yang nantinya dapat digunakan oleh pihak-pihak tertentu untuk menyesuaikan pembelajaran yang sesuai untuk siswa agar pendidikan dapat terus maju.
            </div>
            """, unsafe_allow_html=True)
    st.write("")
    st.write("""
            <div style="text-align: justify">
            Meskipun pendidikan online menawarkan fleksibilitas, para siswa harus menghadapi berbagai tantangan seperti kurangnya interaksi sosial dan kesulitan dalam mempertahankan fokus. 
            Di sinilah adaptivitas menjadi kunci utama kesuksesan. Dengan memprediksi tingkat adaptivitas siswa, kita dapat menyesuaikan pengalaman pembelajaran secara individual, 
            memastikan setiap siswa mendapatkan pendidikan yang sesuai dengan kebutuhannya. Oleh karena itu, pembuatan dashboard adaptivitas menjadi langkah yang penting dalam mendukung 
            kemajuan pendidikan di era digital ini.
            </div>
            """, unsafe_allow_html=True)
    st.write("")

    st.subheader("""
    Berikut adalah data terkait siswa yang ada:""")
    st.write(df)

    st.markdown("""
                Tabel di atas memiliki 14 kolom dan 1205 baris. Berikut adalah penjelasan untuk setiap kolom:
                1. **Gender**: Berisi jenis kelamin dari para siswa. Kolom ini memiliki nilai Boy dan Girl.
                2. **Age**: Berisi rentang usia para siswa.
                3. **Education Level**: Kolom ini berisikan tingkat institusi pendidikan siswa, seperti School, College, dan University.
                4. **Institution Type**: Berisi jenis institusi pendidikan siswa, yaitu Government (Pemerintah) atau Non Government (Bukan pemerintah).
                5. **IT Student**: Berisi pernyataan apakah siswa belajar sebagai siswa IT atau tidak (Yes or No).
                6. **Location**: Berisi pernyataan apakah lokasi siswa di kota (Yes or No).
                7. **Load-shedding**: Berisi level dari Load-shedding. Load shedding adalah keadaan dimana ketika permintaan listrik melebihi pasokan, kadang-kadang orang perlu terputus dari listrik untuk mencegah seluruh sistem runtuh. Nilai dari kolom ini ada Low dan High.
                8. **Financial Condition**: Berisi kondisi keuangan keluarga siswa. Kolom ini memiliki nilai Poor, Mid, dan Rich.
                9. **Internet Type**: Berisi jenis internet yang paling banyak digunakan dalam perangkat.
                10. **Network Type**: Berisi Jenis konektivitas jaringan, seperti 2G, 3G, dan 4G.
                11. **Class Duration**: Berisi rentang durasi kelas harian.
                12. **Self Lms**: Berisi ketersediaan LMS (Learning Management System) milik institusi.
                13. **Device**: Berisi jenis perangkat yang digunakan oleh sebagian besar siswa di kelas.
                14. **Adaptivity Level**: Berisi tingkat kemampuan beradaptasi siswa. Kolom ini merupakan kolom target.
                """)

# Halaman Visualisasi Data
elif page == "Visualisasi Data":
    selected_category = st.sidebar.selectbox("Halaman",
                                             ["Distribusi Data", "Analisis Perbandingan", "Analisis Hubungan", "Analisis Komposisi"])

    if selected_category == "Distribusi Data":
        st.subheader("Distribusi Usia Siswa Berdasarkan Tingkat Adaptivitas")
        low = df[df['Adaptivity Level'] == "Low"]

        male_age_counts = low['Age'].value_counts()

        plt.figure(figsize=(10, 6))
        plt.hist(low['Age'], bins=20, color='red', alpha=0.5, label='Low')

        plt.title('Distribusi Usia Siswa Berdasarkan Adaptivity Level Low')
        plt.xlabel('Kategori Range Usia Siswa')
        plt.ylabel('Jumlah Siswa')
        plt.legend()

        plt.grid(True)
        plt.show()
        st.pyplot()

        #####

        moderate = df[df['Adaptivity Level'] == "Moderate"]

        male_age_counts = moderate['Age'].value_counts()

        plt.figure(figsize=(10, 6))
        plt.hist(moderate['Age'], bins=20, color='orange', alpha=0.5, label='Moderate')

        plt.title('Distribusi Usia Siswa Berdasarkan Adaptivity Level Moderate')
        plt.xlabel('Kategori Range Usia Siswa')
        plt.ylabel('Jumlah Siswa')
        plt.legend()

        plt.grid(True)
        plt.show()
        st.pyplot()

        #####

        high = df[df['Adaptivity Level'] == "High"]

        male_age_counts = high['Age'].value_counts()

        plt.figure(figsize=(10, 6))
        plt.hist(high['Age'], bins=20, color='green', alpha=0.5, label='High')

        plt.title('Distribusi Usia Siswa Berdasarkan Adaptivity Level High')
        plt.xlabel('Kategori Range Usia Siswa')
        plt.ylabel('Jumlah Siswa')
        plt.legend()

        plt.grid(True)
        plt.show()
        st.pyplot()

        st.write("**Penjelasan**")
        st.markdown("""
                    <div style="text-align: justify">
                    Dari 3 (tiga) visualisasi di atas, range usia 21-25 hampir mendominasi di setiap level. Dan pada level 'High', terlihat
                    bahwa tidak ada range usia '1-5' karena tidak memungkinkan jika siswa dengan usia 1-5 mendapatkan tingkat adaptivitas tinggi,
                    mengingat itu adalah usia yang sangat-sangat muda.
                    </div>
                    """, unsafe_allow_html=True)
        st.write("")
        st.markdown("""
                    <div style="text-align: justify">
                    Dapat dilihat juga bahwa pada sumbu Y yaitu jumlah siswa pada level 'High', hanya mencapai angka 35, dimana jika dibandingkan dengan
                    level 'Low' dan 'Moderate' yang mencapai angka 140 hingga 200 itu adalah angka yang sangat kecil. Hal tersebut menandakan, bahwa masih sedikit
                    siswa yang dapat beradaptasi dengan pendidikan secara online dalam tingkat tinggi. Rata-rata hanya mencapai level 'Moderate'
                    atau bahkan 'Low'.
                    </div>
                    """, unsafe_allow_html=True)

    elif selected_category == "Analisis Perbandingan":
        st.subheader("Perbandingan Tingkat Adaptivitas berdasarkan Lama Durasi Pelajaran/Kelas")
        durasi = ['Class Duration']
        plt.figure(figsize=(15,10))

        for i, col in enumerate(durasi):
            plt.subplot(3,3,i + 1)
            ax = sns.countplot(data = df, x = col, hue = "Adaptivity Level", palette = sns.color_palette("Set1"))
        st.pyplot()

        st.markdown("**Penjelasan**")
        st.markdown("""
                    <div style="text-align: justify">
                    Secara keseluruhan, paling banyak siswa berada pada tingkat adaptivitas "Moderate" atau sedang.
                    Namun, pada durasi '0', tidak ada yang mencapai tingkat "High". 
                    Terdapat penurunan jumlah siswa yang berada pada tingkat low, moderate, dan high pada durasi kelas '3-6' jam.
                    Lamanya durasi kelas dapat berpengaruh terhadap tingkat adaptasi siswa pada pendidikan/pembelajaran secara online.
                    Tidak bisa terlalu lama atau terlalu sebentar karena dapat memengaruhi pemahaman siswa terhadap materi yang diberikan.
                    </div>
                    """, unsafe_allow_html=True)

    elif selected_category == "Analisis Hubungan":
        st.subheader("Korelasi Antara Setiap Fitur/Kolom dengan Tingkat Adaptasi Siswa")
        plt.figure(figsize=(12, 8))
        heatmap_data = df1.corr()
        sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title('Korelasi Antara Setiap Fitur/Kolom dengan Tingkat Adaptasi Siswa')
        plt.show()
        st.pyplot()

        st.write("**Penjelasan**")
        st.markdown("""
                    <div style="text-align: justify">
                    Dari visualisasi di atas, fitur/kolom yang memiliki korelasi tinggi terhadap tingkat adaptasi siswa adalah kolom "Class Duration".
                    Durasi kelas yang terlalu lama atau terlalu sebentar dapat memengaruhi pemahaman siswa terhadap materi yang diberikan sehingga dapat memengaruhi
                    tingkat adaptivitas siswa. Selain itu ada kolom "Institution Type", "Location", dan "Financial Condition". Institusi yang berasal dari pemerintahan 
                    dapat memberikan fasilitas yang berbeda terhadap para siswa nya. Tempat siswa yang berada di kota juga dapat memengaruhi tingkat adaptivitas, 
                    karena biasanya jaringan internet yang ada di kota lebih stabil. Kondisi finansial tentu dapat memengaruhi tingkat adaptivitas siswa, mengingat ada beberapa
                    hal yang perlu dipersiapkan seperti device dan internet yang memadai. Dengan device dan internet yang memadai, siswa dapat mengikuti kegiatan 
                    belajar mengajar dengan baik.
                    </div>
                    """, unsafe_allow_html=True)

    else:
        pilih = st.selectbox("Silakan pilih komposisi yang ingin ditampilkan:",
                            ["Gender", "Age", "Education Level", "Class Duration", "Adaptivity Level"])

        if pilih == "Gender":
            jumlah_Gender = df['Gender'].value_counts().reset_index()
            jumlah_Gender.columns = ['Gender', 'Jumlah']
            fig_Gender = px.pie(jumlah_Gender, names='Gender', values='Jumlah', title='Komposisi Pada Gender')
            st.plotly_chart(fig_Gender)

            st.write("**Penjelasan**")
            st.markdown("""
                        <div style="text-align: justify">
                        Pada dataset ini, terdapat lebih banyak siswa yang berjenis kelamin laki-laki. Perbedaan gender pada
                        siswa cukup berpengaruh terhadap tingkat adaptivitas nya karena terkadang terdapat perbedaan kebiasaan atau gaya
                        belajar antara siswa laki-laki dan perempuan. Pada beberapa instansi juga sering membedakan antara perlakuan dengan
                        siswa laki-laki dengan perempuan. Hal tersebut tentu dapat memengaruhi tingkat adaptivitas siswa.
                        </div>
                        """, unsafe_allow_html=True)
            
        elif pilih == "Age":
            jumlah_Age = df['Age'].value_counts().reset_index()
            jumlah_Age.columns = ['Age', 'Jumlah']
            fig_Age = px.pie(jumlah_Age, names='Age', values='Jumlah', title='Komposisi Pada Age')
            st.plotly_chart(fig_Age)

            st.write("**Penjelasan**")
            st.markdown("""
                        <div style="text-align: justify">
                        Usia tentunya akan sangat berpengaruh terhadap tingkat adaptivitas siswa. Pada usia-usia tertentu, banyak orang 
                        yang mengalami kesusahan dalam beradaptasi terhadap teknologi, mengingat pendidikan secara online pastinya akan berkaitan dengan teknologi,
                        seperti zoom, google meet, dan lain-lain. DIsini terdapat banyak siswa pada range usia 21-25 dan 11-15 karena pada usia tersebut
                        orang-orang akan lebih mudah untuk mengadopsi teknologi yang ada dan dapat mempermudah mereka dalam melakukan pendidikan secara online, sehingga
                        dapat meningkatkan tingkat adaptivitas mereka.
                        </div>
                        """, unsafe_allow_html=True)

        elif pilih == "Education Level":
            jumlah_EducationLevel = df['Education Level'].value_counts().reset_index()
            jumlah_EducationLevel.columns = ['Education Level', 'Jumlah']
            fig_EducationLevel = px.pie(jumlah_EducationLevel, names='Education Level', values='Jumlah', title='Komposisi Pada Education Level')
            st.plotly_chart(fig_EducationLevel)

            st.write("**Penjelasan**")
            st.markdown("""
                        <div style="text-align: justify">
                        Sesuai dengan range usia, paling banyak siswa berada pada tingkat pendidikan "School" dan "University". School ini mencakup seluruh siswa dari 
                        Sekolah Dasar atau setara hingga Sekolah Menengah Atas atau setaranya. Pada tingkat pendidikan tersebut, siswa pastinya lebih mudah dalam beradaptasi terhadap teknologi juga pendidikan secara online.
                        </div>
                        """, unsafe_allow_html=True)

        elif pilih == "Class Duration":
            jumlah_ClassDuration = df['Class Duration'].value_counts().reset_index()
            jumlah_ClassDuration.columns = ['Class Duration', 'Jumlah']
            fig_ClassDuration = px.pie(jumlah_ClassDuration, names='Class Duration', values='Jumlah', title='Komposisi Pada Class Duration')
            st.plotly_chart(fig_ClassDuration)

            st.write("**Penjelasan**")
            st.markdown("""
                        <div style="text-align: justify">
                        Durasi kelas pada kegiatan belajar mengajar termasuk faktor yang paling memengaruhi tingkat adaptivitas siswa. Durasi kelas yang terlalu lama 
                        akan membuat siswa menjadi bosan sehingga materi yang disampaikan tidak dapat dimengerti dengan baik. Begitupun sebaliknya, durasi kelas yang terlalu sebentar 
                        akan membuat siswa mampu memahami materi yang disampaikan. Perlu menyesuaikan waktu yang tepat dan sesuai agar seluruh siswa dapat beradaptasi dengan baik.
                        </div>
                        """, unsafe_allow_html=True)

        elif pilih == "Adaptivity Level":
            jumlah_AdaptivityLevel = df['Adaptivity Level'].value_counts().reset_index()
            jumlah_AdaptivityLevel.columns = ['Adaptivity Level', 'Jumlah']
            fig_AdaptivityLevel = px.pie(jumlah_AdaptivityLevel, names='Adaptivity Level', values='Jumlah', title='Komposisi Pada Adaptivity Level')
            st.plotly_chart(fig_AdaptivityLevel)

            st.write("**Penjelasan**")
            st.markdown("""
                        <div style="text-align: justify">
                        Dari komposisi di atas, paling banyak siswa mencapai tahap "Moderate" untuk tingkat adaptivitas nya. Dan masih sedikit siswa yang mencapai tingkat "High". Ini berarti, masih
                        banyak siswa yang kesulitan dalam beradaptasi dengan pendidikan secara online. Mengingat banyak hal yang harus disiapkan dan memerlukan adaptasi yang cukup agar dapat memahami materi yang disampaikan 
                        selama kegiatan belajar mengajar secara online.
                        </div>
                        """, unsafe_allow_html=True)

        else:
            st.write("Silakan pilih variasi.")

# Halaman Prediksi
else:
    st.subheader("Silakan Prediksi.")

    input_data = {}
    col1, col2 = st.columns(2)

    with col1:
            # Dropdown untuk kolom "Gender"
            Gender = st.selectbox('Pilih Gender', [i for i in sorted(df['Gender'].unique())])

            # Dropdown untuk kolom "Age"
            Age = st.selectbox('Pilih Range Umur (Tahun)', [i for i in sorted(df['Age'].unique())])

            # Dropdown untuk kolom "Age"
            Education_Level = st.selectbox('Pilih Tingkat Pendidikan', [i for i in sorted(df['Education Level'].unique())])

            # Dropdown untuk kolom "Institution Type"
            Institution_Type = st.selectbox('Pilh Tipe Institusi', [i for i in sorted(df['Institution Type'].unique())])

            # Dropdown untuk kolom "IT Student"
            IT_Student = st.selectbox('Apakah belajar di bidang IT?', [i for i in sorted(df['IT Student'].unique())])

            # Dropdown untuk kolom "Location"
            Location = st.selectbox('Apakah lokasi nya di Kota?', [i for i in sorted(df['Location'].unique())])

            # Dropdown untuk kolom "Load-shedding"
            Loadshedding = st.selectbox('Pilih Load-shedding', [i for i in sorted(df['Load-shedding'].unique())])

    with col2:
            # Dropdown untuk kolom "Financial Condition"
            Financial_Condition = st.selectbox('Pilih Kondisi Keuangan', [i for i in sorted(df['Financial Condition'].unique())])

            # Dropdown untuk kolom "Internet Type"
            Internet_Type = st.selectbox('Pilih Jenis Internet', [i for i in sorted(df['Internet Type'].unique())])

            # Dropdown untuk kolom "Network Type"
            Network_Type = st.selectbox('Pilih Jenis Jaringan', [i for i in sorted(df['Network Type'].unique())])

            # Dropdown untuk kolom "Class Duration"
            Class_Duration = st.selectbox('Pilih Range Durasi Kelas (Jam)', [i for i in sorted(df['Class Duration'].unique())])

            # Dropdown untuk kolom "Self Lms"
            Self_Lms = st.selectbox('Apakah institusi nya memiliki LMS sendiri?', [i for i in sorted(df['Self Lms'].unique())])

            # Dropdown untuk kolom "Device"
            Device = st.selectbox('Pilih Jenis Device', [i for i in sorted(df['Device'].unique())])

    data = pd.DataFrame({
        'Gender': [df[df['Gender'] == Gender].index[0]],
        'Age': [df[df['Age'] == Age].index[0]],
        'Education Level': [df[df['Education Level'] == Education_Level].index[0]],
        'Institution Type': [df[df['Institution Type'] == Institution_Type].index[0]],
        'IT Student': [df[df['IT Student'] == IT_Student].index[0]],
        'Location': [df[df['Location'] == Location].index[0]],
        'Load-shedding': [df[df['Load-shedding'] == Loadshedding].index[0]],
        'Financial Condition': [df[df['Financial Condition'] == Financial_Condition].index[0]],
        'Internet Type': [df[df['Internet Type'] == Internet_Type].index[0]],
        'Network Type': [df[df['Network Type'] == Network_Type].index[0]],
        'Class Duration': [df[df['Class Duration'] == Class_Duration].index[0]],
        'Self Lms': [df[df['Self Lms'] == Self_Lms].index[0]],
        'Device': [df[df['Device'] == Device].index[0]]
    })
    button = st.button('Prediksi')

    if button:
        filename='knn.pkl'
        with open(filename,'rb') as file:
            loaded_model = pickle.load(file)

        predicted = loaded_model.predict(data)
        
        if predicted[0] == 0:
            st.error("Tingkat adaptasi nya adalah Low (Rendah)")
        elif predicted[0] == 1:
            st.warning("Tingkat adaptasi nya adalah Moderate (Sedang)")
        elif predicted[0] == 2:
            st.success("Tingkat adaptasi nya adalah High (Tinggi)")
        else:
            st.write('Not Defined')
