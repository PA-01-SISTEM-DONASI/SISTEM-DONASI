import json
import stdiomask
# from prettytable import PrettyTable


DATA_FILE = 'data_donasi.json'

#MEMBACA PRODUK INI DAP
def baca_produk():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print("Error membaca file:", e)
        return []

#INI AKUN NYA DAP
users = {
    "staff": {"password": 12345, "role": "Staff"},
    "user": {"password": 67890, "role": "user"},
}

#INI BUAT DONASI NYA DAP/ CRUD BAGIAN CREATE
def donasi():
    try:
        nama = input("Masukkan nama: ")
        print("\n1. Ewallet")
        print("\n2. Offline")
        Method = input("Masukkan Method: ")
        if Method == "1":
            Method = "EWALLET"
            norek = int(input("Masukkan Norek: "))
            jumlah = int(input("Masukkan Jumlah: "))
            data = baca_produk()
            # data.append({"nama_pendonasi": nama, "method": Method, "norek": norek, "jumlah": jumlah})
            # with open(DATA_FILE, 'w') as f:
            #     json.dump(data, f, indent=4)
            # print("DONASI BERHASIL DITAMBAHKAN")
            print("========================")
            print("===== STRUK DONASI =====")
            print("========================")
            print("\nNama    : ", nama)
            print("\nMethod  : ", "EWALLET")
            print("\nNorek   : ", norek)
            print("\nJumlah  : ", jumlah)
            print("\n========================")
            print("Status Donasi : SUCCES")
            print("TERIMAKASIH ATAS DONASINYA")
        elif Method == "2":
            norek = "-"
            jumlah = int(input("Masukkan Jumlah: "))
            data = baca_produk()
            print("========================")
            print("===== STRUK DONASI =====")
            print("========================")
            print("\nNama    : ", nama)
            print("\nMethod  : ", "OFFLINE")
            print("\nNorek   : ", norek)
            print("\nJumlah  : ", jumlah)
            print("\n========================")
            print("Status Donasi : SUCCES")
            print("TERIMAKASIH ATAS DONASINYA")
    except Exception as e:
        print("Terjadi kesalahan:", e)

#INI BUAT CRUD BAGIAN READ
# def lihat_donasi():
#     try:
#         with open(DATA_FILE, 'r') as f:
#             data = json.load(f)
#         print("\nData Donasi:")
#         for p in data:
#             print(p)
#         return data
#     except Exception as e:
#         print("Error membaca file:", e)
#         return []

#INI BAGIAN LOGINNYA DAP
def login():
    print("=== SISTEM LOGIN PENCATATAN DONASI ===")
    attempts = 3

    while attempts > 0:
        username = input("Username (staff/user): ").lower()
        try:
            pw_input = stdiomask.getpass("Password (hanya angka): ")
            password = int(pw_input) 
        except ValueError:
            print("Password harus berupa angka!\n")
            attempts -= 1
            print(f"Sisa kesempatan: {attempts}")
            continue
        except Exception as e:
            print("Terjadi kesalahan saat input password:", e)
            attempts -= 1
            print(f"Sisa kesempatan: {attempts}")
        except KeyboardInterrupt:
            print("\nJangan klik ctrl+c yah")
        except EOFError:
            print("\nJangan klik ctrl+z yah")
            continue

        if username in users and users[username]["password"] == password:
            print(f"Login berhasil sebagai {users[username]['role']}")
            return users[username]["role"]
        else:
            attempts -= 1
            print("Username atau password salah.")
            print(f"Sisa kesempatan: {attempts}\n")

    print("Kesempatan login habis. Program dihentikan.")
    return None

# def update_donasi():
#     try:
#         nama = input("Masukkan nama donatur yang ingin diupdate: ")
#         norek = int(input("Masukkan norek baru: "))
#         jumlah = int(input("Masukkan jumlah baru: "))
#         data = baca_produk()
#         updated = False
#         for p in data:
#             if p['nama'] == nama:
#                 p['norek'] = norek
#                 p['jumlah'] = jumlah
#                 updated = True
#         with open(DATA_FILE, 'w') as f:
#             json.dump(data, f, indent=4)
#         if updated:
#             print("Produk berhasil diupdate!")
#         else:
#             print("Produk tidak ditemukan.")
#     except Exception as e:
#         print("Terjadi kesalahan:", e)

#INI MENU UTAMA DAP
def main():
    role = login()
    if not role:
        return

    while True:
        print("\n=== SISTEM PENCATATAN DONASI ===")
        print("1. DONATE")
        if role == "Staff":
            # print("2. LIHAT DONATE")
            # print("3. UPDATE DONATE")
            # print("4. HAPUS DONATE")
            print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            donasi()
        # elif pilihan == "2" and role == "Staff":
        #     lihat_donasi()
        # elif pilihan == "3" and role == "Staff":
        #     update_donasi()
        # elif pilihan == "4" and role == "Staff":
        #     hapus_donasi()
        # elif pilihan == "0":
        #     print("Keluar dari program. ")
        #     break
        # else:
        #     print("Pilihan tidak valid atau tidak punya akses.")

main()