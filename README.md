<h2 align="center">API-Monitoring Siswa</h2>

# Sistem Absensi dan Monitoring Siswa
### Studi Kasus SMP Negeri 2 Makassar
#### Spesifikasi :
##### - Hak Akses
- Admin
- Siswa
- Guru Wali Kelas
- Guru BK
- Tata Usaha
- Orang Tua Siswa

##### - Fitur
- Absensi Siswa
- Kumpul Tugas
- Rekap Penilaian Sisa:
  - Sikap
  - Perilaku
  - Tugas
  
#### Cara Install:
- Buat database dengan nama: <b>db_monitoring siswa</b>
- Buat environment :
  - windows: py -m venv env
  - ubuntu: pthon3 -m venv venv
- Jalankan perintah <b>pip install -r requirements.txt</b> pada terminal
- Jlankan perintah berikut pada terminal:
  - <b>flask db init</b>
  - <b>flask db migrate</b>
  - <b>flask db upgrade</b>
### Project Dalam Tahap Pengerjaan

