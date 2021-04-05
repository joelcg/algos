import string
hKecil=string.ascii_lowercase
hBesar=string.ascii_uppercase

def enkripsiCaesar(pesan, kunci):
    enkripsi=''
    for karakter in range(len(pesan)):
        if pesan[karakter].islower():
            enkripsi+=hKecil[(hKecil.index(pesan[karakter])+kunci)%26]
        elif pesan[karakter].isupper():
            enkripsi+=hBesar[(hBesar.index(pesan[karakter])+kunci)%26]
        else:
            enkripsi+=(pesan[karakter])
    return enkripsi

def dekripsiCaesar(enkripsi, kunci):
    dekripsi=''
    for karakter in range(len(enkripsi)):
        if enkripsi[karakter].islower():
            dekripsi+=hKecil[(hKecil.index(enkripsi[karakter])-kunci)%26]
        elif enkripsi[karakter].isupper():
            dekripsi+=hBesar[(hBesar.index(enkripsi[karakter])-kunci)%26]
        else:
            dekripsi+=(enkripsi[karakter])
    return dekripsi

def kriptografiCaesar():
    inputPesan=input('Pesan yang ingin dienkripsi: ')
    inputKunci=int(input('Kunci enkripsi: '))
    pesanDienkripsi=enkripsiCaesar(inputPesan, inputKunci)
    print('Hasil enkripsi pesan: ', pesanDienkripsi)
    pesanDidekripsi=dekripsiCaesar(pesanDienkripsi, inputKunci)
    print('Hasil dekripsi pesan: ', pesanDidekripsi)  