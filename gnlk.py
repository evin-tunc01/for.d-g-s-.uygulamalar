# Günlük su tüketimi izleme

gunluk_hedef = 2.0  # 2 litre su içme hedefi
toplam_tuketim = 0.0

print("Günlük su tüketimini takip edelim.")
print(f"Günlük hedef: {gunluk_hedef} litre")

while toplam_tuketim < gunluk_hedef:
    try:
        miktar = float(input("İçtiğiniz su miktarını litre cinsinden girin: "))
        if miktar <= 0:
            print("Lütfen pozitif bir değer girin.")
            continue
        toplam_tuketim += miktar
        print(f"Toplam içtiğiniz su: {toplam_tuketim:.2f} litre")
        if toplam_tuketim >= gunluk_hedef:
            print("Tebrikler, günlük su tüketim hedefinize ulaştınız!")
    except ValueError:
        print("Geçerli bir sayı girin.")

