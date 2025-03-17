yas = int(input("yaşınızı giriniz:"))
if yas > 21:
    print("askere geç kaldınız")
elif yas == 20:
    print("askere gitmelisin")
else:
    print("daha zaman var")


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#Koşullar

#If

# if 5>3: print("Doğru")


#Else


# if 5>6:
#     print("Doğru")
# else:
#     print("Yanlış")

#Else If


# if 5>8:
#     print("Doğru")

# elif 10<1:
#     print("Üstteki yanlış")

# else:
#     print("Her ikisi de yanlış")

#Tek Satırda Yazmak

# yas=17

# durum="Oy Kullanabilir" if yas>=18 else "Oy Kullanamaz"
# print(durum)


#Ve/Veya Kullanımı 

#Ve(And)
# if 5>3 and True:
#     print("Doğru")

# if 5>2 and 9<8:
#     print("Doğru 2")

#Veya(Or)

if 5>10 or 11<3:
    print("Doğru Değer 2")

if False or 10>5:
    print("Doğru Değer")     

else:
    print("Yukarıdaki Yanlış")
