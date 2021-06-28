sayac=0
ücret=0
while sayac==0:
   yaş=int(input("yaş giriniz"))
   if yaş>1 and yaş<4:
       süre=int(input("süre giriniz"))
       veli=input("veli var mı")
       if veli== "evet":
            if süre>0 and süre<20:
                ücret+55
                ücret+=70
            elif süre>30 and süre<60:
                ücret+65
            elif süre>=60:
                print("tekrar süre gir")
    else:
    if yaş<10 and yaş>5:
       süre=int(input("süre giriniz"))
       if süre > 0 and süre < 20:
                    ücret + 50
       elif süre > 20 and süre < 30:
          ücret += 65
       elif süre > 30 and süre < 60:
           ücret += 80
       elif süre>=60:
                print("tekrar süre gir")
    if yaş < 15 and yaş > 10:
       süre = int(input("süre giriniz"))
        if süre > 0 and süre < 20:
           ücret + 50
        elif süre > 20 and süre < 30:
           ücret += 65
        elif süre > 30 and süre < 60:
           ücret += 80
        elif süre>=60:
             print("tekrar süre gir")

        elif yaş>14:
            continue
    çıkış=input("çıkış yapılacak mı")
    if çıkış=="evet":
        sayac=2
        print("toplam ücret",ücret)