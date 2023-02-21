# Mengimpor semua metode dari Transaksi
from Transaction import *

trnsct = Transaction() # Buat objek kelas Transaksi

# Main menu of Super Cashier Machine
print('''
-----------------------------------------------
       WELCOME TO SUPER CASHIER MACHINE!!!          
-----------------------------------------------
''')

while True:
    tables = [
            ["Silahkan pilih Feature: "],
            ["1. Tambah Item Barang Belanja"],
            ["2. Periksa Order / Keranjang Belanjaan"],
            ["3. Menghapus Item Barang Dari Keranjang Belanjaan"],
            ["4. Reset Transaksi Belanja (Menghapus Semua Item Barang Belanja)"],
            ["5. Update Nama Item Belanja"],
            ["6. Update Kuantitas Item Belanja"],
            ["7. Update Harga Item Belanja"],
            ["8. Hitung Total Harga Belanja"],
            ["9. Tutup Program"]
            ]    
    headers = ["Menu"]
    print("Super Cashier Machine")
    print("-"*68)
    print(tabulate(tables, headers, tablefmt='github', stralign="center"))
 
    number = int(input('Input Nomor Feature: '))
    if number == 1:
        trnsct.add_item()
    elif number == 2:
        trnsct.check_order()
        print('---------------------------------------------------------')
    elif number == 3:
        trnsct.delete_item()
        print('---------------------------------------------------------')
    elif number == 4:
        trnsct.reset_transaction()
        print('---------------------------------------------------------')
    elif number == 5:
        trnsct.update_item_name()
        print('---------------------------------------------------------')
    elif number == 6:
        trnsct.update_item_quantity()
        print('---------------------------------------------------------')
    elif number == 7:
        trnsct.update_item_price()
        print('---------------------------------------------------------')
    elif number == 8:
        trnsct.total_price()
        print('---------------------------------------------------------')
    elif number == 9:
        print('''
        -----------------------------------------------
           Thank you for using Super Cashier Machine!
        -----------------------------------------------
        ''')
        break