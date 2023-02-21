# Importing tabulate
from tabulate import tabulate

class Transaction:
    '''Kelas untuk tujuan transaksi.'''

    def __init__(self):
        # Menginisialisasi kamus keranjang belanja kosong
        self.shopping_cart = {}
    
    def add_item(self):
        '''
        Metode untuk menambahkan satu atau lebih item ke keranjang belanja
        
        Parameter:
             item_name (str): Nama produk
             kuantitas (int): Jumlah produk
             harga (int): Harga satuan produk
             continue_loop (str): indikator istirahat/lanjut perulangan
        '''
        #while loop untuk menambahkan item secara terus menerus jika diinginkan
        while True:
            try: #menginisialisasi penanganan pengecualian
                 #Masukkan nama barang, jumlah, dan harga#initialize exception handling
                #Input item name, quantity, and price
                self.item_name = input('Input Nama Produk: ').capitalize()
                self.quantity = int(input('Input Kuantitas: '))
                self.price = int(input('Input Harga Produk: '))

            except ValueError:
                    # Menampilkan Peringatan kesalahan dan instruksi kemudian melanjutkan perulangan
                    print('Kuantitas atau harga harus numerik')
                    print('Silahkan Input Yang Valid')
                    print('---------------------------------------------------------')
                    continue
            
            # Shows produk yang ditambah
            print(f'{self.item_name} dengan kuantitas sebanyak {self.quantity} '
                f'dan harga satuan {self.price} ditambahkan ke keranjang belanjaan')
            print('---------------------------------------------------------') 
            
            # Perbarui kamus shopping_cart dengan item yang ditambahkan
            self.shopping_cart.update({self.item_name: [self.quantity, self.price]})
                
            # While loop untuk menyimpan indikator break perulangan 
            while True:
                #Input indikator istirahat perulangan
                self.continue_loop = input('Tambah Produk? (y/n): ').lower()
                #Jika inputnya benar, hentikan loop
                if self.continue_loop == 'n':
                    break
                elif self.continue_loop == 'y':
                    break
                
                # Menampilkan instruksi untuk input yang salah
                print('Silahkan Input "y" or "n"')
                print('---------------------------------------------------------')
            
            # Bersyarat untuk memutus perulangan jika indikatornya adalah "n"
            # atau lanjutkan perulangan jika indikatornya "y"
            if self.continue_loop == 'n':
                break
            else:
                continue

    def update_item_name(self):
        '''
        Metode untuk memperbarui nama barang di keranjang belanja
        
        Parameter:
             item_name (str): Nama produk yang perlu diubah
             new_item_name (str): Nama baru untuk produk
        '''
        # While loop untuk membiarkan pengguna mencoba lagi jika inputnya salah
        while True:
            # Input nama item
            self.item_name = input('Nama Produk: ').capitalize()
            # Indikator untuk mengecek apakah nama item sudah masuk
            # Keranjang belanja atau tidak
            is_in_cart = self.item_name in self.shopping_cart.keys()

            # Bersyarat untuk mengubah nama item lalu memutus loop
            # jika indikatornya Benar
            if is_in_cart == True:
                # Input Nama item yang akan di update
                self.new_item_name = input('Nama Produk di Update: ').capitalize()
                self.shopping_cart[self.new_item_name] = self.shopping_cart[self.item_name]
                del self.shopping_cart[self.item_name]

                # Menampilkan pesan sukses
                print('Harga produk berhasil diperbarui')
                print('---------------------------------------------------------')
                break

            # Menampilkan peringatan dan instruksi jika input salah
            print('Item tersebut tidak terdapat di keranjang belanja!')
            print('Silahkan Ulangi Kembali')
            print('---------------------------------------------------------')

    def update_item_quantity(self):
        '''
        Metode untuk memperbarui jumlah barang di keranjang belanja
        
         Parameter:
             item_name (str): Nama produk yang kuantitasnya perlu diubah
             new_quantity (str): Jumlah produk baru
        '''
        # While loop untuk membiarkan pengguna mencoba lagi jika inputnya salah
        while True:
            # Input item name
            self.item_name = input('Nama Produk: ').capitalize()
            # Indikator untuk mengecek apakah nama item sudah masuk
            # keranjang belanja atau tidak
            is_in_cart = self.item_name in self.shopping_cart.keys()

            # Bersyarat untuk mengubah jumlah item kemudian memutus putaran
            # jika indikatornya Benar
            if is_in_cart == True:
                # Masukkan jumlah barang baru
                self.new_quantity = int(input('Kuantitas produk yang diupdate '))
                self.shopping_cart[self.item_name][0] = self.new_quantity

                # Menampilkan pesan sukses
                print('Harga produk berhasil diperbarui')
                print('---------------------------------------------------------')
                break
            
            # Menampilkan peringatan dan instruksi jika input salah
            print('Item tersebut tidak terdapat di keranjang belanja!')
            print('Silahkan Ulangi Kembali')
            print('---------------------------------------------------------')

    def update_item_price(self):
        '''
        Metode untuk memperbarui harga barang di keranjang belanja
        
       Parameter:
             item_name (str): Nama produk yang kuantitasnya perlu diubah
             new_price (int): Harga baru produk tersebut
        '''
        # While loop untuk membiarkan pengguna mencoba lagi jika inputnya salah
        while True:
            # Input item name
            self.item_name = input('Nama Produk: ').capitalize()
            # Indikator untuk mengecek apakah nama item sudah masuk
            # Keranjang belanja atau tidak
            is_in_cart = self.item_name in self.shopping_cart.keys()

            # Bersyarat untuk mengubah harga barang lalu memutus putaran
            # jika indikatornya Benar
            if is_in_cart == True:
                self.new_price = int(input('Harga produk yang akan di update: '))
                self.shopping_cart[self.item_name][1] = self.new_price

                # Menampilkan pesan sukses
                print('Harga produk berhasil diperbarui')
                print('---------------------------------------------------------')
                break

            # Menampilkan peringatan dan instruksi jika input salah
            print('Item tersebut tidak terdapat di keranjang belanja!')
            print('Silahkan Ulangi Kembali')
            print('---------------------------------------------------------')

    def delete_item(self):
        '''
        Metode untuk menghapus produk dari keranjang belanja
        
        Parameters:
            item_name (str): Nama produk yang ingin dihapus
        '''
        # While loop untuk membiarkan pengguna mencoba lagi jika inputnya salah
        while True:
            # Input item name
            self.item_name = input('Nama Produk: ').capitalize()
            # Indikator untuk mengecek apakah nama item sudah masuk
            # keranjang belanja atau tidak
            is_in_cart = self.item_name in self.shopping_cart.keys()

            # Bersyarat untuk menghapus item dari keranjang belanja
            # jika indikatornya True maka hancurkan wcp
            if is_in_cart == True:
                self.shopping_cart.pop(self.item_name)

                # Menampilkan pesan sukses
                print('Produk berhasil dihapus')
                print('---------------------------------------------------------')
                break
            
            # Menampilkan peringatan dan instruksi jika input salah
            print('Produk tersebut tidak terdapat di keranjang belanja!')
            print('Silahkan Ulangi Kembali')
            print('---------------------------------------------------------')

    def reset_transaction(self):
        '''Method untuk menghapus semua daftar produk di keranjang belanjaan'''
        # Hapus semua kunci dan nilai dalam kamus shopping_cart
        self.shopping_cart.clear()

        # Menampilkan success message
        print('Keranjang Belanja Kosong!')
        print('---------------------------------------------------------')
    
    def check_order(self):
        '''Method untuk memeriksa dan menampilkan produk dalam keranjang belanja'''
        # Data for shopping list table
        self.data = [
            ['Nama Produk', 'Kuantitas', 'Harga', 'Total Harga'] # Headers
        ]

        # For loop untuk menambahkan data untuk setiap header
        for key, value in self.shopping_cart.items():
            self.data.append([key, value[0], value[1], value[0]*value[1]])
        
        # Print tabel daftar barang di keranjang belanja
        print(tabulate(self.data, headers="firstrow"))

        # For loop untuk memeriksa kuantitas dan harga item dalam daftar belanja
        for key, value in self.shopping_cart.items():
            if value[0] < 0 or value[1] < 0:
                # Menampilkan peringatan dan instruksi untuk input yang salah
                print(f'Kuantitas Atau Harga dari {key} Terdapat Kesalahan')
                print('Update Jumlah Barang Atau Harga') 
    
    
    def total_price(self):
        '''Fungsi untuk calculate total price'''
        # Initialisasi  total_price variable as 0
        total_price = 0

        # Hitung jumlah harga total setiap barang
        for index in range(1, len(self.data)):
            total_price += self.data[index][3]

        # Kondisi tertentu untuk diskon    
        if total_price > 500_000:
            discount = 0.1 # 10% discount
            total_price -= discount * total_price
            print('Anda Mendapatkan Diskon 10%')
        elif total_price > 300_000: 
            discount = 0.08 # 8% discount
            total_price -= discount * total_price
            print('Anda Mendapatkan Diskon 8%')
        elif total_price > 200_000:
            discount = 0.05 #5% discount
            total_price -= discount * total_price
            print('Anda Mendapatkan Diskon 5%')
        else:
            # Menampilkan daftar diskon jika pengguna
            # tidak mendapatkan diskon
            print('Anda Tidak Mendapatkan Diskon')
            print('''
           Persyaratan Diskon Untuk Belanjaan Anda:
              5%: jika total harga lebih besar dari 200000
              8%: jika total harga lebih besar dari 300000
              10%: jika total harga lebih besar dari 500000
            ''')

        # Menunjukkan total harga setelah diskon (jika ada)
        print(f'Total Harga: Rp.{total_price:,.2f}')