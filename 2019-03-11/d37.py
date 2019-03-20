def dosya_ac(dosya_yolu):
    import os
    try:

import os
try:
    if os.path.exists(r"D:\SelimBozdogan\defter.txt"):
        dosya=open(r"D:\SelimBozdogan\defter.txt","r+")
    else:
        dosya=open(r"D:\SelimBozdogan\defter.txt","w+")
    dosya.read()
    Adi=input("Adinizi giriniz:")
    Soyadi=input("Soyadini giriniz:")
    Telefon=input("Tel no:")
    kayit=Adi+";"+Soyadi+";"+Telefon+"\n"
    dosya.write(kayit)
except:
    print("Hata var")
finally:
    dosya.close()
def listeleme(dosya_yolu):
    import os
    try:
        if os.path.exists(dosya_yolu):
            dosya=open(dosya_yolu,"r+")
        else:
            dosya=open(dosya_yolu,"w+")
        liste=dosya.readlines()
        print("-"*20)
        for i in liste:            
            print(liste.index(i),i,sep="-")
        print("-"*20)
    except:
        print("Hata var")
    finally:
        dosya.close()
anahtar=1
while anahtar==1:
    dosya_yolu="D:\SelimBozdogan\defter.txt"
    print("1-Listeleme","2-Kayit Alma","5-Cikis",sep="\n")
    giris=input("Yapmak istediğiniz islemi seciniz")
    if giris=="1":
        Listeleme(dosya_yolu)
    elif giris=="2":

