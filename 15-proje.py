def hesapla(odev,lab,vize,final):
    sonuc=((odev*15)+(lab*15)+(vize*30)+(final*40))/100
    return sonuc
def harfler(odev,lab,vize,final):
    ortalama=hesapla(odev,lab,vize,final)
    if 100>=ortalama>=90:
        print("Notunuz AA")
    if 90>ortalama>=80:
        print("Notunuz BA")
    if 80>ortalama>=70:
        print("Notunuz BB")
    if 70>ortalama>=60:
        print("Notunuz BC")
    if 60>ortalama>=50:
        print("Notunuz CC")
    if 50>ortalama>=40:
        print("Notunuz DC")
    if 40>ortalama:
        print("Notunuz DD")
    print("Ortalama: ",ortalama)    

kosul=1

while kosul:
    odev=int(input("Ödev Puanınızı giriniz: "))
    lab=int(input("Lab Puanınızı giriniz: "))
    vize=int(input("Vize Puanınızı giriniz: "))
    final=int(input("Final Puanınızı giriniz: "))

    if 100>=(odev or lab or vize or final)>=0:
        harfler(odev,lab,vize,final)
    else:
        print("Notlar 100 den büyük ve 0 dan küçük olamaz diyelim")
    while True:    
        devam=int(input("Programı bitirmek istiyorsanız 0 yazın. Değilse 1 yazın: "))

        if devam==0:
            kosul=0
            break
        elif devam==1:
            break
        else:
            print("Hatalı bir değer girdiniz. Lütfen tekrar girin")
