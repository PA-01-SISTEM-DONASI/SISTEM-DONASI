# SISTEM-DONASI
# Kelompok 1
Muhammad Arham Anugrah | 2509116044

Risky Farel Wijaya | 2509116066   

Muhammad Davi Aditya Pratama | 2503116070

Jihan Shafira Rahmah | 2509116073

# Flowchart
Flowchart yang kami buat terbagi menjadi 3 bagian, yaitu: Menuu utama, Menu role staff dan menu user.

# 1. Menu utama.
   Pada flowchart bagian pertama ini terdapat 3 pilihan menu yaitu Login, Register dan keluar. 
 
# 2. Menu role staff
   Flowchart untuk role staff ini terdapat 6 pilihan menu yaitu Tambah Donasi, Lihat Donasi, Edit Donasi, Hapus Donasi, Kelola Posko, dan Logout.
   
# 3. Menu role user
   Flowchart untuk role user memiliki 5 pilihan menu yaitu Tambah Donasi, Lihat Donasi, Top Up Saldo, Cek Saldo, dan Logout.

# LIBRARY
# 1. JSON
Pada program sistem donasi ini, kami menggunakan 3 JSON untuk mendukung jalannya program. 

A. users.json

<img width="894" height="590" alt="Screenshot 2025-10-23 103434" src="https://github.com/user-attachments/assets/0899b815-c856-45c1-be30-88b1e6e5d8d1" />

B. data_donasi.json

<img width="543" height="791" alt="Screenshot 2025-10-26 172234" src="https://github.com/user-attachments/assets/3ae63e8e-ce9c-4563-8fd8-57b2d26cf1cd" />

C. Posko.json


# 2. os
<img width="553" height="267" alt="Screenshot 2025-10-26 172436" src="https://github.com/user-attachments/assets/74b30d6a-71f9-41e2-abf5-54c99b53b941" />

# 3. pwinput
<img width="174" height="66" alt="Screenshot 2025-10-26 004320" src="https://github.com/user-attachments/assets/ccb3a11f-110f-4d92-80e2-40cc325e56ce" />

# 4. time
<img width="482" height="74" alt="Screenshot 2025-10-23 104946" src="https://github.com/user-attachments/assets/6ee59416-1416-47f1-9162-99ec32563950" />

# 5. re
<img width="722" height="215" alt="Screenshot 2025-10-26 143222" src="https://github.com/user-attachments/assets/85306e75-f723-475f-a7f1-1a31b1c36127" />

# 6. PrettyTable
<img width="718" height="218" alt="Screenshot 2025-10-26 172746" src="https://github.com/user-attachments/assets/df4a7588-83ac-40fc-9ba0-1866f7329d71" />

# Menu Utama   
Ketika program ini dijalankan, maka akan masuk ke dalam menu utama yang berisi 3 pilihan menu yaitu Login, Register dan keluar.

<img width="312" height="155" alt="Screenshot 2025-10-19 211549" src="https://github.com/user-attachments/assets/2a3e22ec-0aff-4b8d-92eb-f515bae47e53" />

Untuk masuk ke masing-masing menu, cukup menginputkan nomor dari pilihan menu tersebut. Contohnya masuk menu login, input angka "1"

# RUN 1
Pilihan menu pertama pada sistem ini yaitu Login. Untuk masuk menu login, input angka "1".

<img width="221" height="143" alt="Screenshot 2025-10-26 004259" src="https://github.com/user-attachments/assets/1f7724fc-85c2-41b7-95d8-7b538af9e6a1" />

# RUN 2
Setelah masuk ke menu login, maka akan disuruh untuk mengisi username dan password. Untuk username dan password terbagi menjadi dua role, yaitu staff dan user. Untuk role staff, usernamenya "staff" dan untuk passwordnya adalah "12345". Lalu, untuk role user username dan password disesuaikan dengan yang telah dibuat sebelumnya. Pada sistem login ini, kami menggunakan library pwinput untuk melindungi password agar tidak terlihat saat proses login.

Contoh login role staff:

<img width="174" height="66" alt="Screenshot 2025-10-26 004320" src="https://github.com/user-attachments/assets/e57d1b14-2de8-43e5-b3a7-66bbb3f7f561" />

Contoh login role user:

<img width="160" height="67" alt="Screenshot 2025-10-26 113958" src="https://github.com/user-attachments/assets/fabea4ae-2912-4646-894b-6fe085218450" />

# RUN 3
Pilihan menu kedua yaitu Register. Menu ini berfungsi untuk user membuat username dan password terlebih dahulu sebelum menggunakan sistem. Untuk masuk pada menu Register input angka "2".

<img width="227" height="131" alt="Screenshot 2025-10-23 222409" src="https://github.com/user-attachments/assets/6ac62c83-9c2b-4d75-aef2-9999a099882b" />

# RUN 4
Seteleh masuk menu Register, maka akan disuruh untuk mengisi username baru dan password. Pertama isi dulu username pada "Username baru: ", lalu enter dan isi "Password: ".

<img width="263" height="42" alt="Screenshot 2025-10-23 222449" src="https://github.com/user-attachments/assets/4306d40f-4806-4c34-a5ae-7cc7de5acbb5" />

Sebagai contoh, kami membuat username baru dengan nama Arham dan password 000.

# RUN 5
Setelah memasukkan username baru dan password, tekan enter pada keyboard hingga ada output "Registrasi berhasil" seperti gambar dibawah ini.

<img width="233" height="73" alt="Screenshot 2025-10-23 222456" src="https://github.com/user-attachments/assets/4af3399f-ede4-44bb-88c0-4629587ae6e0" />

# RUN 6
Menu ketiga sekaligus terakhir pada menu utama kali ini adalah Keluar. Menu ini berfungsi jika kita ingin keluar pada sistem ini. Untuk keluar pada menu ini, cukup inputkan angka "0", lalu enter. 

<img width="207" height="132" alt="Screenshot 2025-10-26 115039" src="https://github.com/user-attachments/assets/e68a0953-d035-4bc9-b926-dbce3139c9e4" />

# RUN 7
Hasil yang akan terjadi ketika memilih menu Keluar adalah seperti ini:

<img width="279" height="139" alt="image" src="https://github.com/user-attachments/assets/c1176f92-d3dd-4cd1-997a-bdfb27e6a34f" />

# Role
Pada sistem ini terdapat 2 role yaitu Staff dan user(Donatur). Berikut panduan penggunaan untuk role staff. 
# RUN 1 Staff
Untuk masuk sebagai staff, Login dengan username staff dan password 12345. 

<img width="211" height="91" alt="Screenshot 2025-10-20 204612" src="https://github.com/user-attachments/assets/907df82c-9880-4c52-ad37-4cfe57f586d5" />
  
Karena pada sistem ini kami gunakan library pwinput, password yang diisi pada saat login otomatis akan disembunyikan atau diganti dengan tanda *****

# RUN 2 Staff
Menu ini menampilkan pilihan utama untuk staff, yaitu **1. Kelola Donasi** untuk mengelola seluruh proses donasi, atau **0. Logout** untuk keluar dari sistem. Staff diminta memasukkan nomor menu yang ingin dipilih.

<img width="435" height="125" alt="Screenshot 2025-10-26 204028" src="https://github.com/user-attachments/assets/09d5c8e9-55ed-4708-b355-2cc89d939591" />

Untuk mengakses menu-menu tersebut, cukup input nomor pada menu tersebuut. Contoh untuk mengakses menu tambah donasi, input angka 1 lalu enter untuk masuk ke menu tersebut. 

# RUN 3 Staff (Kelola Donasi)
Menu ini adalah bagian **Kelola Donasi** untuk staff, menampilkan berbagai opsi pengelolaan donasi, seperti menambah jenis donasi atau posko, melihat dan mengedit data donasi, serta menghapus posko. Staff diminta memasukkan nomor menu yang ingin dijalankan.

<img width="891" height="657" alt="Screenshot 2025-10-26 204150" src="https://github.com/user-attachments/assets/cc28492d-d1bb-4258-826a-8ee4e9ff9591" />

# RUN 4 Staff (Tambah Jenis Donasi)
Staff diminta untuk memasukkan nama jenis donasi baru, dengan contoh seperti *Donasi Hewan Terlantar* atau *Donasi Korban Perang*. Setelah nama dimasukkan, sistem menambahkan jenis donasi tersebut dan menampilkan konfirmasi keberhasilan, misalnya *“Jenis donasi 'Donasi Tanah Longsor' berhasil ditambahkan!”*.

<img width="779" height="275" alt="Screenshot 2025-10-26 204413" src="https://github.com/user-attachments/assets/726e798f-f756-4c84-aa17-3de5f49f5f8a" />

# RUN 5 Staff (Tambah Posko)
Staff diminta memasukkan nama lokasi posko baru, dengan contoh seperti *Sangatta*, *Bengalon*, atau *Muara Ancalong*. Setelah dimasukkan, sistem menambahkan posko tersebut dan menampilkan konfirmasi keberhasilan, misalnya *“Posko 'Samarinda' berhasil ditambahkan!”*.

<img width="705" height="249" alt="Screenshot 2025-10-26 204639" src="https://github.com/user-attachments/assets/32b1635b-6e78-4d8b-a83a-32145b40a1af" />

# RUN 6 Staff (Lihat Donasi)
Menu ini menampilkan seluruh data donasi yang telah dilakukan, termasuk username, nama donatur, jenis donasi, jumlah, metode pembayaran, dan posko. Di bagian bawah ditampilkan total donasi, serta opsi untuk **mencari donasi**, **menyortir donasi**, atau **kembali** ke menu sebelumnya. 

<img width="1164" height="406" alt="Screenshot 2025-10-26 204824" src="https://github.com/user-attachments/assets/871dfe8a-f09a-4b1a-a0dd-426a7757e6cb" />

# RUN 7 Staff (Lihat Jenis Donasi)
Menu ini menampilkan daftar semua jenis donasi beserta ID-nya. Staff dapat menekan Enter untuk kembali ke menu sebelumnya.

<img width="535" height="367" alt="Screenshot 2025-10-26 205217" src="https://github.com/user-attachments/assets/afbc947c-0fac-4b51-a77d-6e4a1ba1963b" />
 
# RUN 8 Staff (Lihat Posko Donasi)
Menu ini menampilkan daftar semua posko donasi beserta ID-nya. Staff dapat menekan Enter untuk kembali ke menu sebelumnya.

<img width="540" height="347" alt="Screenshot 2025-10-26 205438" src="https://github.com/user-attachments/assets/0ca9dd70-ae86-46cb-b2d2-d3b6526cea12" />

# RUN 9 Staff (Edit Donasi)
- Menu **Edit Donasi** menampilkan daftar donasi yang sudah tercatat beserta total donasi, lalu meminta staff memasukkan nomor donasi yang ingin diedit atau 0 untuk batal.

<img width="1061" height="313" alt="Screenshot 2025-10-26 205742" src="https://github.com/user-attachments/assets/448ecc04-453a-4450-abc6-5f94848bc836" />

- Staff dapat mengubah data donasi yang dipilih. Pada contoh ini, sistem meminta input nama donatur; jika ingin mengubahnya, staff mengetik nama baru, misalnya *shafira*, atau menekan Enter untuk tetap menggunakan nama lama.

<img width="683" height="78" alt="Screenshot 2025-10-26 205927" src="https://github.com/user-attachments/assets/92bb88bf-0d60-4fc3-a0cb-a77a3310f83e" />

- Staff dapat mengubah jenis donasi dari data yang dipilih. Sistem menampilkan daftar jenis donasi, dan staff dapat memilih nomor baru (misalnya 2) atau menekan Enter untuk tidak mengubah jenis donasi.

<img width="693" height="232" alt="Screenshot 2025-10-26 210155" src="https://github.com/user-attachments/assets/3336ab48-80ae-4d78-b5d1-4fb0a1fc97f9" />

- Staff dapat mengubah lokasi posko dari data donasi yang dipilih. Sistem menampilkan daftar posko, dan staff dapat memilih nomor baru (misalnya 5) atau menekan Enter untuk tidak mengubah lokasi. Setelah itu, sistem menampilkan konfirmasi *“Data donasi berhasil diperbarui”*.

<img width="687" height="280" alt="Screenshot 2025-10-26 210253" src="https://github.com/user-attachments/assets/29daff3e-4809-457d-92ce-cd8f0288ddff" />

# RUN 10 Staff (Hapus Posko Donasi)
- Menu **Hapus Posko Donasi** menampilkan daftar posko yang tersedia dan meminta staff memasukkan nama posko yang ingin dihapus atau 0 untuk batal.

<img width="788" height="360" alt="Screenshot 2025-10-26 210447" src="https://github.com/user-attachments/assets/8d6dc282-2359-4eff-8c34-2cd651e19c74" />

- Staff diminta mengonfirmasi penghapusan posko yang dipilih. Jika memilih **y**, sistem akan menghapus posko tersebut dan menampilkan konfirmasi, misalnya *“Posko 'Sangatta' berhasil dihapus”*.

<img width="770" height="120" alt="Screenshot 2025-10-26 210650" src="https://github.com/user-attachments/assets/0d3ac43e-0285-4f6e-a320-0fc30b40765d" />

# Role
Lanjut untuk role yang kedua adalah Role User. Berikut panduan penggunaan untuk role staff.
# Run 1 user
  Untuk masuk sebagai user, Login dengan username dan password yang sudah dibuat sebelumnya. Sebagai contoh untuk masuk sebagai user, login dengan username Davi     dan password 1234, lalu enter. Pada menu login, password akan otomatis disembunyikan oleh sistem karena sudah menggunakan library pwinput.
  
   <img width="160" height="67" alt="Screenshot 2025-10-26 113958" src="https://github.com/user-attachments/assets/ca945ae1-4a33-4c2c-bb07-29d6d17b1131" />

# Run 2 user
Pada menu user, terdapat 5 pilihan menu yang dapat diakses, seperti: 
1. Tambah Donasi
2. Lihat Donasi
3. Top Up saldo
4. Cek Saldo
0. Logout


# Run 3 user (Tambah Donasi)
Setelah masuk ke menu user, pencet nomor 1, yaitu Tambah donasi

<img width="361" height="203" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/7535716f-430d-4e11-9ccd-7e2068789224" />

# Run 3 user (Tambah Donasi)
Setelah masuk, Akan muncul menu untuk memilih jenis Donasi

<img width="315" height="214" alt="Screenshot (44)" src="https://github.com/user-attachments/assets/55cf876e-b23f-4e28-918b-833806c39da7" />

# Run 3 user (Tambah Donasi)
user bisa memilih jenis donasi yang user inginkan

<img width="320" height="240" alt="Screenshot (45)" src="https://github.com/user-attachments/assets/81678edf-33fa-4742-8480-c0254c462a6a" />

# Run 3 user (Tambah Donasi)
SEtelah itu, User memilih posko mana yang user ingin dituju


<img width="318" height="238" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/35461f97-dc53-4069-ad3f-bc50c1ee23ab" />

# Run 3 user (Tambah Donasi)
User bisa masukan Nama Donatur

<img width="471" height="265" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/1fb50626-8480-4403-a3e6-9b096b471ba3" />

# Run 3 user (Tambah Donasi)
User bisa memilih jumlah Donasi

<img width="471" height="265" alt="Screenshot (52)" src="https://github.com/user-attachments/assets/080dc251-0e40-4032-87aa-ac6146c0e727" />

# Run 3 user (Tambah Donasi)
Setelah User memilih jumlah donasi maka Struk belanja akan keluar

<img width="496" height="279" alt="Screenshot (53)" src="https://github.com/user-attachments/assets/8fa97eb2-e0c0-4c0f-baeb-1d647ed1bc02" />


# Run user 4 (Lihat Donasi)
Lanjuut pada fitur Lihat donasi, User bisa memasukan nomor 2

<img width="380" height="199" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/1fab05c9-f84c-40a3-bf77-0cd912a6f7de" />

# Run user 4 (Lihat Donasi)
Setelah itu akan muncul Tabel donasi dan Total Donasi yang diterima

<img width="838" height="471" alt="Screenshot (59)" src="https://github.com/user-attachments/assets/2acf1aab-d484-4f1e-af97-5e5b95ca0c78" />

# Run user 4 (Lihat Donasi)
Jika user ingin mengSortir donasi maka user bisa memasukan angka 1

<img width="816" height="474" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/1c3922da-8c07-4178-823f-012813bf7be3" />

# Run user 4 (Lihat Donasi)
Pada opsi ini User bisa memilih untuk mensortir dari jumlah Terkecil-Terbesar / Terbesar-Terkecil

<img width="342" height="192" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/33cfd6f1-ca0a-47dd-b4b4-44e0b055880c" />

# Run user 4 (Lihat Donasi)
jika memilih Terkecil-Terbesar maka urutan donasi akan berubah dengan urutan nominal terkecil paling atas

<img width="862" height="436" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/087d7ed1-8543-4fe4-8e2e-aa0330cee642" />

# Run user 4 (Lihat Donasi)
jika memilih Terbesar-Terkecil maka urutan donasi akan berubah dengan urutan nominal Terbesar paling atas

<img width="836" height="455" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/25a46585-f947-467b-b41a-f0035264f19a" />

# Run user 4 (Lihat Donasi)
jika user ingin membatalkan pilihan bisa memasukan angka 0 dan akan kembali ke Tabel donasi

<img width="285" height="190" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/bff63117-d1bb-4c80-9966-7772cc4399e0" />

# Run user 4 (Lihat Donasi)
User bisa memasukan angka 0 untuk kembali ke menu User

<img width="826" height="471" alt="Screenshot (68)" src="https://github.com/user-attachments/assets/64729790-09eb-411e-8fd6-1787a0ffa694" />

# Run  user 5 (Top up Saldo)
Jika User ingin Top up Saldo maka User bisa memasukan angka 3

<img width="361" height="203" alt="Screenshot (69)" src="https://github.com/user-attachments/assets/deb6706c-78e6-4fc2-99a8-8c27497892e6" />

# Run  user 5 (Top up Saldo)
User bisa memasukan nominal yang di inginkan

<img width="323" height="85" alt="Screenshot (70)" src="https://github.com/user-attachments/assets/cbebfd84-5b28-452d-9eae-0767098be95b" />

# Run  user 5 (Top up Saldo)
Setelah memasukan nomminal yang di inginkan, maka saldo otomatis bertambah

<img width="414" height="119" alt="Screenshot (71)" src="https://github.com/user-attachments/assets/71093312-c49b-44f0-85e7-1f8c8fe523a6" />

# Run  user 5 (Top up Saldo)
User lalu menekan enter untuk kembali ke Menu User

<img width="414" height="119" alt="Screenshot (71)" src="https://github.com/user-attachments/assets/892f1db4-436e-46ee-b919-9fd001de34d9" />


# Run  user 6 (Cek Saldo)
Pada Menu, User bisa memasukan angka 4 untuk mengecek saldo

<img width="252" height="211" alt="Screenshot (73)" src="https://github.com/user-attachments/assets/54471714-cec8-45fe-b4f9-a9c0a6893a53" />

# Run  user 6 (Cek Saldo)
User bisa menekan enter untuk kembali ke Menu User

<img width="252" height="211" alt="Screenshot (73)" src="https://github.com/user-attachments/assets/24f9521e-7835-48e8-9a7e-3f3cf7f97d52" />

# Run  user 6 (Keluar)
Pada Menu, User bisa memasukan angka 0 untuk Logout 

<img width="286" height="213" alt="Screenshot (75)" src="https://github.com/user-attachments/assets/ca988b6e-bfae-4bf6-a2aa-94616093361c" />

# Run  user 6 (Keluar)
Pada opsi ini user bisa Memasukan angka 0 untuk keluar dari program

<img width="247" height="144" alt="Screenshot (77)" src="https://github.com/user-attachments/assets/dd9b6692-e497-4fd7-8321-ffddf5cec295" />

# Run  user 6 (Keluar)
Setelah menekan 0 maka User telah keluar dari program

<img width="382" height="181" alt="Screenshot (78)" src="https://github.com/user-attachments/assets/f57b209e-7b8d-455f-a583-fd878de84c16" />
