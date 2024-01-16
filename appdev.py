from flask import Flask, request, render_template, redirect, session,make_response,url_for
from flask_mysqldb import MySQL
import re
from datetime import timedelta
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics.pairwise import cosine_similarity
from random import choices
import random
import string
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from fpdf import FPDF
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.exceptions import abort
import numpy as np




app = Flask(__name__)


# MySQL configurations
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='physic'
app.config['STATIC_FOLDER'] = '/static'


# Secret key for session management
app.secret_key = 'bebas'

# Initialize MySQL
mysql = MySQL(app)

msg=''

# Function to check if user is logged in
def is_logged_in():
    return 'username' in session

#NLP Sastrawi 
# Fungsi untuk melakukan case folding
def case_folding(text):
    return text.lower()

# Fungsi untuk melakukan stemming
def stemming(text):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in text]
    return stemmed_words

factory = StemmerFactory()
stemmer = factory.create_stemmer()


#COSIN SIMILARITY
def cosine_sim(text1, text2):
    corpus = [text1, text2]
    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(corpus)
    similarity = cosine_similarity(cv_matrix)
    return similarity[0][1]


def train_logistic_regression(X_train, y_train):
    # Inisialisasi model logistic regression
    model = LogisticRegression()
    # Train model dengan data latih
    model.fit(X_train, y_train)
    return model


def preprocess_text(text):
    # Case folding
    text = text.lower()

    # Stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    text = stemmer.stem(text)
    return text

app.permanent_session_lifetime = timedelta(days=1)  # Atur sesuai kebutuhan

# Fungsi untuk menggenerate kode 5 digit
# Fungsi untuk menggenerate kode 5 digit
def generate_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(5))
    return code

# Fungsi untuk menyimpan kode ke database
def save_code(username,nama, kelas, tanggal, kode):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO kode (username, dosen, kelas, tanggal, kode) VALUES (%s,%s,%s,%s,%s)", (username,nama, kelas, tanggal, kode))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error:", e)
        return False
# Fungsi untuk mengambil data skor siswa dari database MySQL


def remove_html_tags(text):
    # Definisikan pola regex untuk mencari tag HTML, termasuk &nbsp;
    pattern = r"<\/?(p|span|br|sup|sub|sum)[^>]*>|&nbsp;|;"
    # Ganti tag HTML dengan string kosong
    clean_text = re.sub(pattern, "", text)
    return clean_text


def get_linier_regression(input_text):
    # Buat koneksi ke database MySQL
    cursor = mysql.connection.cursor()

    # Query data dari database MySQL
    cursor.execute("SELECT jawaban, labels FROM soal_2")
    data = cursor.fetchall()

    # Buat array numpy untuk metadata jawaban
    metadata = [
        {"answer": data[i][0], "label": data[i][1]} for i in range(len(data))
    ]

    # Buat model regresi linier
    model = LinearRegression()

    # Latih model dengan metadata jawaban
    model.fit(metadata, np.array([data[i][1] for i in range(len(data))])[:, None])

    # Prediksi label untuk teks inputan
    label = model.predict(np.array([input_text]).reshape(1, -1))

    return label[0][0]


#menu utaman index steam-ea
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/panduan')
def panduan():
    return render_template('test.html')





#login Mahasiswa 
#sistem bagian mahasiswa

@app.route('/register/siswa', methods=['GET', 'POST'])
def registersiswa():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        

        # Check if account exists using MySQL
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM login_siswa WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO login_siswa VALUES (NULL, %s, %s, %s)', (username,email,password))
            conn.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register_siswa.html', msg=msg)


#login mahasiswa
@app.route('/login/siswa', methods=['GET', 'POST'])
def loginsiswa():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM login_siswa WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # If the user exists, store the username in the session
            session['username'] = user[1]
            return redirect(url_for('dashboardmahasiswa'))
        else:
            return 'Invalid login credentials. Please try again.'

    return render_template('login-mahasiswa.html')

# Function to connect to MySQL and retrieve data
def get_data(username):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT Chapter FROM hasil_siswa WHERE username = %s ORDER BY time DESC LIMIT 6", (username,))
        results = cursor.fetchall()
        data = [result[0] for result in results]
        return data
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None
    finally:
        cursor.close()

def get_data_from_mysql(username):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT skor FROM hasil_siswa WHERE username = %s ORDER BY time DESC LIMIT 6", (username,))
        results = cursor.fetchall()
        data = [result[0] for result in results]
        return data
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None
    finally:
        cursor.close()

def hitung_rata_rata(username):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT selesai FROM hasil_siswa WHERE username = %s ORDER BY time DESC LIMIT 5", (username,))
        results = cursor.fetchall()

        total = 0
        for row in results:
            total += row[0]

        rata_rata = total / len(results) if results else 0
        return rata_rata
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None
    finally:
        cursor.close()




#dashbord mahasiswa
@app.route('/dashboard/siswa')
def dashboardmahasiswa():
    if 'username' not in session:
        return redirect('/')
    username = session['username']
   
    labels = get_data(username)

    # Get data from MySQL
    data = get_data_from_mysql(username)
    # Ambil id mahasiswa berdasarkan username
    cursor = mysql.connection.cursor()
    # Ambil riwayat ujian dari tabel riwayat_ujian berdasarkan mahasiswa_id
    cursor.execute("SELECT kode, chapter, skor, nilai, time FROM hasil_siswa WHERE username = %s ORDER BY time DESC LIMIT 6", (username,))
    riwayat_ujian = cursor.fetchall()
    cursor.close()


    ratarata = hitung_rata_rata(username)
    tidak = 100 - ratarata
    
    return render_template(template_name_or_list='student-exam.html', username=username,data=data,labels=labels, riwayat_ujian=riwayat_ujian,ratarata=ratarata,tidak=tidak)




#dashbord mahasiswa
@app.route('/profil/mahasiswa', methods=['GET', 'POST'])
def profilmahasiswa():
    if 'username' not in session:
        return redirect('/')

    username = session['username']

    if request.method == 'POST':
        name = request.form['nama']
        nim = request.form['nim']
        user = request.form['user']
        email = request.form['email']
        univ = request.form['universitas']
        prodi = request.form['prodi']
        alamat = request.form['alamat']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM profil_siswa WHERE username = %s', (username,))
        existing_profile = cursor.fetchone()

        if existing_profile:
            # Jika profil sudah ada, perbarui profil
            cursor.execute('UPDATE profil_siswa SET nama = %s, nim = %s, user = %s, email = %s, universitas = %s, prodi = %s, alamat = %s WHERE username = %s', (name, nim, user, email, univ, prodi, alamat, username))
        else:
            # Jika profil belum ada, buat profil baru
            cursor.execute('INSERT INTO profil_siswa (username, nama, nim, user, email, universitas, prodi, alamat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (username, name, nim, user, email, univ, prodi, alamat))

        # Commit perubahan ke database
        mysql.connection.commit()
        cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT nama, nim, user, email, universitas, prodi, alamat FROM profil_siswa WHERE username = %s', (username,))
    profile = cursor.fetchone()
    cursor.close()

    return render_template('student-profil.html', username=username, profile=profile)


@app.route('/ujian/mahasiswa')
def ujianmahasiswa():
    if 'username' not in session:
        return redirect('/')

    username = session['username']

    # Dapatkan data nilai dari database berdasarkan username pengguna

    return render_template('student-ujian.html', username=username)


@app.route('/ujian/tahap1', methods=['GET', 'POST'])
def fluida1():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    if request.method == 'POST':
        nama = request.form['user']
        kode = request.form['kelas']
        chapter = request.form.getlist('checkbox')  # Menggunakan getlist karena bisa ada beberapa pilihan yang dipilih
        ganda1 = request.form['content1']
        tg1 = 100

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT jawaban, labels FROM db_soal")
        argumen_data = cursor.fetchall()
        argumen_jawaban = [preprocess_text(data[0]) for data in argumen_data]
        argumen_labels = [data[1] for data in argumen_data]

        input_text_list01 = [remove_html_tags(ganda1)]
        input_text_list1 = [preprocess_text(text) for text in input_text_list01]

        vectorizer = CountVectorizer()
        database_vectorized = vectorizer.fit_transform(argumen_jawaban)

        models = []
        for _ in range(1):
            model = train_logistic_regression(database_vectorized, argumen_labels)
            models.append(model)

        predictions1 = [model.predict(vectorizer.transform(input_text_list1))[0] for model in models]

        argumen_predictions1 = []
        argumen_predictionsPK = []
        argumen_predictionsKT = []
        

        for prediction in predictions1:
            # Konversi prediksi menjadi label yang lebih bermakna
            if prediction == 1:
                argumen_predictions1.append(1)
            elif prediction == 2:
                argumen_predictions1.append(2)
            elif prediction == 3:
                argumen_predictions1.append(3)
            elif prediction == 4:
                argumen_predictions1.append(4)
            elif prediction == 0:
                argumen_predictions1.append(0)
            else:
                argumen_predictions1.append(1)


        for prediction in predictions1:
            if prediction == 1:
                argumen_predictionsPK.append("Tidak paham")
            elif prediction == 2:
                argumen_predictionsPK.append("Miskonsepsi spesifik")
            elif prediction == 3:
                argumen_predictionsPK.append("Pemahaman sebagian")
            elif prediction == 4:
                argumen_predictionsPK.append("Pemahaman keseluruhan")
            elif prediction == 0:
                argumen_predictionsPK.append("Tidak ada jawaban")
            else:
                argumen_predictionsPK.append("Tidak paham")

        for prediction in predictions1:
            if prediction == 1:
                argumen_predictionsKT.append("Mengulangi sebagian dari, atau seluruh pertanyaan atau tanggapan yang tidak relevan")
            elif prediction == 2:
                argumen_predictionsKT.append("Respons sebagian besar mencakup informasi deskriptif, tidak benar, atau tidak logis.")
            elif prediction == 3:
                argumen_predictionsKT.append("Jawaban mencakup setidaknya sebagian besar dari ide-ide yang dapat diterima dan menunjukkan pemahaman konsep, akan tetapi juga mengandung beberapa kesalahpahaman.")
            elif prediction == 4:
                argumen_predictionsKT.append("Jawaban mencakup semua komponen atau sebagian besar dari Jawaban dapat diterima secara ilmiah")
            elif prediction == 0:
                argumen_predictionsKT.append("Tidak ada jawaban")
            else:
                argumen_predictionsKT.append("Mengulangi sebagian dari, atau seluruh pertanyaan atau tanggapan yang tidak relevan")

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT jawaban, labels FROM db_soal")
        first_row = cursor.fetchone()
        if first_row:
            jawaban = first_row[0]
        else:
            jawaban = ("Tidak ada data ditemukan")
        cursor.close()


        cursor = mysql.connection.cursor()
        cursor.execute("SELECT dosen FROM kode WHERE kode = %s", (kode,))
        guru = cursor.fetchone()[0]  # Mengambil hasil query dari tuple

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO hasil_siswa (username, nama, kode, Chapter, jawaban,jawabandb, skor,nilai,keterangan,guru,selesai) VALUES (%s, %s,%s, %s,%s,%s,%s, %s,%s,%s,%s)", (username, nama, kode,chapter,input_text_list01,jawaban,argumen_predictions1,argumen_predictionsPK,argumen_predictionsKT,guru,tg1))
        mysql.connection.commit()
        cursor.close()

        
        metadata_cursor = mysql.connection.cursor()
        metadata_cursor.execute("INSERT INTO db_soal (jawaban, labels) VALUES (%s, %s)", (input_text_list01[0], argumen_predictions1[0]))
        mysql.connection.commit()
        metadata_cursor.close()

        session['kode'] = kode
        session['chapter'] = chapter
        session['id'] = cursor.lastrowid
        return redirect(url_for('hasil1'))


    return render_template('statis_1.html', username=username)


  
@app.route('/hasil/pemahaman/konsep', methods=['GET', 'POST'])
def hasil1():
    if 'username' not in session:
        return redirect('/')
    username = session['username']
    kode = session.get('kode')
    chapter = session.get('chapter')
    id = session.get('id')
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT nilai FROM hasil_siswa WHERE id = %s AND username = %s AND kode = %s AND Chapter = %s', (id, username, kode, chapter))
    data = cursor.fetchone()
    cursor.close()

    return render_template('skor.html', username=username, data=data)


@app.route('/ujian/tahap2', methods=['GET', 'POST'])
def fluida2():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    if request.method == 'POST':
        nama = request.form['user']
        kode = request.form['kelas']
        chapter = request.form.getlist('checkbox')  # Menggunakan getlist karena bisa ada beberapa pilihan yang dipilih
        ganda1 = request.form['content1']
        tg1 = 100

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT jawaban, labels FROM soal_2")
        argumen_data = cursor.fetchall()
        argumen_jawaban = [preprocess_text(data[0]) for data in argumen_data]
        argumen_labels = [data[1] for data in argumen_data]

        input_text_list01 = [remove_html_tags(ganda1)]
        input_text_list1 = [preprocess_text(text) for text in input_text_list01]

        vectorizer = CountVectorizer()
        database_vectorized = vectorizer.fit_transform(argumen_jawaban)

        models = []
        for _ in range(1):
            model = train_logistic_regression(database_vectorized, argumen_labels)
            models.append(model)

        predictions1 = [model.predict(vectorizer.transform(input_text_list1))[0] for model in models]

        argumen_predictions1 = []
        argumen_predictionsPK = []

        for prediction in predictions1:
            # Konversi prediksi menjadi label yang lebih bermakna
            if prediction == 1:
                argumen_predictions1.append(1)
            elif prediction == 2:
                argumen_predictions1.append(2)
            elif prediction == 3:
                argumen_predictions1.append(3)
            elif prediction == 4:
                argumen_predictions1.append(4)
            else:
                argumen_predictions1.append(1)

        for prediction in predictions1:
            if prediction == 1:
                argumen_predictionsPK.append("Tidak paham")
            elif prediction == 2:
                argumen_predictionsPK.append("Miskonsepsi spesifik")
            elif prediction == 3:
                argumen_predictionsPK.append("Pemahaman sebagian")
            elif prediction == 4:
                argumen_predictionsPK.append("Pemahaman keseluruhan")
            else:
                argumen_predictionsPK.append("Tidak paham")
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT dosen FROM kode WHERE kode = %s", (kode,))
        guru = cursor.fetchone()  # Mengambil hasil query dari tuple


        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO hasil_siswa (username, nama, kode, Chapter, jawaban, skor,nilai,guru,selesai) VALUES (%s, %s,%s, %s,%s, %s,%s,%s,%s)", (username, nama, kode,chapter,input_text_list01,argumen_predictions1,argumen_predictionsPK,guru,tg1))
        mysql.connection.commit()
        cursor.close()

        metadata_cursor = mysql.connection.cursor()
        metadata_cursor.execute("INSERT INTO soal_2 (jawaban, labels) VALUES (%s, %s)", (input_text_list01[0], argumen_predictions1[0]))
        mysql.connection.commit()
        metadata_cursor.close()

        session['kode'] = kode
        session['chapter'] = chapter
        session['id'] = cursor.lastrowid
        return redirect(url_for('hasil1'))
    
    return render_template('statis_2.html', username=username)

@app.route('/ujian/tahap3', methods=['GET', 'POST'])
def fluida3():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    if request.method == 'POST':
        nama = request.form['user']
        kode = request.form['kelas']
        chapter = request.form.getlist('checkbox')  # Menggunakan getlist karena bisa ada beberapa pilihan yang dipilih
        ganda1 = request.form['content1']
        tg1 = 100

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT jawaban, labels FROM soal_3")
        argumen_data = cursor.fetchall()
        argumen_jawaban = [preprocess_text(data[0]) for data in argumen_data]
        argumen_labels = [data[1] for data in argumen_data]

        input_text_list01 = [remove_html_tags(ganda1)]
        input_text_list1 = [preprocess_text(text) for text in input_text_list01]

        vectorizer = CountVectorizer()
        database_vectorized = vectorizer.fit_transform(argumen_jawaban)

        models = []
        for _ in range(1):
            model = train_logistic_regression(database_vectorized, argumen_labels)
            models.append(model)

        predictions1 = [model.predict(vectorizer.transform(input_text_list1))[0] for model in models]

        argumen_predictions1 = []
        argumen_predictionsPK = []

        for prediction in predictions1:
            # Konversi prediksi menjadi label yang lebih bermakna
            if prediction == 1:
                argumen_predictions1.append(1)
            elif prediction == 2:
                argumen_predictions1.append(2)
            elif prediction == 3:
                argumen_predictions1.append(3)
            elif prediction == 4:
                argumen_predictions1.append(4)
            else:
                argumen_predictions1.append(1)

        for prediction in predictions1:
            if prediction == 1:
                argumen_predictionsPK.append("Tidak paham")
            elif prediction == 2:
                argumen_predictionsPK.append("Miskonsepsi spesifik")
            elif prediction == 3:
                argumen_predictionsPK.append("Pemahaman sebagian")
            elif prediction == 4:
                argumen_predictionsPK.append("Pemahaman keseluruhan")
            else:
                argumen_predictionsPK.append("Tidak paham")
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT dosen FROM kode WHERE kode = %s", (kode,))
        guru = cursor.fetchone()[0]  # Mengambil hasil query dari tuple


        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO hasil_siswa (username, nama, kode, Chapter, jawaban, skor,nilai,guru,selesai) VALUES (%s,%s, %s,%s, %s,%s, %s,%s,%s)", (username, nama, kode,chapter,input_text_list01,argumen_predictions1,argumen_predictionsPK,guru,tg1))
        mysql.connection.commit()
        cursor.close()

        metadata_cursor = mysql.connection.cursor()
        metadata_cursor.execute("INSERT INTO soal_3 (jawaban, labels) VALUES (%s, %s)", (input_text_list01[0], argumen_predictions1[0]))
        mysql.connection.commit()
        metadata_cursor.close()

        session['kode'] = kode
        session['chapter'] = chapter
        session['id'] = cursor.lastrowid
        return redirect(url_for('hasil1'))

    return render_template('statis_3.html', username=username)
  


@app.route('/ujian/tahap4', methods=['GET', 'POST'])
def fluida4():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    if request.method == 'POST':
        nama = request.form['user']
        kode = request.form['kelas']
        chapter = request.form.getlist('checkbox')  # Menggunakan getlist karena bisa ada beberapa pilihan yang dipilih
        ganda1 = request.form['content1']
        tg1 = 100

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT jawaban, labels FROM soal_4")
        argumen_data = cursor.fetchall()
        argumen_jawaban = [preprocess_text(data[0]) for data in argumen_data]
        argumen_labels = [data[1] for data in argumen_data]

        input_text_list01 = [remove_html_tags(ganda1)]
        input_text_list1 = [preprocess_text(text) for text in input_text_list01]

        vectorizer = CountVectorizer()
        database_vectorized = vectorizer.fit_transform(argumen_jawaban)

        models = []
        for _ in range(1):
            model = train_logistic_regression(database_vectorized, argumen_labels)
            models.append(model)

        predictions1 = [model.predict(vectorizer.transform(input_text_list1))[0] for model in models]

        argumen_predictions1 = []
        argumen_predictionsPK = []

        for prediction in predictions1:
            # Konversi prediksi menjadi label yang lebih bermakna
            if prediction == 1:
                argumen_predictions1.append(1)
            elif prediction == 2:
                argumen_predictions1.append(2)
            elif prediction == 3:
                argumen_predictions1.append(3)
            elif prediction == 4:
                argumen_predictions1.append(4)
            else:
                argumen_predictions1.append(1)

        for prediction in predictions1:
            if prediction == 1:
                argumen_predictionsPK.append("Tidak paham")
            elif prediction == 2:
                argumen_predictionsPK.append("Miskonsepsi spesifik")
            elif prediction == 3:
                argumen_predictionsPK.append("Pemahaman sebagian")
            elif prediction == 4:
                argumen_predictionsPK.append("Pemahaman keseluruhan")
            else:
                argumen_predictionsPK.append("Tidak paham")
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT dosen FROM kode WHERE kode = %s", (kode,))
        guru = cursor.fetchone()[0]  # Mengambil hasil query dari tuple


        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO hasil_siswa (username, nama, kode, Chapter, jawaban, skor,nilai,guru,selesai) VALUES (%s,%s, %s,%s, %s,%s, %s,%s,%s)", (username, nama, kode,chapter,input_text_list01,argumen_predictions1,argumen_predictionsPK,guru,tg1))
        mysql.connection.commit()
        cursor.close()

        metadata_cursor = mysql.connection.cursor()
        metadata_cursor.execute("INSERT INTO soal_4 (jawaban, labels) VALUES (%s, %s)", (input_text_list01[0], argumen_predictions1[0]))
        mysql.connection.commit()
        metadata_cursor.close()

        session['kode'] = kode
        session['chapter'] = chapter
        session['id'] = cursor.lastrowid
        return redirect(url_for('hasil1'))

    return render_template('statis_4.html', username=username)
  


@app.route('/ujian/tahap5', methods=['GET', 'POST'])
def fluida5():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    if request.method == 'POST':
        nama = request.form['user']
        kode = request.form['kelas']
        chapter = request.form.getlist('checkbox')  # Menggunakan getlist karena bisa ada beberapa pilihan yang dipilih
        ganda1 = request.form['content1']
        tg1 = 100

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT jawaban, labels FROM soal_5")
        argumen_data = cursor.fetchall()
        argumen_jawaban = [preprocess_text(data[0]) for data in argumen_data]
        argumen_labels = [data[1] for data in argumen_data]

        input_text_list01 = [remove_html_tags(ganda1)]
        input_text_list1 = [preprocess_text(text) for text in input_text_list01]

        vectorizer = CountVectorizer()
        database_vectorized = vectorizer.fit_transform(argumen_jawaban)

        models = []
        for _ in range(1):
            model = train_logistic_regression(database_vectorized, argumen_labels)
            models.append(model)

        predictions1 = [model.predict(vectorizer.transform(input_text_list1))[0] for model in models]

        argumen_predictions1 = []
        argumen_predictionsPK = []

        for prediction in predictions1:
            # Konversi prediksi menjadi label yang lebih bermakna
            if prediction == 1:
                argumen_predictions1.append(1)
            elif prediction == 2:
                argumen_predictions1.append(2)
            elif prediction == 3:
                argumen_predictions1.append(3)
            elif prediction == 4:
                argumen_predictions1.append(4)
            else:
                argumen_predictions1.append(1)

        for prediction in predictions1:
            if prediction == 1:
                argumen_predictionsPK.append("Tidak paham")
            elif prediction == 2:
                argumen_predictionsPK.append("Miskonsepsi spesifik")
            elif prediction == 3:
                argumen_predictionsPK.append("Pemahaman sebagian")
            elif prediction == 4:
                argumen_predictionsPK.append("Pemahaman keseluruhan")
            else:
                argumen_predictionsPK.append("Tidak paham")
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT dosen FROM kode WHERE kode = %s", (kode,))
        guru = cursor.fetchone()[0]  # Mengambil hasil query dari tuple


        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO hasil_siswa (username, nama, kode, Chapter, jawaban, skor,nilai,guru,selesai) VALUES (%s,%s, %s,%s, %s,%s, %s,%s,%s)", (username, nama, kode,chapter,input_text_list01,argumen_predictions1,argumen_predictionsPK,guru,tg1))
        mysql.connection.commit()
        cursor.close()

        metadata_cursor = mysql.connection.cursor()
        metadata_cursor.execute("INSERT INTO soal_5 (jawaban, labels) VALUES (%s, %s)", (input_text_list01[0], argumen_predictions1[0]))
        mysql.connection.commit()
        metadata_cursor.close()

        session['kode'] = kode
        session['chapter'] = chapter
        session['id'] = cursor.lastrowid
        return redirect(url_for('hasil1'))

    return render_template('statis_5.html', username=username)
  

  


#halaman dosen --------------------------------------------------->>>>>>>>>>>>>>>

@app.route('/register/guru', methods=['GET', 'POST'])
def registerguru():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM login_guru WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO login_guru VALUES (NULL, %s, %s, %s)', (username,email, password))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register_dosen.html', msg=msg)

#login dosen
@app.route('/login/guru', methods=['GET', 'POST'])
def loginguru():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM login_guru WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # If the user exists, store the username in the session
            session['username'] = user[1]
            return redirect(url_for('dashboardosen'))
        else:
            return 'Invalid login credentials. Please try again.'

    return render_template('login-dosen.html')


def get_dosen(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen2(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql2(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen3(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql3(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen4(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql4(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen5(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql5(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen6(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql6(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen7(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql7(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen8(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql8(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen9(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql9(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 1' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen10(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql10(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen11(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql11(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen12(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql12(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen13(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql13(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 2' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen14(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql14(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen15(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql15(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen16(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql16(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen17(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql17(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 3' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen18(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql18(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen19(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql19(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen20(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql20(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen21(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql21(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 4' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen22(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql22(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' AND nilai = 'Tidak paham' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen23(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql23(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' AND nilai = 'Miskonsepsi spesifik' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen24(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql24(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' AND nilai = 'Pemahaman sebagian' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data

def get_dosen25(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


def get_dosen_mysql25(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  skor FROM hasil_siswa WHERE guru = %s AND Chapter = 'Newton 5' AND nilai = 'Pemahaman keseluruhan' ORDER BY time DESC LIMIT 40", (username,)) # Ganti dengan nama tabel dan kolom yang sesuai
    results = cursor.fetchall()
    data = [result[0] for result in results]
    cursor.close()
    return data


#dashbord guru
@app.route('/dashboard/guru')
def dashboardosen():
    if 'username' not in session:
        return redirect('/')

    username = session['username']

    labels = get_dosen(username)
    labels2 = get_dosen2(username)
    labels3 = get_dosen3(username)
    labels4 = get_dosen4(username)
    labels5 = get_dosen5(username)
    labels6 = get_dosen6(username)
    labels7 = get_dosen7(username)
    labels8 = get_dosen8(username)
    labels9 = get_dosen9(username)
    labels10 = get_dosen10(username)
    labels11 = get_dosen11(username)
    labels12 = get_dosen12(username)
    labels13 = get_dosen13(username)
    labels14 = get_dosen14(username)
    labels15 = get_dosen15(username)
    labels16 = get_dosen16(username)
    labels17 = get_dosen17(username)
    labels18 = get_dosen18(username)
    labels19 = get_dosen19(username)
    labels20 = get_dosen20(username)
    labels21 = get_dosen21(username)
    labels22 = get_dosen22(username)
    labels23 = get_dosen23(username)
    labels24 = get_dosen24(username)
    labels25 = get_dosen25(username)
  


    # Get data from MySQL
    data = get_dosen_mysql(username)
    data2 = get_dosen_mysql2(username)
    data3 = get_dosen_mysql3(username)
    data4 = get_dosen_mysql4(username)
    data5 = get_dosen_mysql5(username)
    data6 = get_dosen_mysql6(username)
    data7 = get_dosen_mysql7(username)
    data8 = get_dosen_mysql8(username)
    data9 = get_dosen_mysql9(username)
    data10 = get_dosen_mysql10(username)
    data11 = get_dosen_mysql11(username)
    data12 = get_dosen_mysql12(username)
    data13 = get_dosen_mysql13(username)
    data14 = get_dosen_mysql14(username)
    data15 = get_dosen_mysql15(username)
    data16 = get_dosen_mysql16(username)
    data17 = get_dosen_mysql17(username)
    data18 = get_dosen_mysql18(username)
    data19 = get_dosen_mysql19(username)
    data20 = get_dosen_mysql20(username)
    data21 = get_dosen_mysql21(username)
    data22 = get_dosen_mysql22(username)
    data23 = get_dosen_mysql23(username)
    data24 = get_dosen_mysql24(username)
    data25 = get_dosen_mysql25(username)




    cursor = mysql.connection.cursor()


    # Ambil riwayat ujian dari tabel riwayat_ujian berdasarkan mahasiswa_id
    cursor.execute("SELECT kelas, kode, tanggal FROM kode WHERE username = %s ORDER BY time DESC LIMIT 6", (username,))
    riwayat_ujian = cursor.fetchall()
    cursor.close()

    # Dapatkan data nilai dari database berdasarkan username pengguna

    return render_template(template_name_or_list='teacher-dashboard.html', labels=labels, data=data, username=username, riwayat_ujian=riwayat_ujian,
                           labels2=labels2,data2=data2,labels3=labels3,data3=data3,labels4=labels4,data4=data4,labels5=labels5,data5=data5,labels6=labels6,data6=data6,
                           labels7=labels7,data7=data7,labels8=labels8,data8=data8,labels9=labels9,data9=data9,labels10=labels10,data10=data10,labels11=labels11,data11=data11,
                           labels12=labels12,data12=data12,labels13=labels13,data13=data13,labels14=labels14,data14=data14,labels15=labels15,data15=data15,labels16=labels16,data16=data16,
                           labels17=labels17,data17=data17,labels18=labels18,data18=data18,labels19=labels19,data19=data19,labels20=labels20,data20=data20,labels21=labels21,data21=data21,
                           labels22=labels22,data22=data22,labels23=labels23,data23=data23,labels24=labels24,data24=data24,labels25=labels25,data25=data25)

@app.route('/profil/guru', methods=['GET', 'POST'])
def profildosen():
    if 'username' not in session:
        return redirect('/')

    username = session['username']

    
    if request.method == 'POST':
        name = request.form['name']
        nim = request.form['nip']
        user = request.form['username']
        email = request.form['email']
        univ = request.form['universitas']
        prodi = request.form['prodi']
        alamat = request.form['alamat']
        nohp = request.form['nohp']

        # Simpan profil pengguna ke database (misalnya dalam tabel "profil_pengguna")
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM profil_guru WHERE username = %s', (username,))
        existing_profile = cursor.fetchone()

        if existing_profile:
            cursor = mysql.connection.cursor()
            # Jika profil sudah ada, perbarui profil
            cursor.execute('UPDATE profil_guru SET nama = %s, nip = %s, user = %s, email = %s, universitas = %s, prodi = %s, alamat = %s, nohp = %s', (username, name, nim, user, email, univ, prodi, alamat, nohp))
            mysql.connection.commit()
            cursor.close()

        else:
            # Jika profil belum ada, buat profil baru
            cursor.execute('INSERT INTO profil_guru (username, nama, nip, user, email, universitas, prodi, alamat, nohp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)', (username, name, nim, user, email, univ, prodi, alamat, nohp))
            mysql.connection.commit()
            cursor.close()

    # Ambil data profil dari database berdasarkan username pengguna
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT nama, nip, user,email, universitas, prodi, alamat, nohp  FROM profil_guru WHERE username = %s', (username,))
    profile = cursor.fetchone()
    cursor.close()

    # Dapatkan data nilai dari database berdasarkan username pengguna
    return render_template('teacher-profil.html', username=username, profile=profile)


#halaman kode ujian pada dosen
@app.route('/kode/guru', methods=['GET', 'POST'])
def kodedosen():
    if 'username' not in session:
        return redirect('/')

    username = session['username']
    if request.method == 'POST':
        kelas = request.form['kelas']
        tanggal = request.form['tanggal']

        code = generate_code()
        if save_code(username,username, kelas, tanggal, code):
            return render_template('result.html', code=code, kelas=kelas, tanggal=tanggal,username=username)
        else:
            return "Terjadi kesalahan saat menyimpan kode ke database."
         
    return render_template('teacher-kode.html', username=username)



#dashbord dsoen
@app.route('/data/nilai/mahasiswa', methods=['GET', 'POST'])
def datadosen():
    if 'username' not in session:
        return redirect('/')

    username = session['username']
    results = []  # Inisialisasi results dengan list kosong
    if request.method == 'POST':
        keyword = request.form['search']

        # Query untuk mencari data berdasarkan keyword
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM hasil_siswa WHERE nama LIKE %s AND guru= %s OR kode LIKE %s AND guru= %s ', ('%' + keyword + '%',username, '%' + keyword + '%',username))
        results = cursor.fetchall()
        cursor.close()
    return render_template('teacher-data.html', username=username, results=results)


@app.route('/kriteria')
def kriteria():
    if 'username' not in session:
        return redirect('/')

    username = session['username']


    return render_template('kriteria.html', username=username)


@app.route('/soal/aes')
def soal():
    if 'username' not in session:
        return redirect('/')

    username = session['username']


    return render_template('teacher-soal.html', username=username)


@app.route('/unduh/data/siswa', methods=["GET", "POST"])
def unduh():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    class SearchForm(FlaskForm):
        keyword = StringField('Keyword', validators=[DataRequired()])
        submit = SubmitField('Search')
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.keyword.data

        conn = mysql.connect()
        cursor = conn.cursor()
        # Query data dari database
        cursor.execute('SELECT * FROM hasil_siswa WHERE nama LIKE %s AND guru= %s OR kode LIKE %s AND guru = %s ',('%' + keyword + '%', username,'%' + keyword + '%',username))
        results = cursor.fetchall()
        cursor.close()
        
    
        # Jika tidak ada hasil pencarian, tampilkan pesan error
        if not results:
            abort(404)
        
        # Buat file PDF
        pdf = FPDF()
        pdf = FPDF('P', 'mm', 'A4') # A4: 210 x 297 mm
        pdf.add_page()
        # Mengatur margin
        
        pdf.set_left_margin(10)
        pdf.set_right_margin(10)
        pdf.set_top_margin(10)
        pdf.set_auto_page_break(True, margin=15)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(40, 10, 'Kode Ujian:' + keyword)
        # Menambahkan judul dokumen
        pdf.cell(80, 10, 'HASIL SISWA', 0, 1, 'C')

        # Menambahkan garis bawah
        pdf.cell(190, 0.5, '', 'B', 1)
        pdf.ln()
        pdf.set_font('Arial', '', 10)
        for result in results:
            pdf.cell(0, 10, f'Nama: {result[2]}', 0, 1)
            pdf.cell(0, 10, f'Kode Ujian : {result[3]}', 0, 1)
            pdf.cell(0, 10, f'Chapter: {result[4]}', 0, 1)
            pdf.cell(0, 10, f'Nilai Pemahaman Konsep: {result[7]}', 0, 1)
            pdf.cell(0, 10, f'Guru Pengampu: {result[8]}', 0, 1)
            pdf.cell(0, 10, f'Tanggal & Waktu: {result[10]}', 0, 1)
            pdf.cell(0, 10, f'_________________________________________________________________________', 0, 1)
        
        response = make_response(pdf.output(dest='S').encode('latin1'))
        response.headers.set('Content-Disposition', 'attachment', filename='Nilai Siswa .pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response

    return render_template('unduh.html', form=form, username=username)







@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin_db WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # If the user exists, store the username in the session
            session['username'] = user[1]
            return redirect(url_for('adminindex'))
        else:
            return 'Invalid login credentials. Please try again.'
    return render_template('login-admin.html')


@app.route('/admin/home')
def adminindex():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) AS id FROM login_guru')
    total_accounts = cursor.fetchone()[0]

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) AS id FROM login_siswa')
    total_accounts1 = cursor.fetchone()[0]

    return render_template('admin.html', username=username,total_accounts=total_accounts,total_accounts1=total_accounts1)


@app.route('/admin/guru')
def adminguru():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM login_guru')
    teachers = cursor.fetchall()
    return render_template('adminguru.html',username=username,teachers=teachers)

@app.route('/delete/guru/<id_data>')
def delete(id_data):
    # Query database untuk menghapus data guru dengan id tertentu
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM login_guru WHERE id={}'.format(id_data))
    cursor.commit()

    # Redirect ke halaman index
    return redirect(url_for('adminguru'))




@app.route('/admin/siswa')
def adminsiswa():
    if 'username' not in session:
        return redirect('/')
    username = session['username']

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM login_siswa')
    data = cursor.fetchall()

    return render_template('adminsiswa.html',username=username,data=data)

@app.route('/delete/siswa/<id_data>')
def deletesiswa(id_data):
    # Query database untuk menghapus data guru dengan id tertentu
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM login_siswa WHERE id={}'.format(id_data))
    cursor.commit()

    # Redirect ke halaman index
    return redirect(url_for('adminsiswa'))



@app.route('/logout')
def logout():
    # Clear the session to log out the user
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
