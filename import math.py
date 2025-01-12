import math

# Oklid mesafesini hesaplayan fonksiyon
def oklid_mesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0]) ** 2 + (nokta2[1] - nokta1[1]) ** 2)

# Noktalarin tanimlanmasi
# Ornek olarak 5 nokta tanimliyoum
noktalar = [
    (2, 3),
    (5, 7),
    (1, 9),
    (8, 2),
    (4, 5)
]

# Minimum mesafenin bulunmasi
def minimum_mesafe(noktalar):
    min_mesafe = float('inf')  # Baslangicta sonsuz olarak ayarlanir
    en_yakin_noktalar = (None, None)
    
    # Tum nokta ciftleri arasindaki mesafeleri hesapla
    for i in range(len(noktalar)):
        for j in range(i + 1, len(noktalar)):
            mesafe = oklid_mesafesi(noktalar[i], noktalar[j])
            if mesafe < min_mesafe:
                min_mesafe = mesafe
                en_yakin_noktalar = (noktalar[i], noktalar[j])
    
    return min_mesafe, en_yakin_noktalar

# Hesaplama ve sonuclarin yazdirilmasi
mesafe, noktalar = minimum_mesafe(noktalar)
print(f"En yakin noktalar: {noktalar[0]} ve {noktalar[1]}")
print(f"Aralarindaki Oklid mesafesi: {mesafe}")
