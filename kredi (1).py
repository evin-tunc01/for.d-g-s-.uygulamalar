# Kredi kartı borcu ödemesini izleme

toplam_borc = 500.0  # Başlangıç borcu
odenen_tutar = 0.0

print("Kredi Kartı Borcu Ödeme Takibi")
print(f"Toplam Borç: {toplam_borc:.2f} TL")

while odenen_tutar < toplam_borc:
    try:
        miktar = float(input("Ödediğiniz miktarı TL cinsinden girin: "))
        if miktar <= 0:
            print("Lütfen pozitif bir değer girin.")
            continue
        odenen_tutar += miktar
        if odenen_tutar >= toplam_borc:
            print(f"Tebrikler! Kredi kartı borcunuzu ödediniz. Toplam ödendi: {odenen_tutar:.2f} TL")
            break
        else:
            print(f"Kalan borç: {toplam_borc - odenen_tutar:.2f} TL")
    except ValueError:
        print("Geçerli bir miktar girin.")