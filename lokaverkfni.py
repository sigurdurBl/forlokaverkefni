
class Viðskiptavinur:
    def __init__(self,nafn,heimili,kt,þjoderni,okt,simi,postur):
        self.nafn = nafn
        self.hemili = heimili
        self.kt =kt
        self.þjoderni = þjoderni
        self.okt = okt
        self.simi = simi
        self.postur = postur


class gerdBills:
    def __init__(self,framledari,skranr,tegund,leyfilegurfjoldimanna):
        self.framledari = framledari
        self.skranr = skranr
        self.tegund = tegund
        self.leyfilegurfjoldimanna = leyfilegurfjoldimanna


class bill:
    def __init__(self,skranr,argerd,tegund,framledari,ath):
        self.skranr = skranr
        self.argerd = argerd
        self.tegund = tegund
        self.framledari = framledari
        self.ath = ath


class pantanair:
    def __init__(self,audkenni,vidskiptavinir,pontunardagur,ath):
        self.audkenni = audkenni
        self.vidskiptavinir = vidskiptavinir
        self.pontunardagur = pontunardagur
        self.ath = ath





