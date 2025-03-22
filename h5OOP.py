class hesap():

    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2 

    def carp (self):
         sonuc1 = self.sayi1*self.sayi2
         return sonuc1 

    def bol (self):
        sonuc2 = self.sayi1/self.sayi2
        return sonuc2

    def topla (self):
        sonuc3 = self.sayi1+self.sayi2
        return sonuc3

    def cikar (self):
        sonuc4 = self.sayi1-self.sayi2
        return sonuc4

    def yazdir(self):
        toplam=self.topla()  
        print('Sayıların toplamı :' , toplam)

        carpma=self.carp()
        print('Sayıların çarpımı :' , carpma)

        bolme=self.bol()
        print('Sayıların bölümü :' , bolme)

        cikartma=self.cikar()
        print('Sayıların farkı :' , cikartma)


a = hesap(4,5)
a.yazdir()

print(a.topla())
print(a.cikar())
print(a.bol())
print(a.carp())
