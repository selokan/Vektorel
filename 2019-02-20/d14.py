# liste=[3,4,5,6,110,234,54,123]
# for item in liste
#     print(item)

import random
sayi=random.randint(1,49)
print(sayi)
sozluk={1:"birinci",2:"ikinci",3:"üçüncü",4:"üncü",5:""}
for i in range(1,11):
    girilen=int(input("Hangi Sayı:"))
    if girilen:
        girilen=int(girilen)
        if sayi<girilen:
            print("Aşağı kalan hak {}".format(str(10-i)))
        elif sayi>girilen:
            print("Yukarı kalan hak {}".format(str(10-i)))
        elif sayi==girilen:
            print("Tebrikler {} hakta sayıyı buldun".format(i))
            break
if sayi != girilen:
        print("Oyunu Kaybettin")
