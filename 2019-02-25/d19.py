def oyna(kolon):
    import random
    buyukliste=[]
    for j in range(0,kolon):
        liste=[]
        sayi= random.randint(1,50)
        for i in range(1,7):
            while sayi in liste:
                sayi= random.randint(1,50)
            liste.append(sayi)
        liste.sort()
        buyukliste.append(liste)
    print(*buyukliste,sep="\n")
kolon=int(input("Kolon sayısı giriniz:"))
oyna(kolon)