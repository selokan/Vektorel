# Girilen  I.Vize,II.Vize ve Final Notları üzerinden hesaplama yapıp notu ekrana yazdıran programı yazınız.
# Vizelerin %60'ını Finalin %40'ını dikkate almalıdır. 

print("Not Hesaplama Programı")

x=int(input("1.Vize Notu:"))
y=int(input("2.Vize Notu:"))
z=int(input("Final Notu:"))

q=((x*0.3)+(y*0.3))
z=z*0.4
sonuc=(q+z)

print("Ögrencinin Ortalama Notu: {}".format(sonuc))

notu=sonuc
hnote={25:"FF",44:"EE",54:"DD",69:"CC",85:"BB",100:"AA"}
if notu<=25:
    print("Ögrencinin Harf Notu: {}".format(hnote[25]))
elif notu<=44:
    print("Ögrencinin Harf Notu: {}".format(hnote[44]))
elif notu<=54:
    print("Ögrencinin Harf Notu: {}".format(hnote[54]))
elif notu<=69:
    print("Ögrencinin Harf Notu: {}".format(hnote[69]))
elif notu<=85:
    print("Ögrencinin Harf Notu: {}".format(hnote[85]))
elif notu<=100:
    print("Ögrencinin Harf Notu: {}".format(hnote[100]))
else:
    print("Hata")