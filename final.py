class sirket():
    gonderileren_adet_koli=0
    urun_ad=""
    urun_tipi=""
    gondericiad=""
    yil=0
    aliciad=""
    aliciadres=""
    def __init__(self,gonderilen_adet_koli,urun_ad,urun_tipi,gondericiad,yil,aliciad,aliciadres):
        self.gonderileren_adet_koli=gonderilen_adet_koli
        self.urun_ad=urun_ad
        self.urun_tipi=urun_tipi
        self.gondericiad=gondericiad
        self.yil=yil
        self.aliciad=aliciad
        self.aliciadres=aliciadres
urun=sirket("1200","tostmakinesi","elektronik","ahmet","2021","alperen","caycuma/ZONGULDAK")