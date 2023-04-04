import random

girilenSayilar=[]
sansliSayilar=[]
eslesenSayilar=[]

tutanSayi=0

def ekle(girilenSayi):
    #En fazla 6 sayı girilmesi için kontrol
    if (len(girilenSayilar))>5:
        print("En fazla 6 sayı seçebilirsiniz!")
        cagir()

    #Girilen sayının 1-49 aralığında olması için kontrol
    if girilenSayi<1 or girilenSayi>50:
        print("1-49 arası sayı seçebilirsiniz!")
        cagir()
    
    #Girilen sayının tekrarlı olmaması için kontrol
    if girilenSayi in girilenSayilar:
        print("Aynı sayıyı tekrar giremezsiniz!")
        cagir()

    girilenSayilar.append(girilenSayi)
    print(girilenSayilar)
    cagir()

def cagir():
    girilenSayi=int(input("1-49 arasında 6 adet sayı giriniz: "))
    ekle(girilenSayi)
cagir()


