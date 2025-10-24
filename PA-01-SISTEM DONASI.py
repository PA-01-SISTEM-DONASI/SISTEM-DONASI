import json
import os
import stdiomask
import time
import re
from prettytable import PrettyTable

USER_FILE = 'users.json'
DONASI_FILE = 'data_donasi.json'
LOKASI = [
    "Posko A - Sangatta",
    "Posko B - Bengalon",
    "Posko C - Muara Wahau",
    "Posko D - Rantau Pulung"
]
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
        return json.load(f)

def save_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

#BUAT REGIST USER
def register():
    clear_screen()
    users = load_json(USER_FILE)
    username = input("Username baru: ")
    password = stdiomask.getpass("Password: ")

    if not re.match(r'^[A-Za-z0-9_]+$', username):
        print("Username hanya boleh berisi huruf, angka, dan underscore (_).")
        input("Tekan Enter untuk kembali...")
        return
    
    for u in users:
        if u["username"] == username:
            print("Username sudah terdaftar.")
            input("Tekan Enter untuk kembali...")
            return

    users.append({
        "username": username,
        "password": password,
        "role": "User",
        "saldo": 0
    })
    save_json(USER_FILE, users)
    print("Registrasi berhasil!")
    input("Tekan Enter untuk kembali...")

#BUAT LOGIN
def login():
    clear_screen()
    users = load_json(USER_FILE)
    attempts = LOGIN_ATTEMPTS

    while attempts > 0:
        try:
            username = input("Username: ")
            password = stdiomask.getpass("Password: ")
        except (KeyboardInterrupt, EOFError):
            print("\nInput dibatalkan.")
            return None

        for u in users:
            if u["username"] == username and u["password"] == password:
                u["saldo"] = int(u.get("saldo", 0))
                print("Login berhasil. Menyiapkan akun...")
                time.sleep(1)
                return u

        attempts -= 1
        print(f"Username atau password salah. Sisa percobaan: {attempts}")
        if attempts == 0:
            print("Kesempatan login habis. Kembali ke menu utama.")
            time.sleep(1)
            return None

#BUAT NAMPILIN DATA DONASI
def tampilkan_donasi(current_user=None):
    clear_screen()
    data = load_json(DONASI_FILE)
    if not data:
        print("Belum ada data donasi.")
        input("Tekan Enter untuk kembali...")
        return

    if current_user and current_user["role"] == "User":
        data = [d for d in data if d.get("username") == current_user["username"]]

    if not data:
        print("Tidak ada donasi untuk akun ini.")
        input("Tekan Enter untuk kembali...")
        return

    table = PrettyTable(["Nama Donatur", "Jumlah", "Metode", "Lokasi"])
    total = 0
    for d in data:
        jumlah_int = int(d.get("jumlah", 0))
        total += jumlah_int
        table.add_row([d.get("nama", "-"), f"Rp{jumlah_int:,}", d.get("metode", "-"), d.get("lokasi", "-")])

    print(table)

#NAMPILIN TOTAL DONASI NYA USER
    if current_user and current_user["role"] == "Staff":
        print(f"\nTotal Donasi Keseluruhan: Rp{total:,}")
    else:
        print(f"\nTotal Donasi Anda: Rp{total:,}")

    input("\nTekan Enter untuk kembali...")


def tambah_donasi(current_user):
    clear_screen()
    data = load_json(DONASI_FILE)
    users = load_json(USER_FILE)

    print("=== PILIH LOKASI DONASI ===")
    for i, l in enumerate(LOKASI, start=1):
        print(f"{i}. {l}")
    try:
        pilihan = int(input("Pilih lokasi (nomor): "))
        if not (1 <= pilihan <= len(LOKASI)):
            print("Pilihan lokasi tidak valid.")
            input("Tekan Enter untuk kembali...")
            return
    except ValueError:
        print("Input lokasi harus angka.")
        input("Tekan Enter untuk kembali...")
        return

    lokasi = LOKASI[pilihan - 1]
    nama = input("Nama Donatur: ")
    if not re.match(r'^[A-Za-z0-9 ]+$', nama):
        print("Nama hanya boleh berisi huruf, angka, dan spasi.")
        input("Tekan Enter untuk kembali...")
        return
    
    try:
        jumlah = int(input("Jumlah Donasi: "))
    except ValueError:
        print("Jumlah harus angka.")
        input("Tekan Enter untuk kembali...")
        return

    if jumlah < 10_000:
        print("Minimal donasi adalah Rp10.000.")
        input("Tekan Enter untuk kembali...")
        return
    if jumlah > MAX_DONASI:
        print(f"Maksimal donasi adalah Rp{MAX_DONASI:,}")
        input("Tekan Enter untuk kembali...")
        return

    if current_user["role"] == "Staff":
        metode = "Tunai (dicatat oleh Staff)"
        sisa_saldo = None
    else:
        for u in users:
            if u["username"] == current_user["username"]:
                saldo_user = int(u.get("saldo", 0))
                if saldo_user < jumlah:
                    print("Saldo tidak cukup.")
                    top = input("Ingin top up? (y/n): ").lower()
                    if top == "y":
                        topup(current_user)
                    else:
                        print("Transaksi dibatalkan.")
                        input("Tekan Enter untuk kembali...")
                        return
                    
                saldo_user = int(u.get("saldo", 0))
                if saldo_user < jumlah:
                    print("Saldo masih tidak cukup.")
                    input("Tekan Enter untuk kembali...")
                    return
                u["saldo"] = saldo_user - jumlah
                sisa_saldo = u["saldo"]
                save_json(USER_FILE, users)
                metode = "E-Wallet"
                break

    # Simpan donasi ke file
    data.append({
        "username": current_user["username"],
        "nama": nama,
        "jumlah": jumlah,
        "metode": metode,
        "lokasi": lokasi
    })
    save_json(DONASI_FILE, data)

    # Tampilkan struk
    print("\n===== STRUK DONASI =====")
    print(f"Nama    : {nama}")
    print(f"Metode  : {metode}")
    print(f"Jumlah  : Rp{jumlah:,}")
    print(f"Lokasi  : {lokasi}")
    print("========================")
    print("Status Donasi : SUKSES")
    print("TERIMA KASIH ATAS DONASINYA")

    if current_user["role"] == "User":
        print(f"Sisa Saldo Anda: Rp{int(sisa_saldo):,}")
    else:
        print("(Staff tidak menggunakan saldo)")

    input("\nTekan Enter untuk kembali...")


def edit_donasi(current_user):
    clear_screen()
    data = load_json(DONASI_FILE)
    if not data:
        print("Belum ada data donasi.")
        input("Tekan Enter untuk kembali...")
        return

    tampilkan_donasi(current_user)
    nama = input("Masukkan nama donatur yang ingin diedit: ")

    for d in data:
        if d.get("nama", "").lower() == nama.lower() and (current_user["role"] == "Staff" or d.get("username") == current_user["username"]):
            print(f"\nEdit data donasi untuk {d['nama']}")

            if current_user["role"] == "Staff":
                d['nama'] = input(f"Nama Donatur ({d['nama']}): ") or d['nama']

                print("\n=== PILIH LOKASI BARU ===")
                for i, l in enumerate(LOKASI, start=1):
                    print(f"{i}. {l}")
                pilih_lokasi = input(f"Pilih lokasi (1-{len(LOKASI)}) atau Enter untuk tidak mengubah: ")
                if pilih_lokasi.strip():
                    try:
                        idx = int(pilih_lokasi)
                        if 1 <= idx <= len(LOKASI):
                            d['lokasi'] = LOKASI[idx - 1]
                        else:
                            print("Pilihan lokasi tidak valid. Lokasi tidak diubah.")
                    except ValueError:
                        print("Input tidak valid. Lokasi tidak diubah.")

            else:
                d['nama'] = input(f"Nama Donatur ({d['nama']}): ") or d['nama']
                try:
                    d['jumlah'] = int(input(f"Jumlah Donasi ({d['jumlah']}): ") or d['jumlah'])
                except ValueError:
                    print("Jumlah harus angka. Edit dibatalkan.")
                    input("Tekan Enter untuk kembali...")
                    return
                d['lokasi'] = input(f"Lokasi ({d['lokasi']}): ") or d['lokasi']

            save_json(DONASI_FILE, data)
            print("Data donasi berhasil diperbarui.")
            input("Tekan Enter untuk kembali...")
            return
    print("Data donatur tidak ditemukan.")
    input("Tekan Enter untuk kembali...")

def hapus_donasi(current_user):
    clear_screen()
    data = load_json(DONASI_FILE)
    if not data:
        print("Belum ada data donasi.")
        input("Tekan Enter untuk kembali...")
        return

    tampilkan_donasi(current_user)
    nama = input("Masukkan nama donatur yang ingin dihapus: ")

    for i, d in enumerate(data):
        if d.get("nama", "").lower() == nama.lower() and (current_user["role"] == "Staff" or d.get("username") == current_user["username"]):
            konfirmasi = input(f"Yakin hapus donasi '{d['nama']}'? (y/n): ").lower()
            if konfirmasi == 'y':
                del data[i]
                save_json(DONASI_FILE, data)
                print("Data donasi berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            input("Tekan Enter untuk kembali...")
            return
    print("Data donatur tidak ditemukan.")
    input("Tekan Enter untuk kembali...")

def total_donasi():
    clear_screen()
    data = load_json(DONASI_FILE)
    total = sum(int(d.get("jumlah", 0)) for d in data)
    print(f"Total Donasi Keseluruhan: Rp{total:,}")
    input("Tekan Enter untuk kembali...")

#INI UNTUK TOP AP DAP
def topup(current_user):
    clear_screen()
    users = load_json(USER_FILE)
    try:
        nominal = int(input("Masukkan nominal top up: "))
    except ValueError:
        print("Nominal harus angka.")
        input("Tekan Enter untuk kembali...")
        return

    if nominal <= 14_999:
        print("Minimal top up adalah Rp.15.000.")
        input("Tekan Enter untuk kembali...")
        return
    if nominal > MAX_TOPUP:
        print(f"Maksimal top up per transaksi adalah Rp{MAX_TOPUP:,}")
        input("Tekan Enter untuk kembali...")
        return

    for u in users:
        if u["username"] == current_user["username"]:
            saldo_sekarang = int(u.get("saldo", 0))
            saldo_baru = saldo_sekarang + nominal

            if saldo_baru > MAX_SALDO:
                print(f"Saldo tidak boleh melebihi Rp{MAX_SALDO:,}")
                input("Tekan Enter untuk kembali...")
                return

            u["saldo"] = saldo_baru
            save_json(USER_FILE, users)
            print("Memproses top up...")
            time.sleep(0.8)
            print(f"Top up berhasil. Saldo saat ini: Rp{u['saldo']:,}")
            input("Tekan Enter untuk kembali...")
            return

def cek_saldo(current_user):
    clear_screen()
    users = load_json(USER_FILE)
    for u in users:
        if u["username"] == current_user["username"]:
            print(f"Saldo Anda: Rp{int(u.get('saldo', 0)):,}")
            input("Tekan Enter untuk kembali...")
            return

#MENU UTAMA USER INI DAP
def menu_user(user):
    while True:
        clear_screen()
        print(f"=== MENU USER ({user['username']}) ===")
        print("1. Tambah Donasi")
        print("2. Lihat Donasi")
        print("3. Top Up Saldo")
        print("4. Cek Saldo")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_donasi(user)
        elif pilih == "2":
            tampilkan_donasi(user)
        elif pilih == "3":
            topup(user)
        elif pilih == "4":
            cek_saldo(user)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

#INI KALAU LOGIN STAFF
def menu_staff(user):
    while True:
        clear_screen()
        print(f"=== MENU STAFF ({user['username']}) ===")
        print("1. Tambah Donasi")
        print("2. Lihat Donasi (tampilkan total)")
        print("3. Edit Donasi")
        print("4. Hapus Donasi")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_donasi(user)
        elif pilih == "2":
            tampilkan_donasi(user)
        elif pilih == "3":
            edit_donasi(user)
        elif pilih == "4":
            hapus_donasi(user)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

#PROGRAM UTAMA INI DAP
def main():
    while True:
        clear_screen()
        print("=== SISTEM DONASI ===")
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

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
            input("Tekan Enter untuk lanjut...")
main()
