# Python Temelleri -11- Karşılaştırma ve Mantıksal Operatörler

# Programlamada karar mekanizmalarını (if-else, döngüler vb.) kurabilmek için
# verileri birbiriyle karşılaştırmamız ve mantıksal sonuçlar üretmemiz gerekir.
# Karşılaştırma ve mantıksal operatörlerin sonucunda her zaman 'bool' (True veya False) veri tipi döner.

# --------------------------------------------------------
# 1. BÖLÜM: KARŞILAŞTIRMA OPERATÖRLERİ
# --------------------------------------------------------

# Karşılaştırma operatörleri sağındaki ve solundaki iki değeri kıyaslar.
a = 15
b = 20

print("--- KARŞILAŞTIRMA OPERATÖRLERİ ---\n")
print(f"A değişkeni: {a}, B değişkeni: {b}\n")

# 1. Eşit mi? (==) -> Tek eşittir (=) atama yapar, çift eşittir (==) kıyaslar!
print("A, B'ye eşit mi? (a == b)       :", a == b)

# 2. Eşit değil mi? (!=)
print("A, B'den farklı mı? (a != b)    :", a != b)

# 3. Büyüktür (>) ve Küçüktür (<)
print("A, B'den büyük mü? (a > b)      :", a > b)
print("A, B'den küçük mü? (a < b)      :", a < b)

# 4. Büyük Eşittir (>=) ve Küçük Eşittir (<=)
print("A, 15'e büyük veya eşit mi?     :", a >= 15) # True, çünkü a zaten 15'e eşit.

# Stringlerde (metinlerde) karşılaştırma da yapılabilir. Python büyük/küçük harf duyarlıdır!
print("\n'Python' == 'python' sonucu     :", "Python" == "python") # False

# --------------------------------------------------------
# 2. BÖLÜM: MANTIKSAL OPERATÖRLER (AND, OR, NOT)
# --------------------------------------------------------

# Birden fazla karşılaştırmayı (koşulu) birbirine bağlamak için kullanılırlar.

sinav_puani = 85
devamsizlik = 3

print("\n--- MANTIKSAL OPERATÖRLER ---\n")
print(f"Sınav Puanı: {sinav_puani}, Devamsızlık: {devamsizlik} gün\n")

# 1. AND (Ve) Operatörü:
# Bağlanan TÜM koşulların doğru (True) olması zorunludur. Biri bile False ise genel sonuç False çıkar.
# Senaryo: Dersi geçmek için puan 50'den büyük/eşit OLMALI VE devamsızlık 5'ten küçük OLMALI.
gecti_mi = (sinav_puani >= 50) and (devamsizlik < 5)
print("Öğrenci dersi geçti mi? (AND)   :", gecti_mi)

# 2. OR (Veya) Operatörü:
# Bağlanan koşullardan SADECE BİRİNİN doğru (True) olması genel sonucun True olması için yeterlidir.
# Senaryo: Burs almak için puan 90'dan büyük/eşit OLMALI VEYA devamsızlık 0 OLMALI.
burs_aliyor_mu = (sinav_puani >= 90) or (devamsizlik == 0)
print("Öğrenci burs alıyor mu? (OR)    :", burs_aliyor_mu)

# 3. NOT (Değil) Operatörü:
# Çıkan mantıksal sonucu tam tersine çevirir. (True ise False, False ise True yapar).
sistem_aktif_mi = True
print("\nSistem aktif mi?                :", sistem_aktif_mi)
print("Sistemin tersi (not aktif_mi)   :", not sistem_aktif_mi)

# --------------------------------------------------------
# 3. BÖLÜM: KARMAŞIK KOŞULLARI BİRLEŞTİRME
# --------------------------------------------------------

# Parantezler ile işlem önceliği belirleyerek daha uzun ve gerçekçi mantıksal sorgular yazabiliriz.
kredi_skoru = 1200
maas = 30000
kefil_var_mi = False

# Senaryo (Kredi Onay Şartı): 
# (Kredi skoru 1000'den büyük VE Maaşı 20000'den yüksek olmalı) VEYA Kefili olmalı.
kredi_onayi = ((kredi_skoru > 1000) and (maas > 20000)) or kefil_var_mi

print("\n--- KARMAŞIK SENARYO ---")
print(f"Kredi Onay Durumu               : {kredi_onayi}")
# --------------------------------------------------------
# 4. BÖLÜM: AİTLİK OPERATÖRLERİ (IN, NOT IN)
# --------------------------------------------------------

# Bir verinin, bir dizinin (metin, liste, tuple, küme) içinde bulunup bulunmadığını
# sorgulamak için kullanılır. Özellikle listelerde ve metinlerde arama yaparken hayat kurtarır.

kullanici_yetenekleri = ["Python", "SQL", "Excel"]
aranan_kelime = "Analiz"
metin = "Veri Analizi çok eğlenceli!"

print("\n--- AİTLİK (MEMBERSHIP) OPERATÖRLERİ ---\n")

# 1. in (İçinde var mı?)
print("Kullanıcı SQL biliyor mu? ('SQL' in liste)   :", "SQL" in kullanici_yetenekleri)
print("Metinde 'Analiz' geçiyor mu?                 :", aranan_kelime in metin)

# 2. not in (İçinde yok mu?)
print("Kullanıcı R BİLMİYOR mu? ('R' not in liste)  :", "R" not in kullanici_yetenekleri)

# --------------------------------------------------------
# 5. BÖLÜM: KİMLİK OPERATÖRLERİ (IS, IS NOT)
# --------------------------------------------------------

# '==' operatörü iki verinin 'değerinin' aynı olup olmadığına bakar.
# 'is' operatörü ise iki verinin bilgisayar hafızasında (bellekte) 'aynı obje' olup olmadığına bakar.

liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
liste3 = liste1 # liste3, doğrudan liste1'in bellekteki yerini işaret ediyor.

print("\n--- KİMLİK (IDENTITY) OPERATÖRLERİ ---\n")

# Değerleri tamamen aynı olduğu için == sonucu True çıkar.
print("liste1 ve liste2 değerleri eşit mi? (==)   :", liste1 == liste2)

# Değerleri aynı olsa da bellekte farklı yerlerde tutuldukları için is sonucu False çıkar.
print("liste1 ve liste2 AYNI obje mi? (is)        :", liste1 is liste2)

# liste3 doğrudan liste1'e atandığı için ikisi de aynı objedir, sonuç True çıkar.
print("liste1 ve liste3 AYNI obje mi? (is)        :", liste1 is liste3)