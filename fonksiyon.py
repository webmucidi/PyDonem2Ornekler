import random

sayi=random.randint(1,100)


def oyna(rakam):

    if sayi>int(rakam):
        print("Daha BÜYÜK bir sayı girin!")
        return
    elif sayi<int(rakam):
        print("Daha KÜÇÜK bir sayı girin!")
        return 
    else:
        print("Tebrikler")
        exit()
        
def cagir():
    rakam=input("0-100 arasında bir sayı giriniz: ")
    oyna(rakam)
    cagir()

cagir()

