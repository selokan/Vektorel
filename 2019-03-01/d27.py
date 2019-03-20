fonk_1=lambda a,b:a*b
fonk=lambda a,b:a+b+fonk_1(a,b)
print(fonk(2,4))