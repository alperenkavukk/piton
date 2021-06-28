n=int(input("test sayisi giriniz:"))
i=0
sayac=0
if (n<50 and n>0):
    for i in range(n):
       sifre=input("Sifre Giriniz:")
       if (len(sifre))>6 and len(sifre)<20:
            for i in sifre:
              if (sifre.islower()==False) and (sifre.isnumeric()==False) and (sifre.isupper()==False):
                   sayac +=1
                   while sayac==1:
                       print("DOĞRU")
                       break
              else:
                   print("YANLIŞ")
                   break
       else:
                   print("yanlis uzuznluk")
else:
   print("yanlış aralık")