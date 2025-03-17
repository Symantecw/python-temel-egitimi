import math

def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y == 0:
        return "Hata: Sıfıra bölme hatası!"
    return x / y

def us_al(x, y):
    return x ** y

def karekok(x):
    if x < 0:
        return "Hata: Negatif sayının karekökü alınamaz!"
    return math.sqrt(x)

def faktoriyel(x):
    if x < 0:
        return "Hata: Negatif sayının faktöriyeli alınamaz!"
    return math.factorial(int(x))

def mod_al(x, y):
    return x % y

def hesap_makinesi():
    while True:
        print("\nPython Profesyonel Hesap Makinesi")
        print("İşlemler:")
        print("1 - Toplama")
        print("2 - Çıkarma")
        print("3 - Çarpma")
        print("4 - Bölme")
        print("5 - Üs Alma")
        print("6 - Karekök")
        print("7 - Faktöriyel")
        print("8 - Mod Alma")
        print("9 - Çıkış")

        secim = input("İşlem numarasını seçin (1/2/3/4/5/6/7/8/9): ")

        if secim == '9':
            print("Hesap makinesi kapatılıyor...")
            break

        try:
            if secim in ['1', '2', '3', '4', '5', '8']:
                sayi1 = float(input("Birinci sayıyı girin: "))
                sayi2 = float(input("İkinci sayıyı girin: "))

                if secim == '1':
                    print(f"Sonuç: {sayi1} + {sayi2} = {topla(sayi1, sayi2)}")
                elif secim == '2':
                    print(f"Sonuç: {sayi1} - {sayi2} = {cikar(sayi1, sayi2)}")
                elif secim == '3':
                    print(f"Sonuç: {sayi1} * {sayi2} = {carp(sayi1, sayi2)}")
                elif secim == '4':
                    print(f"Sonuç: {sayi1} / {sayi2} = {bol(sayi1, sayi2)}")
                elif secim == '5':
                    print(f"Sonuç: {sayi1} ^ {sayi2} = {us_al(sayi1, sayi2)}")
                elif secim == '8':
                    print(f"Sonuç: {sayi1} % {sayi2} = {mod_al(sayi1, sayi2)}")

            elif secim in ['6', '7']:
                sayi = float(input("Sayıyı girin: "))

                if secim == '6':
                    print(f"Sonuç: √{sayi} = {karekok(sayi)}")
                elif secim == '7':
                    print(f"Sonuç: {sayi}! = {faktoriyel(sayi)}")

            else:
                print("Geçersiz seçim! Lütfen 1-9 arasında bir numara girin.")

        except ValueError:
            print("Hata: Geçersiz giriş! Lütfen sayı girin.")
        except Exception as e:
            print(f"Hata: {e}")

# Hesap makinesini çalıştır
hesap_makinesi()
