'''
=========================================
Graded Challenge 1

Name: Bramantyo Anandaru Suyadi
Batch: HCK 023 FTDS

Program ini untuk pembuatan menu belanja
=========================================
'''


print("""
      
Selamat Datang di Keranjang Belanja Toko Makmur!
Menu:
1. Menambah Barang
2. Menghapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit


""")


class ItemCart:
    #class untuk barang di cart
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        #fungsi untuk identifikasi barang-barang yang ada di kart

class ShoopingCart:
    #berisi fungsi/method yang berguna jika di tes user berupa:
    # penambahan barang, penghapusan barang, display barang, dan perhitungan total barang
    def __init__(self):
        '''
        belum ada method, lebih ke fungsi untuk storage barang/items yang akan diinput user
        '''
        self.catalog = [] #Barang/items yang distore akan berbentuk list
    
    def add_barang(self,barang):
        '''
        User akan mengetik barang dan akan distorkan di list self.catalog
        sehingga self.catalog akan menghasilkan [[brang1, harga1], [barang2, harga2]], 
        di fungsi display_barang nanti di bawah akan mencetak dalam bentuk
        barang1 -> Rp 0000
        barang2 -> RP 1000
        '''
        self.catalog.append(barang) #append() adalah fungsi untuk menaruh inputtan di catalog
        print(f"'{barang.nama}' ditambah dengan harga '{barang.harga}'") 
        #fungsi f ditaruh supaya atribut barang.nama dan barang.harga tidak termakkan oleh string di dalam print
        

    def remove_barang(self, barang_nama):
        '''
        User akan mengetik barang yang akan dihapus jika berada di list self.katalog
        jika nama tersebut (misal: barang1) dihapus, maka list di self.catalog akan berupa
        [barang2, harga2], sehingga pas nanti di display_barang:
        barang2 -> Rp 1000
        '''
        for barang in self.catalog: #memastikkan jika barang ada di keranjang
            if barang.nama == barang_nama:
                self.catalog.remove(barang)
                print(f"'{barang.nama}' dihapuskan dari keranjang")
  
    def display_barang(self):
        '''
        fungsi display yang akan dipakai user nanti jika ingin mendisplay barang-barang di keranjang
        cara kerja secara detailnya sudah dijelaskan di atas, jika user add_barang, barang tersebut akan di store di self.catalog.
        Jika barang di remove, maka akan hilang. Bentukkan display:
        Barang 1 -> Rp000
        '''
        if not self.catalog: #print jika tidak ada apa pun di keranjang
            print("keranjang kosong")
            
         
        else:
            print("isi keranjang:") 
            for barang in self.catalog:
                print (f"{barang.nama} - Rp {barang.harga}")

    def total_barang(self):
       '''
       harga-harga barang yang berada di list nanti akan dijumlahkan untuk menghitung total seluruh harganya
       contoh:
       [[barang1, 4000], [barang2, 5000]]
       sum(barang.harga for barang.nama in self.catalog) -> untuk memastikkan yang dihitung adalah barang.harga 
       untuk setiap barang.nama yang berada di self.catalog
       output:
       9000
       '''
       jumlah = sum(barang.harga for barang in self.catalog)   #Terinspirasi dari excel 
       return jumlah                                           #source ide: https://www.geeksforgeeks.org/sum-function-python/


    def interferance(self):
        '''bagian testing oleh user, jadi akan memperlihatkan bagian print di atas.
        Lalu, ada opsi pilihan yang berisi 1-5
        Jika pilih 1, user akan diminta nama barang yang ingin dia input beserta harganya
        Masukkan barag:   
        Masukkan harga barang:
        *Note: bila yang diinput pada Masukkan harga barang bukan berupa angka, maka akan muncul
        pesan: "Coba lagi, harga salah"
        setelah user selesai menginput, nama barang akan didisplay diikuti pesan "sudah ditambah"
        Jika pilih 2, user akan diminta barang mana yang ingin dia hapus, dan akan diikuti pesan
        nama barang + "sudah dihapus"
        Jika pilih 3, barang yang sudah ditambah tapi belum dihapus akan ditunjukkan sebagaimana
        dijelaskan di bagian def display_barang
        Jika pilih 4, harga barang-barang yang ada di keranjang akan ditambahkan dan akan menunjukkan
        total harga
        Jika pilih 5, maka user akan dikeluarkan diikuti pesan 'Keluar'
        Jika pilihan tidak ada di menu if, akan diikuti pesan "pilihan salah, mohon diulangi lagi :)"
        Jika pilihan bukan merupakan angka, akan diikuti pesan "Silahkan pilih lagi dengan angka"
        '''
        keranjang = ShoopingCart()
        #harus dibikin variable agar lebih dimudahkan pemanggilan method dan fungsi di atas
        while True:
            userpilih = input("pilih menu: ")
            try:
                userpilih = int(userpilih) #memastikkan input awal user berupa integer

                if int(userpilih) == 1: 
                    namaBarang = input('Masukkan barang: ') #Pilihan tambah barang
                    try:
                        hargaBarang = input('Masukkan harga barang: ')
                        hargaBarangFloat = float(hargaBarang)
                        barang = ItemCart(namaBarang, hargaBarangFloat)
                        self.add_barang(barang)
                    except ValueError:
                            print("Coba lagi, harga salah") #ValueError muncul jika yang user masukkan bukan angka
                    
                elif int(userpilih) == 2:
                    namaBarang = input('Masukkan barang yang ingin dihapus: ') #pilihan hapus barang
                    self.remove_barang(namaBarang)

                elif int(userpilih) == 3:
                    self.display_barang() #pilihan display barang

                elif int(userpilih) == 4:
                    totalBelanja = self.total_barang() #pilihan menghitung total harga barang
                    print("Total harga: Rp", totalBelanja)

                elif int(userpilih) == 5:
                    print('Keluar') #pilihan untuk keluar program
                    break
                else:
                    print("pilihan salah, mohon diulangi lagi :)") #Jika yang user masukkan di luar range 1-5

            except ValueError:
                print("Silahkan pilih lagi dengan angka") #ValueError muncul jika yang user masukkan bukan angka


if __name__ == "__main__":
    keranjang = ShoopingCart()
    keranjang.interferance()
            

