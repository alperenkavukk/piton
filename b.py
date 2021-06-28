oran=0
sayac1=0
sayac2=0
sayac3=0
a=1
while a==1:
   ilkod=input("il kodu giriniz")
   ilnüfüs=int(input("nufusu giriniz"))
   kapasite=int(input("kaç kişi alır"))
   metrekare=int(input("kaç metrekare"))
   if(metrekare>=100 and metrekare<=200):
       oran=ilnüfüs/kapasite
       kapasitetürü="2N";
       print("kapisite türü 2N oran",oran)
       sayac1+=1

   elif(metrekare>200 and metrekare<=300):
       oran = ilnüfüs / kapasite
       kapasitetürü="3N";
       print("kapisite türü 3N oran", oran)
       sayac2+=1

   elif(metrekare > 300 and metrekare <= 500):
       oran = ilnüfüs / kapasite
       kapasitetürü="5N";
       print("kapisite türü 5N oran", oran)
      sayac3+=1
   kontrol=int(input("tekrar market girişi için 1'e çıkmak için 0"))

   if(kontrol==0):
       a= 3
       print("2N türü ", sayac1  ,"\n 3N türü ",sayac2,"\n 5N türü ",sayac3)
 
