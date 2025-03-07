import os

def menu():
    print("╔════════════════════════════════════════╗")
    print("║                                        ║")
    print("║        Kümese giriş yapan hayvanlar    ║")
    print("║                                        ║")
    print("╠════════════════════════════════════════╣")
    print("║ 1 - Yeni Hayvan ekle                   ║")
    print("║ 2 - Kayıtları Listele                  ║")
    print("║ 3 - Kayıt Ara                          ║")
    print("║ 4 - Kayıt Sil                          ║")
    print("║ 5 - Kayıt Güncelle                     ║")
    print("║ 6 - Çıkış                              ║")
    print("╚════════════════════════════════════════╝")

def yeni_kayit():
    isim = input("Türü: ")
    cins = input("Hayvan ismi: ")
    with open("rehber.txt", "a") as file:
        file.write(f"{isim},{cins}\n")
    print("Kayıt eklendi.")

def kayitlari_listele():
    if os.path.exists("rehber.txt"):
        with open("rehber.txt", "r") as file:
            print("╔════════════════════════════════════════╗")
            print("║           Kayıtlı hayvanlar            ║")
            print("╠════════════════════════════════════════╣")
            for line in file:
                isim, cins = line.strip().split(",")
                print(f"║ Türü: {isim}, İsmi: {cins} ║")
            print("╚════════════════════════════════════════╝")
    else:
        print("Rehberde kayıt yok.")

def kayit_ara():
    aranan = input("Aramak istediğiniz tür veya isim: ")
    bulundu = False
    if os.path.exists("rehber.txt"):
        with open("rehber.txt", "r") as file:
            for line in file:
                if aranan in line:
                    isim, cins = line.strip().split(",")
                    print(f"Türü: {isim}, İsmi: {cins}")
                    bulundu = True
        if not bulundu:
            print("Kayıt bulunamadı.")
    else:
        print("Rehberde kayıt yok.")

def kayit_sil():
    aranan = input("Silmek istediğiniz tür veya isim: ")
    bulundu = False
    if os.path.exists("rehber.txt"):
        with open("rehber.txt", "r") as file:
            lines = file.readlines()
        with open("rehber.txt", "w") as file:
            for line in lines:
                if aranan not in line:
                    file.write(line)
                else:
                    bulundu = True
        if bulundu:
            print("Kayıt silindi.")
        else:
            print("Kayıt bulunamadı.")
    else:
        print("Rehberde kayıt yok.")

def kayit_guncelle():
    aranan = input("Güncellemek istediğiniz tür veya isim: ")
    bulundu = False
    if os.path.exists("rehber.txt"):
        with open("rehber.txt", "r") as file:
            lines = file.readlines()
        with open("rehber.txt", "w") as file:
            for line in lines:
                if aranan in line:
                    isim, cins = line.strip().split(",")
                    yeni_isim = input(f"Yeni Tür ({isim}): ") or isim
                    yeni_cins = input(f"Yeni İsim ({cins}): ") or cins
                    file.write(f"{yeni_isim},{yeni_cins}\n")
                    bulundu = True
                else:
                    file.write(line)
        if bulundu:
            print("Kayıt güncellendi.")
        else:
            print("Kayıt bulunamadı.")
    else:
        print("Rehberde kayıt yok.")

def main():
    while True:
        menu()
        secim = input("Seçiminiz: ")
        if secim == "1":
            yeni_kayit()
        elif secim == "2":
            kayitlari_listele()
        elif secim == "3":
            kayit_ara()
        elif secim == "4":
            kayit_sil()
        elif secim == "5":
            kayit_guncelle()
        elif secim == "6":
            print("Çıkış yapılıyor...")
            break            
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()