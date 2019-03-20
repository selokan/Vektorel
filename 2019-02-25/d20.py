# def isim(adi="",soyadi=""):
#     print("Merhaba",adi,soyadi)
# isim(input("Adı:"),input("Soyadı:"))

def tip(*args):
    sayim=0
    for item in args:
        if str(type(item)) == "<class 'str'>":
            sayim+=1
    print("Bu parametre de {} kadar str deger vardır".format(sayim))

tip(1,2,3,"deneme",["deneme",2.3],2.3)


def yazdir()