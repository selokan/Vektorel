def dosyaAc(dosyaYolu):
    import os
    dosya = None
    if os.path.exists(dosyaYolu):
            dosya = open(dosyaYolu,"r+")
    else:
            dosya = open(dosyaYolu,"w+")
    return dosya

def KayitAlma(dosyaYolu):
    import os 
    try:
        dosya = dosyaAc(dosyaYolu)
        dosya.read()
        Adi = input("Adını Giriniz")
        Soyadi = input("Soyadı Giriniz")
        Telefon = input("Telefon")
        kayit = Adi + ";" + Soyadi + ";" + Telefon + "\n"
        dosya.write(kayit)
    except:
        print("Hata Var ")
    finally:
        dosya.close()

def Listeleme(dosyaYolu):
    import os 
    try:
        dosya = dosyaAc(dosyaYolu)
        liste = dosya.readlines()
        print("-"*20)
        for i in liste:
            print(liste.index(i)+1,i,sep="-")
        print("-"*20)
    except:
        print("Hata Var ")
    finally:
        dosya.close()

def Duzeltme(dosyaYolu):
    import os 
    try:
        dosya = dosyaAc(dosyaYolu)
        liste = dosya.readlines()
        print("-"*20)
        for i in liste:
            print(liste.index(i)+1,i,sep="-")
        print("-"*20)
        kayit = int(input("Duzeltmek İstediğiniz Kaydı Seçiniz"))
        Adi = input("Adını Giriniz")
        Soyadi = input("Soyadı Giriniz")
        Telefon = input("Telefon")
        liste[kayit-1] = Adi + ";" + Soyadi + ";" + Telefon + "\n"
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    except:
        print("Hata Var ")
    finally:
        dosya.close()

def Silme(dosyaYolu):
    import os 
    try:
        dosya = dosyaAc(dosyaYolu)
        liste = dosya.readlines()
        print("-"*20)
        kayit = int(input("Silmek İstediğiniz Kaydı Seçiniz"))
        liste.pop(kayit-1)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    except:
        print("Hata Var ")
    finally:
        dosya.close()
anahtar = 1
while anahtar == 1:
    dosyaYolu = r"D:\defter.txt"
    print("1-Listeleme","2-KayıtAlma","3-Düzeltme","4-Silme","5-Çıkış",sep="\n")
    giris =  input("Yapmak İstediğiniz İşlemi Seçiniz")
    if giris== "1":
        Listeleme(dosyaYolu)
    elif giris == "2":
        KayitAlma(dosyaYolu)
    elif giris == "3":
        Duzeltme(dosyaYolu)
    elif giris == "4":
        Silme(dosyaYolu)
    elif giris == "5":
        print("Çıkılıyor")
        anahtar = 0







