from cProfile import label
import os
from urllib.request import HTTPDigestAuthHandler
import matplotlib.pyplot as plt
import numpy as np

dict_user = {
    "username" : "erinazr", 
    "password" : "12345"
}
tab_darurat = 0
tab_biasa = 0
tab_pendidikan = 0

#index[1] = tabungan darurat
#index[2] = tabungan biasa
#index[3] = tabungan pendidikan
in_tabungan = [0, 0, 0]
out_tabungan = [0, 0, 0]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali ke menu >>>")
    start_program()

def back_to_login():
    print("\n")
    input("Tekan Enter untuk kembali ke halaman login >>>")
    clear_screen()
    login()

def show_tabungan():
    print(
        "\n===Daftar Tabungan===", "\n"
        "1. Tabungan Darurat\n"
        "2. Tabungan Biasa\n"
        "3. Tabungan Pendidikan\n"
    )

def tambah_saldo():
        show_tabungan()
        try:
            input_namtab = input("Masukkan pilihan tabungan: ")
            input_saldo = int(input("Masukkan nominal yang akan ditambahkan: Rp"))
        except ValueError:
            print("Input saldo hanya bisa dilakukan dengan angka integer.")
        except:
            print("Terdapat kesalahan saat menginput saldo.")
        else:
            if input_namtab == '1':
                global tab_darurat
                tab_darurat += input_saldo
                in_tabungan[0] += input_saldo
                print(f"Saldo sebesar Rp{input_saldo} telah ditambahkan ke tabungan darurat.", "\n")
            elif input_namtab == '2':
                global tab_biasa
                tab_biasa += input_saldo
                in_tabungan[1] += input_saldo
                print(f"Saldo sebesar Rp{input_saldo} telah ditambahkan ke tabungan biasa.", "\n")
            elif input_namtab == '3':
                global tab_pendidikan
                tab_pendidikan += input_saldo
                in_tabungan[2] += input_saldo
                print(f"Saldo sebesar Rp{input_saldo} telah ditambahkan ke tabungan pendidikan.", "\n")
            else:
                print("Tabungan tidak ditemukan.", "\n")
        finally:
            back_to_menu()

def tarik_saldo():
    show_tabungan()
    try:
        input_namtab = input("Masukkan pilihan tabungan: ")
        input_saldo = int(input("Masukkan nominal yang akan diambil: Rp"))
    except ValueError:
        print("Input saldo hanya bisa dilakukan dengan angka integer.")
    except:
        print("Terdapat kesalahan saat memproses transaksi.")
    else:
        if input_namtab == '1':
            global tab_darurat
            if input_saldo <= tab_darurat:
                tab_darurat -= input_saldo
                out_tabungan[0] += input_saldo
                print(f"Saldo sebesar Rp{input_saldo} telah diambil dari tabungan darurat.", "\n")
            else:
                print("Saldo tidak mencukupi.", "\n")
        elif input_namtab == '2':
            global tab_biasa
            if input_saldo <= tab_biasa:
                tab_biasa -= input_saldo
                out_tabungan[1] += input_saldo
                print(f"Saldo sebesar Rp{input_saldo} telah diambil dari tabungan biasa.", "\n")
            else:
                print("Saldo tidak mencukupi.")
        elif input_namtab == '3':
            global tab_pendidikan
            if input_saldo <= tab_pendidikan:
                tab_pendidikan -= input_saldo
                out_tabungan[2] += input_saldo
                print(f"Saldo sebesar Rp{input_saldo} telah diambil dari tabungan pendidikan.", "\n")
            else:
                print("Saldo tidak mencukupi.", "\n")
        else:
            print("Tabungan tidak ditemukan.", "\n")
    finally:
        back_to_menu()

def cek_saldo():
    global tab_darurat
    global tab_biasa
    global tab_pendidikan
    print(
        "Saldo Tabungan\n"
        f"1. Tabungan Darurat: {tab_darurat}",
        f"\n2. Tabungan Biasa: {tab_biasa}"
        f"\n3. Tabungan Pendidikan: {tab_pendidikan}"
    )
    back_to_menu()

def tampil_data():
    print("*"*40, "\nData Pemasukkan dan Pengeluaran Tabungan")
    print("*"*40, "\n")
    print(
        "1. Tabungan Darurat\n", f"Pemasukkan: Rp{in_tabungan[0]}\n", f"Pengeluaran: Rp{out_tabungan[0]}\n", "\n"
        "2. Tabungan Biasa\n", f"Pemasukkan: Rp{in_tabungan[1]}\n", f"Pengeluaran: Rp{out_tabungan[1]}\n", "\n"
        "3. Tabungan Pendidikan\n", f"Pemasukkan: Rp{in_tabungan[2]}\n", f"Pengeluaran: Rp{out_tabungan[2]}\n", "\n"
    )
    back_to_menu()

def pie_chart():
    global tab_darurat
    global tab_biasa
    global tab_pendidikan
    label = ['Tabungan Darurat', 'Tabungan Biasa', 'Tabungan Pendidikan']
    quantity_tab = [tab_darurat, tab_biasa, tab_pendidikan]
    warna = ['brown', 'burlywood', 'cornsilk']

    plt.title("Presentase Saldo Tabungan")
    plt.pie(quantity_tab, labels=label, colors=warna,
        autopct='%1.2f%%', startangle=90)
    
    plt.axis('equal')
    plt.show()

def bar_plot():
    label = ['Tabungan Darurat', 'Tabungan Biasa', 'Tabungan Pendidikan']

    x = np.arange(len(label))
    width = 0.35
    fig, ax = plt.subplots(figsize=(12, 7))

    pemasukkan = ax.bar(x - width/2, in_tabungan, width, label='Pemasukkan', color='mediumseagreen')
    pengeluaran = ax.bar(x + width/2, out_tabungan, width, label='Pengeluaran', color='indianred')

    ax.set_title('Pemasukkan dan Pengeluaran Tabungan')
    ax.set_ylabel('Saldo')
    ax.set_xticks(x)
    ax.set_xticklabels(label)
    ax.legend()

    plt.show()

def start_program():
    if __name__ == "__main__":
        while True:
            clear_screen()
            print(
                ">>> Aplikasi Tabungan Sederhana <<<"
                "\n"
                "\nMenu:"
                "\n[1] Tambah saldo tabungan"
                "\n[2] Cek saldo tabungan"
                "\n[3] Tarik saldo tabungan"
                "\n[4] Tampilkan data pemasukkan dan pengeluaran"
                "\n[5] Tampilkan pie chart tabungan"
                "\n[6] Tampilkan bar plot tabungan"
                "\n[0] Exit"
                "\n================================", "\n"
            )
            input_user = input("Pilih menu > ")
            if input_user == '1':
                tambah_saldo()
            elif input_user == '2':
                cek_saldo()
            elif input_user == '3':
                tarik_saldo()
            elif input_user == '4':
                tampil_data()
            elif input_user == '5':
                pie_chart()
            elif input_user == '6':
                bar_plot()
            elif input_user == "0":
                print("Terima kasih telah menggunakan program tabungan ini.")
                break
            else:
                print(f"Menu {input_user} tidak tersedia.")

def login():
    clear_screen()
    print("***LOGIN***")
    for i in range(3):
        in_user = input("Username: ")
        in_psw = input("Password: ")
        if in_user != dict_user["username"] or in_psw != dict_user["password"]:
            print(f"Username atau password salah, sisa percobaan login: {2-i}.")
        else:
            start_program()
            break

try:
    login()
except NameError:
    print("Terdapat kesalahan dalam penulisan variabel.")
except TypeError:
    print("Tipe data yang digunakan tidak sesuai.")