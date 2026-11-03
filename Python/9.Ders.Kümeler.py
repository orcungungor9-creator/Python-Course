# Python Temelleri -9- Kümeler (Sets)

# Kümeler (set), matematikteki küme mantığıyla aynı şekilde çalışan veri yapılarıdır.
# Süslü parantezler {} kullanılarak oluşturulurlar.
# En önemli iki özelliği:
# 1. İçerisindeki elemanlar "sırasızdır" (indeksleme yapılamaz, yani kume[0] çalışmaz).
# 2. İçerisinde aynı elemandan birden fazla bulunamaz (benzersiz/unique veriler tutar).

# --------------------------------------------------------
# 1. BÖLÜM: KÜME OLUŞTURMA VE BENZERSİZLİK (UNIQUE) KURALI
# --------------------------------------------------------

# Standart küme oluşturma
meyveler = {"Elma", "Armut", "Muz", "Elma", "Armut"}

print("--- KÜME OLUŞTURMA ---\n")
# Çıktıda göreceğiniz gibi tekrar eden "Elma" ve "Armut" sadece birer kez yazdırılır.
# Ayrıca elemanların sırası her çalıştırmada değişebilir, çünkü kümeler sırasızdır.
print("Meyveler kümesi :", meyveler)

# ÖNEMLİ: Boş küme oluşturmak için {} YERİNE set() fonksiyonu kullanılmalıdır.
# Çünkü {} Python'da sözlük (dictionary) veri tipi olarak algılanır.
bos_kume = set()
bos_sozluk = {}
print(f"bos_kume Tipi   : {type(bos_kume)}")
print(f"bos_sozluk Tipi : {type(bos_sozluk)}")

# Listeyi kümeye çevirerek tekrarlı verilerden kurtulmak (Veri temizlemede çok sık kullanılır)
tekrarli_liste = [1, 2, 2, 3, 3, 3, 4, 5, 5]
temiz_kume = set(tekrarli_liste)
print("\nTekrarlı Liste  :", tekrarli_liste)
print("Kümeye Çevrilmiş:", temiz_kume)

# --------------------------------------------------------
# 2. BÖLÜM: KÜMEYE ELEMAN EKLEME VE ÇIKARMA
# --------------------------------------------------------

renkler = {"Kırmızı", "Mavi", "Yeşil"}
print("\n--- ELEMAN EKLEME VE ÇIKARMA ---\n")

# 1. add(eleman): Kümeye yeni bir eleman ekler.
renkler.add("Sarı")
print("add('Sarı') sonrası       :", renkler)

# 2. remove(eleman): Belirtilen elemanı siler. Eğer eleman kümede yoksa HATA (KeyError) verir.
renkler.remove("Mavi")
print("remove('Mavi') sonrası    :", renkler)

# 3. discard(eleman): Belirtilen elemanı siler. Eleman kümede yoksa HATA VERMEZ (daha güvenlidir).
renkler.discard("Siyah") # Siyah kümede yok ama program çökmeden devam eder.
print("discard('Siyah') denemesi :", renkler)

# 4. clear(): Kümenin içindeki tüm elemanları silerek kümeyi boşaltır.
renkler.clear()
print("clear() sonrası küme      :", renkler)

# --------------------------------------------------------
# 3. BÖLÜM: MATEMATİKSEL KÜME İŞLEMLERİ
# --------------------------------------------------------

# Kümeler, birden fazla veri grubu arasında karşılaştırma yaparken metodları sayesinde çok güçlüdür.
kume_A = {1, 2, 3, 4, 5}
kume_B = {4, 5, 6, 7, 8}

print("\n--- MATEMATİKSEL KÜME İŞLEMLERİ ---\n")
print(f"A Kümesi: {kume_A}")
print(f"B Kümesi: {kume_B}\n")

# 1. Birleşim (Union) -> union() veya | sembolü
birlesim = kume_A.union(kume_B)
# birlesim = kume_A | kume_B  # Alternatif kısa kullanım
print("1. Birleşim (A U B)       :", birlesim)

# 2. Kesişim (Intersection) -> intersection() veya & sembolü
kesisim = kume_A.intersection(kume_B)
# kesisim = kume_A & kume_B   # Alternatif kısa kullanım
print("2. Kesişim (A ∩ B)        :", kesisim)

# 3. Fark (Difference) -> difference() veya - sembolü
fark_A_B = kume_A.difference(kume_B) # A'da olup B'de olmayanlar
# fark_A_B = kume_A - kume_B  # Alternatif kısa kullanım
print("3. A'nın B'den Farkı (A-B):", fark_A_B)

# 4. Simetrik Fark (Symmetric Difference) -> symmetric_difference() veya ^ sembolü
# Her iki kümenin kesişimi dışındaki tüm elemanlar (Yalnızca birinde olanlar)
simetrik_fark = kume_A.symmetric_difference(kume_B)
print("4. Simetrik Fark (A ^ B)  :", simetrik_fark)