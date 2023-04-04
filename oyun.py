import random
rastgeleSayi=random.randint(0,100)
def oyna(girilenSayi):
    if girilenSayi<rastgeleSayi:
        print("Daha BÜYÜK bir sayı giriniz!")
        cagir()
    elif girilenSayi>rastgeleSayi:
        print("Daha KÜÇÜK bir sayı giriniz!")
        cagir()
    else:
        print("TEBRİKLER oyunu kazandınız!")
def cagir():
    girilenSayi=int(input("0-100 arası bir sayı giriniz: "))
    oyna(girilenSayi)
cagir()


