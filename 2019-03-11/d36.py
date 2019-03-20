try:
    dosya=open(r"D:\SelimBozdogan\teneme.txt","r+")
    dosya.read()
    dosya.write("\nSen konusma soner")
except FileNotFoundError:
    dosya=open(r"D:\SelimBozdogan\teneme.txt","w")
finally:
    dosya.close()
input()

# print(dosya.read())
# print(dosya.tell())
# print(dosya.read())
# dosya.seek(0)
# print(dosya.readline())
# print(dosya.readline())
# dosya.seek(0)
# print(dosya.readlines())