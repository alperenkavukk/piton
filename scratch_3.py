print("Yemekhane Sistemine Hoşgeldiniz!")
yemeklistesi=[];yemeksozlugu={}
gun="";anayemek="";arasicak="";Corba="";SalataveyaTatli="";aranilanyemek=""
while(True):
   secim=int(input("seçiminizi yapınız"))
   if 1 == secim:
       gun=input("Gün Adını Giriniz")
       anayemek=input("Ana Yemeği Giriniz")
       yemeklistesi.append(anayemek)
       arasicak=input("AraSıcak Yemeği Giriniz")
       Corba=input("Çorba Adını Yazınız")
       SalataveyaTatli=input("Salata veya Tatlıyı Yazınız")

       yemeksozlugu.setdefault(gun, yemeklistesi)
   elif 2== secim:
       sayac = 0
       aranilanyemek = input("Aradığınız Yemeği Giriniz")
       yemeksozlugu.setdefault(gun, yemeklistesi)
       for i in yemeklistesi:
           if (aranilanyemek):
               sayac += 1
               yazi1 = "{} yemeği {} defa yenilmiştir."
               print(yazi1.format(aranilanyemek, sayac))
           else:
                break; 

