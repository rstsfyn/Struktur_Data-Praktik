class KalkulatorSederhana:
    
    def __init__(self, bilangan1, bilangan2):
        self.bilangan1 = bilangan1
        self.bilangan2 = bilangan2
    
    
#SET BILANGAN
    def set_bilangan1(self, bilangan1):
        self.bilangan1 = bilangan1
        
    def set_bilangan2(self, bilangan2):
        self.bilangan2 = bilangan2
    
    
#OPERASI
    def tambah(self):
        hasil = self.bilangan1+self.bilangan2
        print(self.bilangan1, "+", self.bilangan2)
        return hasil
        
    def pangkat(self):
        hasil = 1
        for i in range(self.bilangan2):
            hasil *= self.bilangan1
        print(self.bilangan1, "**",  self.bilangan2)
        return hasil
    def kali(self):
        hasil = self.bilangan1*self.bilangan2
        print(self.bilangan1, "*", self.bilangan2)
        return hasil
    def kurang(self):
        hasil = self.bilangan1-self.bilangan2
        print(self.bilangan1, "-", self.bilangan2)
        return hasil
    

#BILANGAN DEFAULT
kalkulatorku = KalkulatorSederhana(25,30)


def menu():
    while True:
        print("="*30)
        print("=====KALKULATOR SEDERHANA=====")
        print("="*30)
        print("1. Hasil dari Tambah")
        print("2. Hasil dari Pangkat")
        print("3. Hasil dari Perkalian")
        print("4. Hasil dari Pengurangan")
        print("5. Keluar")
        print("="*30)
        
        pilihan = int(input("silahkan pilih menu: "))
        if pilihan == 1:
            print("Hasil = ",kalkulatorku.tambah())
        elif pilihan == 2:
            kalkulatorku.set_bilangan1(2)
            kalkulatorku.set_bilangan2(10)
            print("Hasil = ",kalkulatorku.pangkat())
        elif pilihan == 3:
            kalkulatorku.set_bilangan1(int(input("Silahkan masukkan bilangan 1 : ")))
            kalkulatorku.set_bilangan2(int(input("Silahkan masukkan bilangan 2 : ")))
            print("Hasil = ",kalkulatorku.kali())
        elif pilihan == 4:
            kalkulatorku.set_bilangan1(int(input("Silahkan masukkan bilangan 1 : ")))
            kalkulatorku.set_bilangan2(int(input("Silahkan masukkan bilangan 2 : ")))
            print("Hasil = ",kalkulatorku.kurang())
        else:
            print("terimkasih telah menggunakan program ini")
            break

menu()
