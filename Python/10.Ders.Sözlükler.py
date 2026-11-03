# Python Temelleri -10- Sözlükler (Dictionaries)

# Sözlükler (dict), verileri tıpkı gerçek hayattaki bir sözlük gibi "Anahtar-Değer" (Key-Value)
# çiftleri şeklinde tutan veri yapılarıdır.
# Süslü parantezler {} ile oluşturulur ancak kümelerden farklı olarak içerisinde
# aralarında iki nokta (:) bulunan eşleşmeler barındırır.
# Özellikle yapılandırılmış veriler (veritabanı kayıtları, JSON dosyaları) için vazgeçilmezdir.

# --------------------------------------------------------
# 1. BÖLÜM: SÖZLÜK OLUŞTURMA VE VERİYE ERİŞİM
# --------------------------------------------------------

# Bir profil kaydını sözlük ile modelleyelim:
kullanici_profili = {
    "isim": "Orçun",
    "yas": 20,
    "bolum": "Ekonometri",
    "mezun_mu": False,
    "yetenekler": ["Python", "SQL", "R"] # Değer olarak bir liste bile verebiliriz!
}

print("--- SÖZLÜK OLUŞTURMA VE ERİŞİM ---\n")
print("Tüm Sözlük:", kullanici_profili)

# Veriye erişmek için indeks numarası değil, doğrudan "Anahtar" (Key) adını kullanırız.
print("\nKullanıcının Adı  :", kullanici_profili["isim"])
print("Okuduğu Bölüm     :", kullanici_profili["bolum"])
print("Bildiği ilk dil   :", kullanici_profili["yetenekler"][0]) # Sözlük içindeki listeye erişim

# get() Metodu ile Güvenli Erişim:
# Olmayan bir anahtarı köşeli parantezle çağırırsak Python KeyError hatası verir.
# Ancak get() metodu kullanırsak hata vermek yerine geriye 'None' (Yok) döner.
print("\nget() ile yaş     :", kullanici_profili.get("yas"))
print("Olmayan bir veri  :", kullanici_profili.get("okul_no")) # Hata vermez, None döner.

# --------------------------------------------------------
# 2. BÖLÜM: YENİ VERİ EKLEME VE GÜNCELLEME
# --------------------------------------------------------

print("\n--- VERİ EKLEME VE GÜNCELLEME ---\n")

# Yeni bir Anahtar-Değer çifti eklemek çok basittir.
# Olmayan bir anahtara değer atarsak, doğrudan sözlüğe yeni kayıt olarak eklenir.
kullanici_profili["universite"] = "Pamukkale Üniversitesi"
print("Üniversite eklendi    :", kullanici_profili)

# Var olan bir anahtara yeni değer atarsak, eski değer güncellenir.
kullanici_profili["yas"] = 21 
print("Yaş güncellendi       :", kullanici_profili)

# --------------------------------------------------------
# 3. BÖLÜM: TEMEL SÖZLÜK METODLARI
# --------------------------------------------------------

print("\n--- SÖZLÜK METODLARI ---\n")

# 1. keys(): Sadece sözlükteki "Anahtarları" (sol taraf) verir.
print("Sadece Anahtarlar     :", kullanici_profili.keys())

# 2. values(): Sadece sözlükteki "Değerleri" (sağ taraf) verir.
print("Sadece Değerler       :", kullanici_profili.values())

# 3. items(): Anahtar ve değerleri gruplar halinde birlikte verir. 
# Genelde döngülerle (for) verilerin üzerinde gezinmek için çok sık kullanılır.
print("Anahtar-Değer Çiftleri:", kullanici_profili.items())

# 4. update(): Başka bir sözlükteki verileri mevcut sözlüğe katar veya aynı anahtarları günceller.
fiziksel_bilgiler = {"boy_cm": 183, "kilo_kg": 75, "mezun_mu": True}
kullanici_profili.update(fiziksel_bilgiler)
print("\nupdate() sonrası      :", kullanici_profili)

# 5. pop(anahtar): Belirtilen anahtarı ve onun değerini sözlükten siler, sildiği değeri döndürür.
silinen_bolum = kullanici_profili.pop("bolum")
print(f"\npop() ile silinen bölüm: {silinen_bolum}")
print("Sözlüğün Son Durumu    :", kullanici_profili)