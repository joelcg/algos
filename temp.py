#collection of code and instruction
#
#void function (non-fruitful) atau tidak memiliki nilai balik atau return
#def namafungsi():
#    print("ini kalimat dalam fungsi")
#
#fungsi dengan return value
#luas persegi, Lp = sisi * sisi
#def persegi(s):
#    Lp=s*s
#    return Lp
#print(persegi(10))
#
#fungsi dengan dua parameter atau lebih
#luas persegi panjang, Lpp = panjang * lebar
#def persegipanjang(panjang,lebar):
#    Lpp=panjang*lebar
#    return Lpp
#inputPanjang=int(input("input panjang = "))
#inputLebar=int(input("input lebar= "))
#Hasil=persegipanjang(inputPanjang,inputLebar)
#print("Luas persegi panjang adalah " + str(Hasil))

#latihan minggu 8
# def openmbox():
#     datFile=open('D:\mbox.txt')
#     for x in datFile:
#         print(x)

# def countmbox():
#     datFile=open('D:\mbox.txt')
#     count=0
#     for x in datFile:
#         count=count+1
#     print(count)
    
# def stringLenmbox():
#     datFile=open('D:\mbox.txt')
#     datRead=datFile.read()
#     panjangString=len(datRead)
#     print(panjangString)
    
# def stringReadmbox():
#     datFile=open('D:\mbox.txt')
#     datRead=datFile.read()
#     print(datRead[:50]) #output=From stephen.marquard@uct.ac.za Sat Jan  5 09:14:1

# def findmbox():
#     datFile=open('D:\mbox.txt')
#     count=0
#     for line in datFile:
#         if line.startswith('From:'):
#             print(line)
#             count=count+1
#     print(count)
    
# def findmboxwithrstrip():
#     datFile=open('D:\mbox.txt')
#     count=0
#     for line in datFile:
#         line=line.rstrip()
#         if line.startswith('From:'):
#             print(line)
#             count=count+1
#     print(count)
    
# def openfile():
#     inputFile=input('Masukan nama file:')
#     datFile=open(inputFile)
#     for x in datFile:
#         print(x)

# def openfileerrormitigation():
#     inputFile=input('Masukan path file: ')
#     try:
#         datFile=open(inputFile)
#         for x in datFile:
#             print(x)
#     except:
#         print("Error, file "+inputFile+" tidak ada")
#         quit
    
# def writeFile():
#     inputFileHandler=input('Masukan path file: ')
#     try:
#         fileHandler=open(inputFileHandler)
#         readFile=fileHandler.read()
#         readFile200=readFile[0:200]
#         inputWriteFile=input('Masukan path file: ')
#         try:
#             writeFile=open(inputWriteFile, "w")
#             writeFile.write(readFile200)    
#             writeFile.close()
#         except:
#             print("Error, file "+inputFileHandler+" tidak ada")
#             quit()
#     except:
#         print("Error, file "+inputFileHandler+" tidak ada")
#         quit()

# latihan sandi caesar
# alfabet="abcdefghijklmnopqrstuvwxyz"

# def caesarCypher(pesan, kunci):
#      enkripsi=''
#      for huruf in pesan:
#          enkripsi+=alfabet[(alfabet.index(huruf)+kunci)%(len(alfabet))]
#      return enkripsi

# def caesarDecypher(enkripsi, kunci):
#     dekripsi=''
#     for huruf in enkripsi:
#         dekripsi+=alfabet[(alfabet.index(huruf)-kunci)%(len(alfabet))]
#     return dekripsi

# def enkripsikan():
#     pesan=input('Pesan yang dienkripsi: ')
#     kunci=int(input('Kunci enkripsi: '))
#     pesanTerenkripsi=caesarCypher(pesan, kunci)
#     pesanDidekripsi=caesarDecypher(pesanTerenkripsi, kunci)
#     print('Hasil enkripsi pesan: ',pesanTerenkripsi)
#     print('Hasil dekripsi pesan: ', pesanDidekripsi)  

# def enkripsiCaesar(pesan, kunci): 
#     enkripsi=''
#     for karakter in pesan: 
#         if karakter.islower():
#             enkripsi=enkripsi+chr((ord(karakter)+kunci-97)%26+97)
#         elif karakter.isupper():
#             enkripsi=enkripsi+chr((ord(karakter)+kunci-65)%26+65)
#         else:
#             enkripsi=enkripsi+karakter
#     return enkripsi

# def dekripsiCaesar(enkripsi, kunci):
#     dekripsi=''
#     for karakter in enkripsi: 
#         if karakter.islower():
#             dekripsi=dekripsi+chr((ord(karakter)-kunci-97)%26+97)
#         elif karakter.isupper():
#             dekripsi=dekripsi+chr((ord(karakter)-kunci-65)%26+65)
#         else:
#             dekripsi=dekripsi+karakter
#     return dekripsi
    

# def enkripsikan():
#     inputPesan=input('Pesan yang ingin dienkripsi: ')
#     inputKunci=int(input('Kunci enkripsi: '))
#     pesanTerenkripsi=enkripsiCaesar(inputPesan, inputKunci)
#     print('Hasil enkripsi pesan: ', pesanTerenkripsi)
#     pesanDidekripsi=dekripsiCaesar(pesanTerenkripsi, inputKunci)
#     print('Hasil dekripsi pesan: ', pesanDidekripsi)    

# import string
# def enkripsiCaesarSingkat(pesan, kunci):
#     enkripsi=''
#     for karakter in pesan:
#         if karakter in string.ascii_letters:
#             enkripsi+=chr(ord(karakter)-kunci)
#         else:
#             enkripsi+=karakter
#     return enkripsi

#versi wip
# huruf=string.ascii_letters
# def enkripsiCaesarSingkat(pesan, kunci):
#     enkripsi=''
#     for karakter in range(len(pesan)):
#         if pesan[karakter] in string.ascii_letters:
#             enkripsi+=huruf[(huruf.index(pesan[karakter])+kunci)%26]
#         else:
#             enkripsi+=(pesan[karakter])
#     return enkrips

# def cal1(a,b=20):
#     print(a,b)
# for num in range(-2, -5, -1):
#     print(num, end=", ")
# print(36/4*(3+2)*4+2)
# asd = "sdasd asd"
# print(asd[2::-1])
# print(5**2,5**3)
# print(type(0XFF))
# print("Emma"<"Emm")
# def abc1():
#     for num in range(10, 14):
#         for i in range (2, num):
#             if num%1 == 1:
#                 print(num)
#                 break
# print(36/4)
# ab, bc=12, 5
# if ab+bc:
#     print('t')
# else:
#     print('f')
# print('Welcome'[:6] + 'Pynative')
# def abc():
#     row= 5
#     num= 0
#     while row<num:
#         star = row+1
#         while star>0:
#             print("*", end=" ")
#             star-=1
#         row+=1
#         print()
# x,c,v=1,2,3
# print(x,c,v)
# x = 7
# # for num in range(0.5, 5.5, 0.5):
# #     print(num)
# list1=[10,20]
# list2=[10,20]
# print(list1 is list2)
# az=0
# while (az<100):
#     az+=2
# print(az)
# print(2*3**3*4)
# print(6**2,6//2)
# print(2**3**2)
# print(type({})is set)
# for num in range(10,14):
#     for i in range(2,num):
#         if num%i==1:
#             print(num)
#             break
# # sample={"a","b","c"}
# # sample.add(1, "z")
# # print(sample)
# print("James Bond"[2::-1])
# goreng=7
# for e in range (goreng,0,-1):
#     print((goreng+1)*''+e*'*')
# for num in range(10, 15, 1):
#     print(num, end=", ")
# bara=10
# api=50
# if(bara**2>100 and api<100):
#     print(bara,api)
# num=5
# row=0
# while row<num:
#     star=row+1
#     while star>0:
#         print(("*"), end=" ")
#         star-=1
#     row+=1
#     print()
# print(bool(0))
# print(bool(-3))
# print(str("string"))
# def add(a,b):
#     return a+5,b+5
# result=add(3,2)
# print(result)
# def outerFun(a,b):
#     def innerfun(c,d):
#         return c+d
#     return innerfun(a,b)
# ayamgoreng=outerFun(5, 10)
# print(ayamgoreng)
x=7
for e in range (x,0,-1):
    print((x-e)*' '+e*'*')
    
    
    
    
    
    
    
    
    
    