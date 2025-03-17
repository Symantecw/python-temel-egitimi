#Fonksiyonlar 

#String
# def merhaba(x):
#     print(x)

# merhaba("Hello World")

#Integer
# def toplama(sayı1,sayı2):
#     toplam=sayı1+sayı2
#     print(toplam)

# toplama(5,3)

#Return
# def toplama(sayı1,sayı2):
#     toplam=sayı1+sayı2
#     return toplam

# sonuc=toplama(5,3)
# print(sonuc)


#*args
# def ulkeler(*x):
#     return x

# sonuc=ulkeler("Almanya","Arjantin","Türkiye")
# print(sonuc)

#Fonksiyonları İç içe kullanma

def toplam(x,y):
    return x+y

def toplam2(a):
    return a+toplam

toplam=toplam(5,3)
print(toplam2(4))

#String ve Integer Kullanma

def isim_yas(isim,yas):
    print("Kullanıcı adı: "+isim+" ve yaşınız: ",yas+5)

isim_yas("Eray",15)
