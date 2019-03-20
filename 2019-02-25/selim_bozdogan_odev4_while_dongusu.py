from random import randint
print ("""***********************************************
Sayısal Loto Numara Programı
***********************************************""")
i=0
kolon = [0,0,0,0,0,0]
for j in kolon:
    while i < len(kolon):
        secilen=randint(0,50)
        if secilen not in kolon:
            kolon[i]=secilen
            i+=1
    print(sorted(kolon))
    i=0
c= input("Yeni Numaralar istiyor musunuz? (Y/N)")
l=0
kolon = [0,0,0,0,0,0]
while c=="y" or c=="Y":
    for k in kolon:
        while l < len(kolon):
            secilen=randint(0,50)
            if secilen not in kolon:
                kolon[l]=secilen
                l+=1
        print(sorted(kolon))
        l=0
    c=input("Yeni Numaralar istiyor musunuz? (Y/N)")
if c=="n" or c=="N":
    print("İyi Şanslar")
