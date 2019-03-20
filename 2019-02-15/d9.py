# liste=[1,1.1,1.1j,"str",("--",1),{"a":"A"},[1,2,3,4]]
# # print(liste[6][1])
# # print(liste[4][1])
# # print(liste[5]["a"])
# # print(liste)

liste=[1,2,3,4,5]
# liste2=liste
liste2=liste.copy()
liste2[1]=8
print(liste)

print(id(liste))
print(id(liste2))

# aynı olacaklar cunku birbirleriyle aynı oldular


