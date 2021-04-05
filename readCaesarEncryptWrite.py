import string
hKecil = string.ascii_lowercase
hBesar = string.ascii_uppercase

# Penjelasan singkat:
# Mengasumsikan bahwa pergeseran enkripsi Caesar adalah dengan nilai kunci positif...
# Dekripsi enkripsi Caesar pada fungsi ini adalah dengan melakukan pergeseran dengan nilai kunci negatif 

def dekripsiCaesar():
    pathEnkripsi = input("Input path ke file yang dienkripsi: ") #(1) menerima input file dari teks (.txt)
    fileEnkripsi = open(pathEnkripsi, 'r')
    kunci = int(input("Input kunci enkripsi: ")) #(3) menerima input keyboard untuk memasukkan Kunci Chipernya
    dekripsi = ""
    enkripsi = fileEnkripsi.read()
    for karakter in range(len(enkripsi)): #(2) memproses input untuk di-decrypt menggunakan Algoritma Caesar
        if enkripsi[karakter].islower():
            dekripsi += hKecil[(hKecil.index(enkripsi[karakter]) - kunci) % len(hKecil)]
        elif enkripsi[karakter].isupper():
            dekripsi += hBesar[(hBesar.index(enkripsi[karakter]) - kunci) % len(hBesar)]
        else:
            dekripsi += (enkripsi[karakter])
    fileDekripsi = open('D:\output.txt', 'w')
    fileDekripsi.write(dekripsi) #(4) menghasilkan output file teks (.txt) hasil decrypt
    fileEnkripsi.close()
    fileDekripsi.close()

dekripsiCaesar() 










