from flask import Flask, render_template

app = Flask(__name__)

mahasiswa = {
    "nama": "Muhammad Fariduddin Al Attar",
    "nim": "1482500064",
    "program_studi": "Sistem Teknologi Informasi",
    "universitas": "Universitas 17 Agustus 1945 Surabaya",
    "email": "faridduddin26@gmail.com",
    "ipk": "3,40"
}

daftar_nilai = [
    {"no": 1, "mata_kuliah": "TI dan Aplikasi Bisnis Berkembang", "sks": 3, "nilai": "AB", "angka": 10.5},
    {"no": 2, "mata_kuliah": "Arsitektur dan Organisasi Komputer", "sks": 2, "nilai": "AB", "angka": 7},
    {"no": 3, "mata_kuliah": "Pemrograman Berorientasi Objek", "sks": 3, "nilai": "A", "angka": 12},
    {"no": 4, "mata_kuliah": "Sistem Basis Data", "sks": 3, "nilai": "B", "angka": 9},
    {"no": 5, "mata_kuliah": "Algoritma dan Struktur Data", "sks": 3, "nilai": "AB", "angka": 10.5},
    {"no": 6, "mata_kuliah": "Statistika dan Probabilitas", "sks": 3, "nilai": "B", "angka": 9}
]

@app.route("/")
def profil():
    return render_template("index.html", mahasiswa=mahasiswa)

@app.route("/nilai")
def nilai():
    return render_template("nilai.html", daftar_nilai=daftar_nilai)

@app.route("/admin")
def admin():
    total_sks = sum(item["sks"] for item in daftar_nilai)
    rata_nilai = round(sum(item["angka"] for item in daftar_nilai) / total_sks, 2)
    statistik = [
        {"judul": "Total Mata Kuliah", "angka": len(daftar_nilai), "keterangan": "Mata kuliah terdaftar"},
        {"judul": "Total SKS", "angka": total_sks, "keterangan": "SKS semester ini"},
        {"judul": "IPK Awal", "angka": mahasiswa["ipk"], "keterangan": "Data profil mahasiswa"}
    ]
    return render_template("admin.html", statistik=statistik, daftar_nilai=daftar_nilai, rata_nilai=rata_nilai)

if __name__ == "__main__":
    app.run(debug=True)
