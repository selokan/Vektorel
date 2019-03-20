class Harf_Sayaci:
    def __init__(self):
        self.sesli_harfler ="aeiıoüöu"
        self.sessiz_harfler = "qwrtypğşçlkmjnhbgvfcdxsz"
        self.turkce_harf="çığöşü"
        self.sessiz_sayac = 0
        self.sesli_sayac = 0
        self.turkce_sayac=0
        self.kelime = ""

    def kelime_sor(self):
        return input("Kelimeyi giriniz")

    def seslidir(self,harf):
        return harf in self.sesli_harfler
    
    def sessizdir(self,harf):
        return harf in self.sessiz_harfler
    
    def turkce(self,harf):
        return harf in self.turkce_harf

    def arttır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sesli_sayac += 1
            if self.sessizdir(harf):
                self.sessiz_sayac += 1
            if self.turkce(harf):
                self.turkce_sayac += 1

        return (self.sessiz_sayac,self.sesli_sayac,self.turkce_sayac)

    def ekrana_bas(self):
        sayim = self.arttır()
        mesaj = "{} kelimesinde {} tane sesli ve {} tane sessiz harf var aynı zamanda {} kadar türkçe karakter vardır"
        print(mesaj.format(self.kelime,sayim[1],sayim[0],sayim[2]))

    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

