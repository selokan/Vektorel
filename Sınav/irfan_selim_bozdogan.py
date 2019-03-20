# Bakiye sorgulama, para çekme, para yatırma ve hesaplar arası para transferi yapılabilen bir bankamatik uygulaması yazınız.
print("""__________________________________________________
Bankamatik Programına Hoşgeldiniz
1- Bakiye Sorgulama
2- Para Yatırma
3- Para Çekme
4- Hesaplarım arası para aktarımı
5- ÇIKIŞ
__________________________________________________""")
i=int(input("Hangi işlemi yapmak istiyorsunuz?:"))
x=1000
y=0
while i<6:
    print("""__________________________________________________
    Bankamatik Programına Hoşgeldiniz
    1- Bakiye Sorgulama
    2- Para Yatırma
    3- Para Çekme
    4- Hesaplarım arası para aktarımı
    5- ÇIKIŞ
    __________________________________________________""")
    if i==1:
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz=", x,"TL")
        print("Hesap 2 Bakiyeniz=", y,"TL")
        j= int(input("Hangi işlemi yapmak istiyorsunuz?:"))
        break
    elif i==2 and j==2:
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz=", x,"TL")
        print("Hesap 2 Bakiyeniz=", y,"TL")
        b=int(input("Hangi hesaba para yatıracaksınız?(1/2):"))
        c=int(input("Yatırmak istediğiniz miktarı giriniz:"))
        if b==1:
            x+=c
            print("."*30)
            print("BAKİYENİZ")
            print("Hesap 1 Bakiyeniz=", x,"TL")
            print("Hesap 2 Bakiyeniz=", y,"TL")
        elif b==2:
            y+=c
            print("."*30)
            print("BAKİYENİZ")
            print("Hesap 1 Bakiyeniz=", x,"TL")
            print("Hesap 2 Bakiyeniz=", y,"TL")
# elif i==3 and j==3:
#         print("BAKİYENİZ")
#         print("Hesap 1 Bakiyeniz=", x,"TL")
#         print("Hesap 2 Bakiyeniz=", y,"TL")
#         d=int(input("Hangi hesaptan para çekeceksiniz?(1/2):"))
#         e=int(input("Çekmek istediğiniz miktarı giriniz:"))
#         if d==1:
#             x-=e
#             print("."*30)
#             print("BAKİYENİZ")
#             print("Hesap 1 Bakiyeniz=", x,"TL")
#             print("Hesap 2 Bakiyeniz=", y,"TL")
#         elif d==2:
#             y-=e
#             print("."*30)
#             print("BAKİYENİZ")
#             print("Hesap 1 Bakiyeniz=", x,"TL")
#             print("Hesap 2 Bakiyeniz=", y,"TL")
#         if e>x:
#             print("YETERSİZ BAKİYE!!!")
#     elif i==5 and j==5:
#         q=input("Çıkmak istediğinize emin misiniz?(E/H)")
#         if q=="e" or q=="E":
#             print("ÇIKIŞ İŞLEMİ YAPILDI...")