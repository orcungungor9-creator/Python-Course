# Python Temelleri -8- Demetler (Tuples)

# Demetler (tuple), listelere çok benzeyen ancak "değiştirilemez" (immutable) olan veri yapılarıdır.
# Normal parantez () kullanılarak veya sadece elemanlar virgülle ayrılarak oluşturulurlar.
# Oluşturulduktan sonra içindeki elemanlar güncellenemez, yeni eleman eklenemez veya silinemez.
# Sabit kalmasını istediğimiz veriler (örneğin harita koordinatları, ay isimleri, sistem ayarları) için idealdir.

# --------------------------------------------------------
# 1. BÖLÜM: DEMET (TUPLE) OLUŞTURMA VE ÖZEL DURUMLAR
# --------------------------------------------------------

# Standart bir tuple tanımı
renkler = ("Kırmızı", "Yeşil", "Mavi")

# Parantez kullanmadan da tuple oluşturulabilir (Python virgülleri görünce tuple anlar)
koordinatlar = 41.0082, 28.9784 

# ÖNEMLİ KURAL: Tek elemanlı bir tuple oluştururken sonuna virgül koymak zorunludur!
# Aksi takdirde Python bunu normal bir parantez (matematiksel/string) olarak algılar.
tek_elemanli_tuple = ("Elma",)
normal_string = ("Elma") 

print("--- DEMET OLUŞTURMA ---\n")
print(f"Renkler        : {renkler} \t Tipi: {type(renkler)}")
print(f"Koordinatlar   : {koordinatlar} \t Tipi: {type(koordinatlar)}")
print(f"Tek Elemanlı   : {tek_elemanli_tuple} \t\t Tipi: {type(tek_elemanli_tuple)}")
print(f"Virgülsüz Hata : {normal_string} \t\t Tipi: {type(normal_string)}")

# --------------------------------------------------------
# 2. BÖLÜM: İNDEKSLEME VE DEĞİŞTİRİLEMEZLİK (IMMUTABLE)
# --------------------------------------------------------

# Listelerdeki ve stringlerdeki indeksleme (sıfırdan başlama) ve dilimleme mantığı tamamen geçerlidir.
mevsimler = ("İlkbahar", "Yaz", "Sonbahar", "Kış")

print("\n--- İNDEKSLEME VE DİLİMLEME ---\n")
print("İlk mevsim    :", mevsimler[0])
print("Son mevsim    :", mevsimler[-1])
print("İlk 2 mevsim  :", mevsimler[0:2])

# DEĞİŞTİRİLEMEZLİK (IMMUTABILITY) KURALI:
# Tuple içindeki bir elemanı listelerdeki gibi değiştiremeyiz.
# Eğer aşağıdaki kodu çalıştırırsak Python "TypeError" hatası verir:
# mevsimler[1] = "Sıcak Yaz"  # HATA VERİR! Tuple nesnesi atama işlemini desteklemez.

# --------------------------------------------------------
# 3. BÖLÜM: DEMET METODLARI VE PAKET AÇMA (UNPACKING)
# --------------------------------------------------------

# Tuple'lar değiştirilemez olduğu için append, remove, pop gibi listelere özgü metodları yoktur.
# Sadece veri aramaya yönelik 2 adet metodları vardır: count() ve index()

sayilar_tuple = (1, 5, 3, 5, 9, 5, 2)

print("\n--- DEMET METODLARI ---\n")
# 1. count(eleman): Demetin içinde belirtilen elemandan kaç tane olduğunu sayar.
print(f"Tuple içinde '5' sayısı {sayilar_tuple.count(5)} kez geçiyor.")

# 2. index(eleman): Belirtilen elemanın baştan kaçıncı indekste (ilk nerede) olduğunu söyler.
print(f"'9' sayısı tuple içinde {sayilar_tuple.index(9)}. indekste bulunuyor.")

# PAKET AÇMA (Unpacking): Tuple içindeki değerleri sırasıyla çoklu değişkenlere tek satırda atama işlemidir.
# Python'da çok sık kullanılan ve kod okunuşunu güzelleştiren bir özelliktir.
print("\n--- PAKET AÇMA (UNPACKING) ---\n")

kullanici_bilgisi = ("Orçun", 20, "Ekonometri")
isim, yas, bolum = kullanici_bilgisi # Elemanlar sırasıyla değişkenlere otomatik atandı!

print(f"İsim  : {isim}")
print(f"Yaş   : {yas}")
print(f"Bölüm : {bolum}")