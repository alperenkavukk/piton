class Personel():
    mesai = "9 -18"
    sirket = "AS-AS"
    isim=""
    yetenek=""
    mass=0
    gunsayisi=0
    rutbe=""
    def __init__(self,isim,maas,yetenek,rutbe):
        self.isim = isim
        self.yetenek = yetenek
        self.maas = maas
        self.gunsayisi = 0
        self.rutbe = rutbe,

    def calıs(self):
        print(self.isim,"çalışıyor")
        self.gunsayisi+=1

    def terfi(self):
        print("Tebrikler ",self.isim,"Terfi aldın")
        self.maas+=200

    def bilgileriGoster(self):
        print("*-"*20)
        print("Personelin ismi: ",self.isim)
        print("Personelin yetenekleri: ",self.yetenek)
        print("Personelin maaşı: ",self.maas)
        print("Personelin toplam gün sayısı",self.gunsayisi)
        print("Personelin konumu: ",self.rutbe)
        print("*-"*20)