class Uye:
    def __init__(self,eposta, parola):
        self.eposta = eposta
        self.parola = parola

uye1 = Uye("fatihcelik@icloud.com", "fatih123")
uye2 = Uye("ahmetdemir@icloud.com", "ironman123")
uye3 = Uye("aysebakir@icloud.com", "prenses123")
uye4 = Uye("mustafasari@icloud.com", "sari123")
uye5 = Uye("bedirhanSapkali@icloud.com", "kel123")

print()

girilenEPosta = input("Lütfen E-Posta adresinizi giriniz...")
if ((girilenEPosta == uye1.eposta) or (girilenEPosta == uye2.eposta) or (girilenEPosta == uye3.eposta)):
    girilenParola = input("Lütfen parolanızı giriniz...")
    if (girilenParola == uye1.parola):
        print("Giriş başarılı!")
    else:
        print("Girdiğiniz parola yanlış!")
else:
  print("Girdiğiniz E-Posta adresi yanlış...")