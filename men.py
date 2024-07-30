# Menüdeki yemeklerin ve içeceklerin fiyatlarını tanımlayalım
menu = {
    "Köfte": 25.0,
    "Izgara Tavuk": 30.0,
    "Pizza": 35.0,
    "Salata": 15.0,
    "Su": 5.0,
    "Kola": 8.0
}

def hesapla_toplam_fiyat(secenekler):
    toplam_fiyat = 0.0
    for secenek, miktar in secenekler.items():
        if secenek in menu:
            toplam_fiyat += menu[secenek] * miktar
        else:
            print(f"{secenek} menüde bulunmuyor.")
    return toplam_fiyat

# Kullanıcıdan seçimleri al
def kullanici_secimlerini_al():
    secimler = {}
    print("Lütfen menüdeki yemeklerin adlarını ve miktarlarını girin (bitirmek için 'bitir' yazın):")
    
    while True:
        secim = input("Yemek adı (örnek: Köfte) veya 'bitir' : ")
        if secim.lower() == 'bitir':
            break
        if secim not in menu:
            print(f"{secim} menüde bulunmuyor. Lütfen tekrar deneyin.")
            continue
        try:
            miktar = int(input(f"{secim} için miktar: "))
            if miktar <= 0:
                print("Miktar 0'dan büyük olmalıdır.")
                continue
            secimler[secim] = secimler.get(secim, 0) + miktar
        except ValueError:
            print("Geçerli bir miktar girin.")
    
    return secimler

# Ana fonksiyon
def main():
    secimler = kullanici_secimlerini_al()
    toplam_fiyat = hesapla_toplam_fiyat(secimler)
    print(f"Toplam Fiyat: {toplam_fiyat:.2f} TL")

if __name__ == "__main__":
    main()
