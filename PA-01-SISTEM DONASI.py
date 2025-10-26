import json
import os
import pwinput
import time
import re
from prettytable import PrettyTable

USER_FILE = 'users.json'
DONASI_FILE = 'data_donasi.json'
POSKO_FILE = 'posko.json'
JENIS_DONASI_FILE = 'jenis_donasi.json'

MAX_DONASI = 10_000_000
MAX_TOPUP = 10_000_000
MAX_SALDO = 50_000_000
LOGIN_ATTEMPTS = 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump([], f)
    with open(file, 'r') as f:
        content = f.read().strip()
        return json.loads(content) if content else []

def save_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def safe_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\n\nEOF Error terdeteksi. Kembali ke menu sebelumnya.")
        time.sleep(1)
        return None
    except KeyboardInterrupt:
        print("\n\nProgram dibatalkan oleh user (Ctrl+C).")
        time.sleep(1)
        return None

#FUNC ERROR HANDLING BIAR GA PANJANG
def safe_int_input(prompt, min_val=None, max_val=None, allow_cancel=True):
    while True:
        try:
            value = safe_input(prompt)
            if value is None:
                return None
            
            if allow_cancel and value.strip() == '0':
                return 0
            
            value = int(value)
            
            if min_val is not None and value < min_val:
                print(f"Nilai minimal adalah {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Nilai maksimal adalah {max_val:,}.")
                continue
            
            return value
        except ValueError:
            print("Input harus berupa angka!")
            continue
        except KeyboardInterrupt:
            print("\n\nInput dibatalkan.")
            time.sleep(1)
            return None

def load_jenis_donasi():
    if not os.path.exists(JENIS_DONASI_FILE):
        default_jenis = [
            {"id": 1, "nama": "Fakir dan Miskin"},
            {"id": 2, "nama": "Donasi Kebakaran"},
            {"id": 3, "nama": "Donasi Bencana Alam"},
            {"id": 4, "nama": "Donasi Pendidikan"},
            {"id": 5, "nama": "Donasi Kesehatan dan Medis"}
        ]
        save_json(JENIS_DONASI_FILE, default_jenis)
        return default_jenis
    return load_json(JENIS_DONASI_FILE)

#TAMBAH JENIS
def tambah_jenis_donasi():
    try:
        clear_screen()
        jenis_list = load_jenis_donasi()
        
        print(">>> TAMBAH JENIS DONASI BARU <<<")
        print("\nContoh: Donasi Hewan Terlantar, Donasi Korban Perang")
        print("Ketik '0' untuk batal\n")
        
        nama_jenis = safe_input("Nama Jenis Donasi: ")
        if nama_jenis is None:
            return
        
        nama_jenis = nama_jenis.strip()
        
        if nama_jenis == "0":
            print("Batal menambah jenis donasi.")
            time.sleep(1)
            return
        
        if not nama_jenis:
            print("Nama jenis donasi tidak boleh kosong.")
            time.sleep(1)
            return
        
        if any(j['nama'].lower() == nama_jenis.lower() for j in jenis_list):
            print("Jenis donasi dengan nama tersebut sudah ada.")
            time.sleep(1)
            return
        
        new_id = max([j['id'] for j in jenis_list], default=0) + 1
        
        jenis_list.append({
            "id": new_id,
            "nama": nama_jenis
        })
        save_json(JENIS_DONASI_FILE, jenis_list)
        print(f"\n✓ Jenis donasi '{nama_jenis}' berhasil ditambahkan!")
        safe_input("Tekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nOperasi dibatalkan.")
        time.sleep(1)

#LIHAT JENIS
def lihat_jenis_donasi():
    try:
        clear_screen()
        jenis_list = load_jenis_donasi()
        
        if not jenis_list:
            print("Belum ada data jenis donasi.")
            safe_input("Tekan Enter untuk kembali...")
            return
        
        print(">>> DAFTAR JENIS DONASI <<<")
        table = PrettyTable(["ID", "Nama Jenis Donasi"])
        for j in jenis_list:
            table.add_row([j['id'], j['nama']])
        print(table)
        safe_input("\nTekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nKembali ke menu.")
        time.sleep(1)

def load_posko():
    if not os.path.exists(POSKO_FILE):
        default_posko = [
            {"id": 1, "nama": "Sangatta"},
            {"id": 2, "nama": "Bengalon"},
            {"id": 3, "nama": "Muara Wahau"},
            {"id": 4, "nama": "Rantau Pulung"}
        ]
        save_json(POSKO_FILE, default_posko)
        return default_posko
    return load_json(POSKO_FILE)

#TAMBAH POSKO
def tambah_posko():
    try:
        clear_screen()
        posko_list = load_posko()
        
        print(">>> TAMBAH POSKO BARU <<<")
        print("\nContoh input: Sangatta, Bengalon, Muara Ancalong")
        print("Ketik '0' untuk batal\n")
        
        lokasi = safe_input("Nama lokasi posko: ")
        if lokasi is None:
            return
        
        lokasi = lokasi.strip()
        
        if lokasi == "0":
            print("Batal menambah posko.")
            time.sleep(1)
            return
        
        if not lokasi:
            print("Nama lokasi tidak boleh kosong.")
            time.sleep(1)
            return
        
        if any(p['nama'].lower() == lokasi.lower() for p in posko_list):
            print("Posko dengan nama tersebut sudah ada.")
            time.sleep(1)
            return
        
        new_id = max([p['id'] for p in posko_list], default=0) + 1
        
        posko_list.append({
            "id": new_id,
            "nama": lokasi
        })
        save_json(POSKO_FILE, posko_list)
        print(f"\n✓ Posko '{lokasi}' berhasil ditambahkan!")
        safe_input("Tekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nOperasi dibatalkan.")
        time.sleep(1)

#LIHAT POSKO
def lihat_posko():
    try:
        clear_screen()
        posko_list = load_posko()
        
        if not posko_list:
            print("Belum ada data posko.")
            safe_input("Tekan Enter untuk kembali...")
            return
        
        print(">>> DAFTAR POSKO DONASI <<<")
        table = PrettyTable(["ID", "Nama Posko"])
        for p in posko_list:
            table.add_row([p['id'], p['nama']])
        print(table)
        safe_input("\nTekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nKembali ke menu.")
        time.sleep(1)

#HAPUS POSKO
def hapus_posko():
    try:
        clear_screen()
        posko_list = load_posko()
        
        if not posko_list:
            print("Belum ada data posko.")
            safe_input("Tekan Enter untuk kembali...")
            return
        
        while True:
            clear_screen()
            print(">>> HAPUS POSKO DONASI <<< \n")
            
            table = PrettyTable(["ID", "Nama Posko"])
            for p in posko_list:
                table.add_row([p['id'], p['nama']])
            print(table)
            
            nama_posko = safe_input("\nMasukkan nama posko yang ingin dihapus (0 untuk batal): ")
            if nama_posko is None or nama_posko.strip() == "0":
                return
            
            nama_posko = nama_posko.strip()
            
            found = False
            for i, p in enumerate(posko_list):
                if p['nama'].lower() == nama_posko.lower():
                    found = True
                    
                    data_donasi = load_json(DONASI_FILE)
                    jumlah_donasi = sum(1 for d in data_donasi if d.get('lokasi', '').lower() == nama_posko.lower())
                    
                    if jumlah_donasi > 0:
                        print(f"\nPosko '{p['nama']}' tidak dapat dihapus karena masih digunakan dalam {jumlah_donasi} donasi.")
                        safe_input("Tekan Enter untuk kembali...")
                        return
                    
                    konfirmasi = safe_input(f"Yakin hapus posko '{p['nama']}'? (y/n): ")
                    if konfirmasi is None:
                        return
                    
                    if konfirmasi.lower() == 'y':
                        del posko_list[i]
                        save_json(POSKO_FILE, posko_list)
                        print(f"✓ Posko '{p['nama']}' berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                    safe_input("Tekan Enter untuk kembali...")
                    return
            
            if not found:
                print("Posko tidak ditemukan.")
                kembali = safe_input("Ingin coba lagi? (y/n): ")
                if kembali is None or kembali.lower() != 'y':
                    break
    except KeyboardInterrupt:
        print("\n\nOperasi dibatalkan.")
        time.sleep(1)

#REGISTER
def register():
    try:
        clear_screen()
        users = load_json(USER_FILE)
        while True:
            username = safe_input("Username baru: ")
            if username is None:
                return
            
            username = username.strip()
            if not username:
                print("Username tidak boleh kosong.")
                continue
            
            if not re.match(r'^[A-Za-z0-9_]+$', username):
                print("Username hanya boleh berisi huruf, angka, dan underscore (_).")
                continue
            if any(u["username"] == username for u in users):
                print("Username sudah terdaftar.")
                continue
            
            try:
                password = pwinput.pwinput("Password: ")
            except (EOFError, KeyboardInterrupt):
                print("\nInput password dibatalkan.")
                return
            
            if not password:
                print("Password tidak boleh kosong.")
                continue
            
            users.append({
                "username": username,
                "password": password,
                "role": "User",
                "saldo": 0
            })
            save_json(USER_FILE, users)
            print("Registrasi berhasil!")
            safe_input("Tekan Enter untuk kembali...")
            break
    except KeyboardInterrupt:
        print("\n\nRegistrasi dibatalkan.")
        time.sleep(1)

#LOGIN
def login():
    try:
        clear_screen()
        users = load_json(USER_FILE)
        attempts = LOGIN_ATTEMPTS
        while attempts > 0:
            username = safe_input("Username: ")
            if username is None:
                return None
            
            username = username.strip()
            
            try:
                password = pwinput.pwinput("Password: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nLogin dibatalkan.")
                return None
            
            if not username or not password:
                print("Username dan password tidak boleh kosong.")
                continue
            
            for u in users:
                if u["username"] == username and u["password"] == password:
                    u["saldo"] = int(u.get("saldo", 0))
                    print("Login berhasil. Menyiapkan akun...")
                    time.sleep(1)
                    return u
            
            attempts -= 1
            print(f"Username atau password salah. Sisa percobaan: {attempts}")
        
        print("Kesempatan login habis. Kembali ke menu utama.")
        time.sleep(1)
        return None
    except KeyboardInterrupt:
        print("\n\nLogin dibatalkan.")
        time.sleep(1)
        return None
    
#TABEL DONASI
def tampilkan_tabel_donasi(current_user, data):
    if not data:
        return 0
    
    if current_user and current_user["role"] == "Staff":
        table = PrettyTable(["No", "Username", "Nama Donatur", "Jenis Donasi", "Jumlah", "Metode", "Posko"])
    else:
        table = PrettyTable(["No", "Nama Donatur", "Jenis Donasi", "Jumlah", "Metode", "Posko"])
    
    total = 0
    for idx, d in enumerate(data, start=1):
        jumlah_int = int(d.get("jumlah", 0))
        total += jumlah_int
        
        if current_user and current_user["role"] == "Staff":
            table.add_row([
                idx,
                d.get("username", "-"),
                d.get("nama", "-"),
                d.get("jenis_donasi", "-"),
                f"Rp{jumlah_int:,}",
                d.get("metode", "-"),
                d.get("lokasi", "-")
            ])
        else:
            table.add_row([
                idx,
                d.get("nama", "-"),
                d.get("jenis_donasi", "-"),
                f"Rp{jumlah_int:,}",
                d.get("metode", "-"),
                d.get("lokasi", "-")
            ])
    
    print(table)
    if current_user and current_user["role"] == "Staff":
        print(f"\nTotal Donasi: Rp{total:,}")
    else:
        print(f"\nTotal Donasi Anda: Rp{total:,}")
    
    return total

#LIHAT DONASI
def lihat_donasi(current_user):
    try:
        while True:
            clear_screen()
            data = load_json(DONASI_FILE)
            
            if not data:
                print("Belum ada data donasi.")
                safe_input("Tekan Enter untuk kembali...")
                return
            
            if current_user["role"] == "User":
                data = [d for d in data if d.get("username") == current_user["username"]]
            
            if not data:
                print("Tidak ada donasi untuk ditampilkan.")
                safe_input("Tekan Enter untuk kembali...")
                return
            
            print(">>> LIHAT DONASI <<<\n")
            tampilkan_tabel_donasi(current_user, data)
            
            if current_user["role"] == "Staff":
                print("1. Cari Donasi")
                print("2. Sortir Donasi")
                print("0. Kembali")
                
                pilih = safe_input("\nPilih aksi: ")
                if pilih is None:
                    return
                
                pilih = pilih.strip()
                
                if pilih == "0":
                    return
                elif pilih == "1":
                    # Cari donasi (Staff)
                    clear_screen()
                    print(">>> CARI DONASI <<<")
                    print("1. Cari berdasarkan Jenis Donasi")
                    print("2. Cari berdasarkan Posko")
                    print("0. Batal")
                    
                    pilihan_cari = safe_input("\nPilih: ")
                    if pilihan_cari is None or pilihan_cari.strip() == "0":
                        continue
                    
                    pilihan_cari = pilihan_cari.strip()
                    
                    if pilihan_cari == "1":
                        jenis_list = load_jenis_donasi()
                        print("\n DAFTAR JENIS DONASI ")
                        for i, j in enumerate(jenis_list, start=1):
                            print(f"{i}. {j['nama']}")
                        
                        pilih_jenis = safe_int_input("\nPilih nomor jenis donasi (0 untuk batal): ", min_val=0, max_val=len(jenis_list))
                        if pilih_jenis is None or pilih_jenis == 0:
                            continue
                        
                        keyword = jenis_list[pilih_jenis - 1]['nama'].lower()
                        hasil = [d for d in data if keyword == d.get("jenis_donasi", "").lower()]
                        
                    elif pilihan_cari == "2":
                        posko_list = load_posko()
                        print("\n>>> DAFTAR POSKO <<<")
                        for i, p in enumerate(posko_list, start=1):
                            print(f"{i}. {p['nama']}")
                        
                        pilih_posko = safe_int_input("\nPilih nomor posko (0 untuk batal): ", min_val=0, max_val=len(posko_list))
                        if pilih_posko is None or pilih_posko == 0:
                            continue
                        
                        keyword = posko_list[pilih_posko - 1]['nama'].lower()
                        hasil = [d for d in data if keyword == d.get("lokasi", "").lower()]
                    else:
                        print("Pilihan tidak valid.")
                        time.sleep(1)
                        continue
                    
                    clear_screen()
                    if not hasil:
                        print(f"Tidak ada hasil untuk '{keyword}'.")
                        safe_input("\nTekan Enter untuk kembali...")
                    else:
                        print(f" HASIL PENCARIAN: '{keyword.title()}' \n")
                        tampilkan_tabel_donasi(current_user, hasil)
                        safe_input("\nTekan Enter untuk kembali...")
                
                elif pilih == "2":
                    # Sortir donasi (Staff)
                    clear_screen()
                    print(" SORTIR DONASI ")
                    print("1. Jumlah (Terkecil-Terbesar)")
                    print("2. Jumlah (Terbesar-Terkecil)")
                    print("0. Batal")
                    
                    pilihan_sort = safe_input("\nPilih: ")
                    if pilihan_sort is None or pilihan_sort.strip() == "0":
                        continue
                    
                    pilihan_sort = pilihan_sort.strip()
                    
                    if pilihan_sort == "1":
                        data_sorted = sorted(data, key=lambda d: int(d.get("jumlah", 0)))
                        judul = "Jumlah (Terkecil-Terbesar)"
                    elif pilihan_sort == "2":
                        data_sorted = sorted(data, key=lambda d: int(d.get("jumlah", 0)), reverse=True)
                        judul = "Jumlah (Terbesar-Terkecil)"
                    else:
                        print("Pilihan tidak valid.")
                        time.sleep(1)
                        continue
                    
                    clear_screen()
                    print(f" DATA DIURUTKAN: {judul} \n")
                    tampilkan_tabel_donasi(current_user, data_sorted)
                    safe_input("\nTekan Enter untuk kembali...")
                else:
                    print("Pilihan tidak valid.")
                    time.sleep(1)
            
            else: 
                print("1. Sortir Donasi")
                print("0. Kembali")
                
                pilih = safe_input("\nPilih aksi: ")
                if pilih is None:
                    return
                
                pilih = pilih.strip()
                
                if pilih == "0":
                    return
                elif pilih == "1":
                    # Sortir donasi (User)
                    clear_screen()
                    print(" SORTIR DONASI ")
                    print("1. Jumlah (Terkecil-Terbesar)")
                    print("2. Jumlah (Terbesar-Terkecil)")
                    print("0. Batal")
                    
                    pilihan_sort = safe_input("\nPilih: ")
                    if pilihan_sort is None or pilihan_sort.strip() == "0":
                        continue
                    
                    pilihan_sort = pilihan_sort.strip()
                    
                    if pilihan_sort == "1":
                        data_sorted = sorted(data, key=lambda d: int(d.get("jumlah", 0)))
                        judul = "Jumlah (Terkecil-Terbesar)"
                    elif pilihan_sort == "2":
                        data_sorted = sorted(data, key=lambda d: int(d.get("jumlah", 0)), reverse=True)
                        judul = "Jumlah (Terbesar-Terkecil)"
                    else:
                        print("Pilihan tidak valid.")
                        time.sleep(1)
                        continue
                    
                    clear_screen()
                    print(f" DATA DIURUTKAN: {judul} \n")
                    tampilkan_tabel_donasi(current_user, data_sorted)
                    safe_input("\nTekan Enter untuk kembali...")
                else:
                    print("Pilihan tidak valid.")
                    time.sleep(1)
                
    except KeyboardInterrupt:
        print("\n\nOperasi dibatalkan.")
        time.sleep(1)

#TAMBAH DONASI(USER)
def tambah_donasi(current_user):
    try:
        clear_screen()
        data = load_json(DONASI_FILE)
        users = load_json(USER_FILE)
        posko_list = load_posko()
        jenis_list = load_jenis_donasi()

        while True:
            print(" >>> PILIH JENIS DONASI <<< ")
            for i, j in enumerate(jenis_list, start=1):
                print(f"{i}. {j['nama']}")
            
            pilihan_jenis = safe_int_input("Pilih jenis donasi (nomor): ", min_val=1, max_val=len(jenis_list), allow_cancel=False)
            if pilihan_jenis is None:
                print("Transaksi dibatalkan.")
                time.sleep(1)
                return
            
            jenis_donasi = jenis_list[pilihan_jenis - 1]['nama']
            break

        while True:
            clear_screen()
            print(" POSKO DONASI ")
            for i, p in enumerate(posko_list, start=1):
                print(f"{i}. {p['nama']}")
            
            pilihan = safe_int_input("Pilih posko (nomor): ", min_val=1, max_val=len(posko_list), allow_cancel=False)
            if pilihan is None:
                print("Transaksi dibatalkan.")
                time.sleep(1)
                return
            
            lokasi = posko_list[pilihan - 1]['nama']
            break

        while True:
            nama = safe_input("Nama Donatur: ")
            if nama is None:
                print("Transaksi dibatalkan.")
                time.sleep(1)
                return
            
            nama = nama.strip()
            if not nama:
                print("Nama tidak boleh kosong.")
                continue
            if not re.match(r'^[A-Za-z0-9 ]+$', nama):
                print("Nama hanya boleh berisi huruf, angka, dan spasi.")
                continue
            break

        while True:
            jumlah = safe_int_input("Jumlah Donasi: ", min_val=10_000, max_val=MAX_DONASI, allow_cancel=False)
            if jumlah is None:
                print("Transaksi dibatalkan.")
                time.sleep(1)
                return
            break

        if current_user["role"] == "Staff":
            metode = "Tunai (dicatat oleh Staff)"
            sisa_saldo = None
        else:
            for u in users:
                if u["username"] == current_user["username"]:
                    saldo_user = int(u.get("saldo", 0))
                    while saldo_user < jumlah:
                        print(f"Saldo tidak cukup (Rp{saldo_user:,}).")
                        top = safe_input("Ingin top up? (y/n): ")
                        if top is None:
                            print("Transaksi dibatalkan.")
                            time.sleep(1)
                            return
                        
                        if top.lower() == "y":
                            topup(current_user)
                            users = load_json(USER_FILE)
                            saldo_user = int(next(user['saldo'] for user in users if user['username'] == current_user['username']))
                        else:
                            print("Transaksi dibatalkan.")
                            safe_input("Tekan Enter untuk kembali...")
                            return
                    u["saldo"] = saldo_user - jumlah
                    sisa_saldo = u["saldo"]
                    save_json(USER_FILE, users)
                    metode = "E-Wallet"
                    break

        data.append({
            "username": current_user["username"],
            "nama": nama,
            "jenis_donasi": jenis_donasi,
            "jumlah": jumlah,
            "metode": metode,
            "lokasi": lokasi
        })
        save_json(DONASI_FILE, data)

        print("\n==== STRUK DONASI ====")
        print(f"Nama    : {nama}")
        print(f"Jenis   : {jenis_donasi}")
        print(f"Metode  : {metode}")
        print(f"Jumlah  : Rp{jumlah:,}")
        print(f"Lokasi  : {lokasi}")
        print("=========================")
        print("Status Donasi : SUKSES")
        print("TERIMA KASIH ATAS DONASINYA")
        if current_user["role"] == "User":
            print(f"Sisa Saldo Anda: Rp{int(sisa_saldo):,}")
        else:
            print("(Staff tidak menggunakan saldo)")
        safe_input("\nTekan Enter untuk kembali...")
    except KeyboardInterrupt:
        print("\n\nTransaksi dibatalkan.")
        time.sleep(1)

#EDIT DONASI(STAFF)
def edit_donasi(current_user):
    try:
        clear_screen()
        data = load_json(DONASI_FILE)
        posko_list = load_posko()
        jenis_list = load_jenis_donasi()
        
        if not data:
            print("Belum ada data donasi.")
            safe_input("Tekan Enter untuk kembali...")
            return
        
        while True:
            clear_screen()
            print(" >>> EDIT DONASI <<< \n")
            data_filtered = data
            if current_user["role"] == "User":
                data_filtered = [d for d in data if d.get("username") == current_user["username"]]
            
            if not data_filtered:
                print("Tidak ada data untuk diedit.")
                safe_input("Tekan Enter untuk kembali...")
                return
            
            tampilkan_tabel_donasi(current_user, data_filtered)
            
            nomor = safe_int_input("\nMasukkan nomor donasi yang ingin diedit (0 untuk batal): ", min_val=0, max_val=len(data_filtered))
            if nomor is None or nomor == 0:
                return
            
            d = data_filtered[nomor - 1]
            
            original_index = data.index(d)
            
            print(f"\n Edit data donasi untuk {d['nama']} ")
            
            if current_user["role"] == "Staff":
                new_nama = safe_input(f"Nama Donatur ({d['nama']}) [Enter = tidak berubah]: ")
                if new_nama is None:
                    return
                if new_nama.strip():
                    data[original_index]['nama'] = new_nama.strip()
                
                print("\nPilih jenis donasi baru:")
                for i, j in enumerate(jenis_list, start=1):
                    print(f"{i}. {j['nama']}")
                pilih_jenis = safe_input(f"Pilih jenis (1-{len(jenis_list)}) atau Enter untuk tidak mengubah: ")
                if pilih_jenis is None:
                    return
                
                pilih_jenis = pilih_jenis.strip()
                if pilih_jenis:
                    try:
                        idx = int(pilih_jenis)
                        if 1 <= idx <= len(jenis_list):
                            data[original_index]['jenis_donasi'] = jenis_list[idx - 1]['nama']
                        else:
                            print("Pilihan jenis tidak valid.")
                    except ValueError:
                        print("Input tidak valid.")
                
                print("\nPilih lokasi baru:")
                for i, p in enumerate(posko_list, start=1):
                    print(f"{i}. {p['nama']}")
                pilih_lokasi = safe_input(f"Pilih lokasi (1-{len(posko_list)}) atau Enter untuk tidak mengubah: ")
                if pilih_lokasi is None:
                    return
                
                pilih_lokasi = pilih_lokasi.strip()
                if pilih_lokasi:
                    try:
                        idx = int(pilih_lokasi)
                        if 1 <= idx <= len(posko_list):
                            data[original_index]['lokasi'] = posko_list[idx - 1]['nama']
                        else:
                            print("Pilihan lokasi tidak valid.")
                    except ValueError:
                        print("Input tidak valid.")
            else:
                new_nama = safe_input(f"Nama Donatur ({d['nama']}) [Enter = tidak berubah]: ")
                if new_nama is None:
                    return
                if new_nama.strip():
                    data[original_index]['nama'] = new_nama.strip()
                
                print("\nPilih jenis donasi baru:")
                for i, j in enumerate(jenis_list, start=1):
                    print(f"{i}. {j['nama']}")
                pilih_jenis = safe_input(f"Pilih jenis (1-{len(jenis_list)}) atau Enter untuk tidak mengubah: ")
                if pilih_jenis is None:
                    return
                
                pilih_jenis = pilih_jenis.strip()
                if pilih_jenis:
                    try:
                        idx = int(pilih_jenis)
                        if 1 <= idx <= len(jenis_list):
                            data[original_index]['jenis_donasi'] = jenis_list[idx - 1]['nama']
                        else:
                            print("Pilihan jenis tidak valid.")
                    except ValueError:
                        print("Input tidak valid.")
                
                jumlah_baru = safe_input(f"Jumlah Donasi ({d['jumlah']}) [Enter = tidak berubah]: ")
                if jumlah_baru is None:
                    return
                
                jumlah_baru = jumlah_baru.strip()
                if jumlah_baru:
                    try:
                        jumlah_baru = int(jumlah_baru)
                        if 10_000 <= jumlah_baru <= MAX_DONASI:
                            users = load_json(USER_FILE)
                            for u in users:
                                if u["username"] == current_user["username"]:
                                    saldo_user = int(u.get("saldo", 0)) + int(d['jumlah'])
                                    if jumlah_baru > saldo_user:
                                        print("Saldo tidak cukup untuk jumlah baru.")
                                    else:
                                        u["saldo"] = saldo_user - jumlah_baru
                                        save_json(USER_FILE, users)
                                        data[original_index]['jumlah'] = jumlah_baru
                                    break
                        else:
                            print(f"Jumlah harus antara Rp10.000 - Rp{MAX_DONASI:,}.")
                    except ValueError:
                        print("Jumlah harus angka.")
                
                print("\nPilih lokasi baru:")
                for i, p in enumerate(posko_list, start=1):
                    print(f"{i}. {p['nama']}")
                pilih_lokasi = safe_input(f"Pilih lokasi (1-{len(posko_list)}) atau Enter untuk tidak mengubah: ")
                if pilih_lokasi is None:
                    return
                
                pilih_lokasi = pilih_lokasi.strip()
                if pilih_lokasi:
                    try:
                        idx = int(pilih_lokasi)
                        if 1 <= idx <= len(posko_list):
                            data[original_index]['lokasi'] = posko_list[idx - 1]['nama']
                        else:
                            print("Pilihan lokasi tidak valid.")
                    except ValueError:
                        print("Input tidak valid.")
            
            save_json(DONASI_FILE, data)
            print("\n✓ Data donasi berhasil diperbarui.")
            safe_input("Tekan Enter untuk kembali...")
            return
            
    except KeyboardInterrupt:
        print("\n\nEdit dibatalkan.")
        time.sleep(1)

#HAPUS DONASI(STAFF)
def hapus_donasi(current_user):
    try:
        clear_screen()
        data = load_json(DONASI_FILE)
        
        if not data:
            print("Belum ada data donasi.")
            safe_input("Tekan Enter untuk kembali...")
            return
        
        while True:
            clear_screen()
            print(">>> HAPUS DONASI <<<\n")
            data_filtered = data
            if current_user["role"] == "User":
                data_filtered = [d for d in data if d.get("username") == current_user["username"]]
            
            if not data_filtered:
                print("Tidak ada data untuk dihapus.")
                safe_input("Tekan Enter untuk kembali...")
                return
            
            tampilkan_tabel_donasi(current_user, data_filtered)
            
            nomor = safe_int_input("\nMasukkan nomor donasi yang ingin dihapus (0 untuk batal): ", min_val=0, max_val=len(data_filtered))
            if nomor is None or nomor == 0:
                return
            
            d = data_filtered[nomor - 1]
            
            konfirmasi = safe_input(f"Yakin hapus donasi '{d['nama']}'? (y/n): ")
            if konfirmasi is None:
                return
            
            if konfirmasi.lower() == 'y':
                data.remove(d)
                save_json(DONASI_FILE, data)
                print("✓ Data donasi berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            safe_input("Tekan Enter untuk kembali...")
            return
            
    except KeyboardInterrupt:
        print("\n\nOperasi dibatalkan.")
        time.sleep(1)

#TOPAP
def topup(current_user):
    try:
        clear_screen()
        users = load_json(USER_FILE)
        
        while True:
            nominal = safe_int_input("Masukkan nominal top up: ", min_val=15_000, max_val=MAX_TOPUP, allow_cancel=False)
            if nominal is None:
                print("Top up dibatalkan.")
                time.sleep(1)
                return
            break
        
        for u in users:
            if u["username"] == current_user["username"]:
                saldo_sekarang = int(u.get("saldo", 0))
                if saldo_sekarang + nominal > MAX_SALDO:
                    print(f"Saldo tidak boleh melebihi Rp{MAX_SALDO:,}")
                    safe_input("Tekan Enter untuk kembali...")
                    return
                u["saldo"] = saldo_sekarang + nominal
                save_json(USER_FILE, users)
                print("Memproses top up...")
                time.sleep(0.8)
                print(f"✓ Top up berhasil. Saldo saat ini: Rp{u['saldo']:,}")
                safe_input("Tekan Enter untuk kembali...")
                return
    except KeyboardInterrupt:
        print("\n\nTop up dibatalkan.")
        time.sleep(1)

#CEK SALDO(USER)
def cek_saldo(current_user):
    try:
        clear_screen()
        users = load_json(USER_FILE)
        for u in users:
            if u["username"] == current_user["username"]:
                print(f"Saldo Anda: Rp{int(u.get('saldo', 0)):,}")
                safe_input("Tekan Enter untuk kembali...")
                return
    except KeyboardInterrupt:
        print("\n\nOperasi dibatalkan.")
        time.sleep(1)

#MENU USER
def menu_user(user):
    try:
        while True:
            clear_screen()
            print(f" >>> MENU USER <<< ({user['username']}) ")
            print("1. Tambah Donasi")
            print("2. Lihat Donasi")
            print("3. Top Up Saldo")
            print("4. Cek Saldo")
            print("0. Logout")
            pilih = safe_input("Pilih menu: ")
            
            if pilih is None:
                continue
            
            pilih = pilih.strip()
            
            if pilih == "1":
                tambah_donasi(user)
            elif pilih == "2":
                lihat_donasi(user)
            elif pilih == "3":
                topup(user)
            elif pilih == "4":
                cek_saldo(user)
            elif pilih == "0":
                break
            else:
                print("Pilihan tidak valid.")
                safe_input("Tekan Enter untuk lanjut...")
    except KeyboardInterrupt:
        print("\n\nLogout paksa.")
        time.sleep(1)

#MENU STAFF
def menu_staff(user):
    try:
        while True:
            clear_screen()
            print(f" >>> MENU STAFF ({user['username']}) <<< ")
            print("1. Kelola Donasi")
            print("0. Logout")
            pilih = safe_input("Pilih menu: ")
            
            if pilih is None:
                continue
            
            pilih = pilih.strip()
            
            if pilih == "1":
                menu_kelola_donasi(user)
            elif pilih == "0":
                break
            else:
                print("Pilihan tidak valid.")
                safe_input("Tekan Enter untuk lanjut...")
    except KeyboardInterrupt:
        print("\n\nLogout paksa.")
        time.sleep(1)

#KELOLA DONASI
def menu_kelola_donasi(user):
    try:
        while True:
            clear_screen()
            print(f" >>> KELOLA DONASI ({user['username']}) <<< \n")

            menu_table = PrettyTable(["No", "Menu", "Keterangan"])
            menu_table.align["Menu"] = "l"
            menu_table.align["Keterangan"] = "l"
            menu_table.hrules = 1
            menu_table.add_row(["1", "Tambah Jenis Donasi", "Menambah kategori donasi baru"])
            menu_table.add_row(["2", "Tambah Posko", "Menambah lokasi posko baru"])
            menu_table.add_row(["3", "Lihat Donasi", "Melihat semua data donasi"])
            menu_table.add_row(["4", "Lihat Jenis Donasi", "Melihat daftar kategori donasi"])
            menu_table.add_row(["5", "Lihat Posko", "Melihat daftar lokasi posko"])
            menu_table.add_row(["6", "Edit Donasi", "Mengubah data donasi yang ada"])
            menu_table.add_row(["7", "Hapus Posko", "Menghapus lokasi posko"])
            menu_table.add_row(["0", "Kembali", "Kembali ke menu Staff"])
            
            print(menu_table)
            
            pilih = safe_input("\nPilih menu: ")
            
            if pilih is None:
                continue
            
            pilih = pilih.strip()
            
            if pilih == "1":
                tambah_jenis_donasi()
            elif pilih == "2":
                tambah_posko()
            elif pilih == "3":
                lihat_donasi(user)
            elif pilih == "4":
                lihat_jenis_donasi()
            elif pilih == "5":
                lihat_posko()
            elif pilih == "6":
                edit_donasi(user)
            elif pilih == "7":
                hapus_posko()
            elif pilih == "0":
                break
            else:
                print("Pilihan tidak valid.")
                safe_input("Tekan Enter untuk lanjut...")
    except KeyboardInterrupt:
        print("\n\nKembali ke menu sebelumnya.")
        time.sleep(1)

def main():
    try:
        load_posko()
        load_jenis_donasi()
        
        while True:
            clear_screen()
            print(" SISTEM DONASI ")
            print("1. Login")
            print("2. Register")
            print("0. Keluar")
            pilihan = safe_input("Pilih menu: ")
            
            if pilihan is None:
                continue
            
            pilihan = pilihan.strip()
            
            if pilihan == "1":
                user = login()
                if user:
                    if user["role"] == "Staff":
                        menu_staff(user)
                    else:
                        menu_user(user)
            elif pilihan == "2":
                register()
            elif pilihan == "0":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid.")
                safe_input("Tekan Enter untuk lanjut...")
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user.")
        print("Terima kasih telah menggunakan Sistem Donasi!")
    except Exception as e:
        print(f"\nTerjadi error tidak terduga: {e}")
        print("Program akan ditutup.")
    finally:
        time.sleep(1)

main()
