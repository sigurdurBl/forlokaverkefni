#Sigurður Aron Blöndal, Þórður Jónatansson
#Lokaverkefni forritunar.

#Klasssi fyrir viðskifta vininn
class Vidskiptavinur:
    def __init__(self,nafn,heimili,kt,þjoderni,okt,simi,postur):
        self.nafn = nafn
        self.hemili = heimili
        self.kt =kt
        self.þjoderni = þjoderni
        self.okt = okt
        self.simi = simi
        self.postur = postur
    #þetta fall les texta skrá sem heldur um uplísingar um vidskiftavinn og prentar það svo út
    def readVIdskiftavindur(self):
        vidskipavinur = []

        with open("vidskiftavinur.txt", "r") as bill1:
            lina = bill1.read().splitlines()

            for x in lina:
                vidskipavinur.append(x.split(","))

        for madur in vidskipavinur:
            for x in madur:
                print(x,end="  ")
            print()
           # print(x[0])


class bill:
    #þetta er klasssi fyrir bílana
    def __init__(self,skranr,argerd,tegund,framledari,ath,leyfilegurfjoldimanna):
        self.skranr = skranr
        self.argerd = argerd
        self.tegund = tegund
        self.framledari = framledari
        self.ath = ath
        self.leyfilegurfjoldimanna = leyfilegurfjoldimanna
    #þetta fall les texta skrá sem heldur um uplísingar um bíla og prenta það svo út
    def readFile(self):
        val = input("hvernig bíl ertu að leita af jeppi sportsbill eða folksbill")

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

        #return temp


#Klassi fyrir pantanir
class pantanair:
    def __init__(self,audkenni,vidskiptavinir,pontunardagur,ath):
        self.audkenni = audkenni
        self.vidskiptavinir = vidskiptavinir
        self.pontunardagur = pontunardagur
        self.ath = ath
    #þetta fall les texta skrár sem heldur um pantanir á bílum og prenta svo það út
    def readpantanair(self):
        pantanir = []
        lina = ""

        with open("pontun.txt", "r") as pontun1:
            lina = pontun1.read().splitlines()
            # print(lina)
            for x in lina:
                pantanir.append(x.split(","))
                # vidskipavinur.remove("")
                # print(vidskipavinur)
        for x in pantanir:
            print(x)
            print(x[0])

#Klassi fyrir bilaleigu
class bilalegia:
    #þetta fall les texta skrá sem heldur um uplýsingar um bílaleigu fyrir bíla
    def readbilalega(self,val,val2):
        val = input("hvaða bíl ertu að leita af")
        val2 = input("hvaða viku vilt þú leigja")
        my_dict = {}

        with open("bilaleiga.txt","r") as bilalegan:
            linur = bilalegan.read()
            print(linur)
            my_dict=eval(linur)
            print(my_dict)
            for k,v in my_dict.items():
                if val == k and val2 == v:
                    print(k,"er í leigu í viku :",v)
                elif val == k and val2 != v:
                    my_dict[val] = val2
                    print("þú valdir að leigja bílin :",val,"og í viku :",val2)
                    with open("bilalegiga.txt","w") as bilalegan:
                        bilalegan.write(str(my_dict))
                    with open("bilaleiga.txt","r") as bilalegan:
                        read = bilalegan.read()
                        print(read)



                else:
                    print("Bíll ekkið til :(")
            #print(k,v)

svar = "N"
while svar == "N":
    print("1 = Prenta út Vidskiptavinur :")
    print("2 = Prenta út Bíll :")
    print("3 = Prenta út Pantanair :")
    print("4 = Prenta út Bílaleiga :")
    print("5 = leiga bíl :")
    print("6 = Hætta í Forriti :")
    v = int(input("hvað vilt þú velja ? :"))

    if v == 1:
        print("Þú hefur valið að Prenta út Vidskiptavini.")
        a = Vidskiptavinur("","","","","","","")
        print(a.readVIdskiftavindur())
    if v == 2:
        print("Þú hefur valið að Prenta út Bíla.")
        b = bill("","","","","","")
        print(b.readFile())

    if v == 3:
        print("Þú hefur valið að Prenta út Pantanair.")
        p = pantanair("","","","")
        print(p.readpantanair())

    if v == 4:
        print("Þú hefur valið að Prenta út Bílaleigu.")
        bl = bilalegia()
        print(bl.readbilalega("",""))

    if v == 6:
        svar = input("vilt þú hætta? Y/N")


