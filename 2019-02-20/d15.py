import random
buyukliste=[]
for j in range(0,7):
    liste=[]
    for i in range(1,7):
        liste.append(random.randint(1,50))
        liste.sort()
    buyukliste.append(liste)

print(buyukliste)