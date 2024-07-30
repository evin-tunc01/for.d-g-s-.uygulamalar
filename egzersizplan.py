# Haftalık egzersiz planı

egzersiz_plani = {
    "Pazartesi": "Koşu",
    "Salı": "Ağırlık Çalışması",
    "Çarşamba": "Yoga",
    "Perşembe": "Yüzme",
    "Cuma": "Pilates",
    "Cumartesi": "Dinlenme",
    "Pazar": "Yürüyüş"
}

print("Haftalık Egzersiz Planı:")
for gun, egzersiz in egzersiz_plani.items():
    print(f"{gun}: {egzersiz}")
