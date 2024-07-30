# Alışveriş listesi (ürün adı: (birim fiyat, miktar))
alisveris_listesi = {
    "Süt": (10.0, 2),  # 10.0 TL birim fiyatı, 2 litre
    "Ekmek": (5.0, 3), # 5.0 TL birim fiyatı, 3 adet
    "Peynir": (20.0, 1), # 20.0 TL birim fiyatı, 1 kilogram
    "Yumurta": (0.5, 12) # 0.5 TL birim fiyatı, 12 adet
}

toplam_maliyet = 0.0

for urun, (birim_fiyat, miktar) in alisveris_listesi.items():
    maliyet = birim_fiyat * miktar
    toplam_maliyet += maliyet
    print(f"{urun}: {miktar} adet x {birim_fiyat:.2f} TL = {maliyet:.2f} TL")

print(f"Toplam Alışveriş Maliyeti: {toplam_maliyet:.2f} TL")
