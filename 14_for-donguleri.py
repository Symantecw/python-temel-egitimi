sayilar = [1, 2, 3, 4, 5]

for eleman in sayilar:
    print(eleman)

i = 0

while i < len(sayilar):
    print(sayilar[i])
    i += 1

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Array-Diziler

dizi=[1,2,3,4,5]
# print(type(dizi))

# print(dizi[0])
# print(dizi[0:])

#For Döngüsü
# print(len(dizi))

# for sayı in range(len(dizi)):
#     print(dizi[sayı])

#While
i=0
degisken=True
while degisken:
    i=i+1
    if i>8:
        #break
        degisken=False
    if i%2==1:
        continue
    print(i)
