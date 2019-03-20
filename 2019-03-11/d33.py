from d32 import Kedi
melek=Kedi(tuy="Kısa",kulak="Dik",goz="Yesil",ad="Melek")
melek.miyavla()
melek.beslenme()
duman=Kedi(tuy="Kısa",kulak="Yatık",goz="Mavi",ad="Duman")
duman.miyavla()
pamuk=Kedi(tuy="Uzun",kulak="Yatık",goz="Farklı",ad="Pamuk")
print(duman.tip)
duman.tip="Scottish"
print(duman.tip)
print(melek.tip)