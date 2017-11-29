
class Vidskiptavinur:
    def __init__(self,nafn,heimili,kt,þjoderni,okt,simi,postur):
        self.nafn = nafn
        self.hemili = heimili
        self.kt =kt
        self.þjoderni = þjoderni
        self.okt = okt
        self.simi = simi
        self.postur = postur

    def readVIdskiftavindur(self):
        vidskipavinur = []
        lina = ""
        with open("vidskiftavinur.txt", "r") as bill1:
            lina = bill1.read()
            vinur = lina.split(":")
            vinur.remove("")
        print(vinur)
        vinurtemp = []
        for x in vinur:
            vinurtemp = x.split(",")
        return vinurtemp



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

    def readFile(self):
        val = input("hvað ertu að leita af")
        # val = "\"" + val + "\""
        bilar = []
        lina = ""
        with open("bill.txt", "r") as bill1:
            lina = bill1.read()
            bilar = lina.split(":")
            bilar.remove("")
            # bilar=lina.split(",")
        print(bilar)
        temp = []
        for x in bilar:
            temp = x.split(",")

            print(val)
            # print(temp[2])
            temp[2] = temp[2][1:-1]
            print("verður svona", temp[2])
            if val == temp[2]:
                print(temp)
                # print(temp[2])
                # for lin in bilar:
                # print(lin)

        return temp



class pantanair:
    def __init__(self,audkenni,vidskiptavinir,pontunardagur,ath):
        self.audkenni = audkenni
        self.vidskiptavinir = vidskiptavinir
        self.pontunardagur = pontunardagur
        self.ath = ath

print(Vidskiptavinur("","","","","","","").readVIdskiftavindur())
print(bill("","","","","").readFile())
