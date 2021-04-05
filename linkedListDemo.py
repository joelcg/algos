class node: 
    def __init__(self, data=None):
        self.data = data
        self.lanjut = None
  
class linkedList:
    def __init__(self): # fungsi untuk memanggil diri sendiri
        self.head = node()
        
    def masuk(self, data): # fungsi untuk memasukan suatu input(data) ke linkedlist
        sekarang = self.head
        nodeBaru = node(data)
        while sekarang.lanjut != None:
            sekarang = sekarang.lanjut
        sekarang.lanjut = nodeBaru
        
    def panjang(self): # fungsi untuk menampilkan panjang total node
        total = 0
        sekarang = self.head
        while sekarang.lanjut != None:
            total += 1
            sekarang = sekarang.lanjut
        return total
    
    def tampilan(self): # fungsi untuk menampilkan gambaran linked list
        tampak = []
        nodeSekarang = self.head
        while nodeSekarang.lanjut != None:
            nodeSekarang = nodeSekarang.lanjut
            tampak.append(nodeSekarang.data)
        print(tampak)
    
    def get(self, index): # fungsi memanggil data dari suatu posisi pada index
        if index >= self.panjang() or index < 0: # mekanisme agar program dapat gagal secara aman
            print("ERROR: Posisi tersebut di luar dari batasan")
            return None
        indexSekarang = 0
        nodeSekarang = self.head
        while True:
            nodeSekarang = nodeSekarang.lanjut
            if indexSekarang == index:
                return print(nodeSekarang.data)
            indexSekarang += 1
        
    def hapus(self, index): # fungsi menghapus data dari suatu titik index
        if index >= self.panjang() or index < 0:
            print("ERROR: Posisi tersebut di luar dari batasan")
            return None
        indexSekarang = 0
        nodeSekarang = self.head
        while True:
            nodeTerakhir = nodeSekarang
            nodeSekarang = nodeSekarang.lanjut
            if indexSekarang == index:
                nodeTerakhir.lanjut = nodeSekarang.lanjut
                return
            indexSekarang += 1
        
    def __getitem__(self, index):
        return self.get(index)
        
produk = linkedList()
produk.tampilan()
produk.masuk(1)
produk.masuk(2)
produk.masuk(3)
produk.masuk(4)
produk.tampilan()
produk.hapus(1)
produk.tampilan()
produk.get(1)