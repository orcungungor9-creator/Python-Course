# Python Temelleri -6- Karakter Dizileri (Strings)

# Karakter dizileri (str), metinleri tuttuğumuz veri tipleridir.
# Python'da metinler harflerin, sayıların veya sembollerin bir araya gelmesiyle oluşur.
# Bu derste metinleri parçalamayı ve string metodlarıyla düzenlemeyi öğreneceğiz.

# --------------------------------------------------------
# 1. BÖLÜM: METİN TANIMLAMA VE UZUNLUK BULMA (LEN)
# --------------------------------------------------------

# Tek, çift veya üç tırnak ile string tanımlanabilir.
mesaj = "Python öğrenmek çok zevkli!"
cok_satirli_mesaj = """Bu metin
birden fazla
satıra yayılabilir."""

# len() fonksiyonu: Bir string'in kaç karakterden oluştuğunu (uzunluğunu) verir.
# Boşluklar ve noktalama işaretleri de birer karakter sayılır.
karakter_sayisi = len(mesaj)
print("--- UZUNLUK (LEN) ---")
print(f"'{mesaj}' metni tam {karakter_sayisi} karakterden oluşuyor.\n")

# --------------------------------------------------------
# 2. BÖLÜM: İNDEKSLEME VE DİLİMLEME (SLICING)
# --------------------------------------------------------

# Python'da saymaya 0'dan başlanır! (Sıfırıncı indeks)
# metin[başlangıç : bitiş : adım] kuralı ile metnin istediğimiz kısmını alabiliriz.

kurs_adi = "Veri Analizi"

print("--- İNDEKSLEME VE DİLİMLEME ---")
# 1. Tek bir karaktere ulaşmak
print("İlk harf       :", kurs_adi[0])   # 'V'
print("Üçüncü harf    :", kurs_adi[2])   # 'r'
print("Son harf       :", kurs_adi[-1])  # 'i' (Negatif indeks sondan başlar)

# 2. Metnin bir kısmını kesmek (Dilimleme / Slicing)
print("İlk 4 harf     :", kurs_adi[0:4]) # 'Veri' (4. indeks dahil edilmez)
print("4'ten sonrakiler:", kurs_adi[4:])  # ' Analizi' (4. indeksten sona kadar)

# 3. Adım atlayarak veya tersten kesmek
print("İkişer atlayarak :", kurs_adi[::2]) # 'Vr nlz' (Baştan sona 2 adımda bir)
print("Metni ters çevir :", kurs_adi[::-1])# 'izilanA ireV' (Geriye doğru 1 adım)

# --------------------------------------------------------
# 3. BÖLÜM: EN SIK KULLANILAN STRING METODLARI
# --------------------------------------------------------

# String metodları, mevcut metni değiştirmez, bize yeni bir metin döndürür.

ornek_metin = "   bugün hava ÇOK güzel.   "

print("\n--- STRING METODLARI ---")

# 1. upper() ve lower(): Tüm harfleri büyütür veya küçültür.
print("Büyük harf    :", ornek_metin.upper())
print("Küçük harf    :", ornek_metin.lower())

# 2. title() ve capitalize(): Baş harfleri büyütür.
# title() her kelimenin, capitalize() sadece ilk kelimenin baş harfini büyütür.
print("Title metodu  :", ornek_metin.title())

# 3. strip(): Metnin başındaki ve sonundaki gereksiz boşlukları (veya belirtilen karakterleri) siler.
temiz_metin = ornek_metin.strip()
print(f"Boşluksuz hali: '{temiz_metin}'")

# 4. replace(eski, yeni): Metin içindeki bir bölümü başka bir metinle değiştirir.
degismis_metin = temiz_metin.replace("bugün", "yarın")
print("Değiştirilmiş :", degismis_metin)

# 5. split(ayirici): Metni belirttiğimiz ayırıcıya göre bölüp bir "liste (list)" oluşturur.
# İçine değer girilmezse varsayılan olarak boşluklardan böler.
kelimeler = temiz_metin.split()
print("Kelimeler     :", kelimeler) # ['bugün', 'hava', 'ÇOK', 'güzel.']