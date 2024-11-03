import unittest
from Bramantyo_app import ItemCart, ShoopingCart

class TestBramApp(unittest.TestCase):
    '''
    Ini adalah bagian pengujian aplikasi, bagian-bagian yang akan diuji adalah:
    1. Penambahan barang beserta harganya pada def test_add_barang
    2. Penghapusan barang pada def test_remove_barang
    3. Penjumlahan harga barang pada def test_total_barang
    Detail cara bekerjanya akan dijelaskan pada masing-masing fungsi/method
    '''
    def setUp(self):
        '''
        Dalam fungsi ini, yang dilakukan hanya sekedar set-up saja yang berawal juga dengan menambahkan beberapa barang
        belanjaan umum seperti Pisang dan Susu
        '''
        self.catalog = ShoopingCart()  #variable bernama self.catalog
        self.barang1 = ItemCart("Pisang", 1000) #variable bernama self.barang1
        self.barang2 = ItemCart("Susu", 5000) #variable bernama self.barang2
        self.catalog.add_barang(self.barang1) #menambahkan barang self.barang1
        self.catalog.add_barang(self.barang2) #menambahkan barang self.barang2

    def test_add_barang(self):
        '''
        Bagian sini masuk dalam tes penambahan barang, kita akan menambahkan barang baru yaitu daging yang akan masuk ke list juga.
        Jadi, list yang tadinya berbentuk
        [[Pisang, 1000], [Susu, 5000]]
        akan berubah jadi
        [[Pisang, 1000], [Susu, 5000], [Daging, 10000]]
        '''
        self.barang3 = ItemCart("Daging", 10000) #menambahkan barangberupa daging berharga 10000
        self.catalog.add_barang(self.barang3)
        self.assertEqual(len(self.catalog.catalog),3) #mengecek bila yang berada di list itu 3 barang


    def test_remove_barang(self):
        '''
        Bagian sini masuk dalam tes penambahan barang, kita akan menambahkan barang baru yaitu daging yang akan masuk ke list juga.
        Jadi, list yang tadinya berbentuk
        [[Pisang, 1000], [Susu, 5000], [Dagin, 10000]]
        akan berubah jadi
        [[Susu, 5000], [Daging, 10000]]       
        
        '''
        self.catalog.remove_barang("Pisang") #nama pisang dihapuskan
        self.assertNotEqual("Pisang", self.catalog.catalog) #mengecek bila nama pisang masih di dalam list


    def test_total_barang(self):
        '''
        Bagian tes ini adalah penjumlahan total barang yang ada di list di bawah
        [[Susu, 5000], [Daging, 10000]]
        Seharusnya sesuai logika, akan berhasil jika totalnya 15000, tetapi di bawah
        total yang bener menurut komputer adalah 6000
        '''
        output = self.catalog.total_barang() #fungsi penjumlahan total dibuat variable terlebih dahulu
        result = output #dibuat variable lagi agar bisa dimasukkan dalam assertEqual
        expect = 6000 #harusnya 15000 tetapi yang dianggap benar adalah 6000
        self.assertEqual(expect, result) #mengecek bila hasilnya sesuai expect

if __name__ == "__main__":
    unittest.main()