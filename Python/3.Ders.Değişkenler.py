# Python Temelleri -3- Degiskenler

# Degiskenler, programda kullanacağımız verileri saklamak için kullanılan bellek alanlarıdır.
# Python'da değişkenler oluşturmak için bir isim verilir ve bu isme bir değer atanır.
# Degiskenler, programın çalışması sırasında değerlerini değiştirebilir ve farklı türde verileri saklayabilir.
# Degisken olustururken uyulması gereken kurallar vardır.
# Python dilinde degisken atamak için "=" (eşittir) operatörü kullanılır. Degiskenin ismi solda, değeri ise sağda yer alır.


print("Python'da Degiskenler ve Atama İşlemleri")


#--------------------------------------------------------
print("\n---Degisken Atama Örnekleri---")

# Temel Veri Tipleri ile Atama
yas = 25                  # Integer (Tam Sayı)
isim = "Python"           # String (Metin)
sicaklik = 36.5           # Float (Ondalıklı Sayı)
kabul_edildi = True       # Boolean (Mantıksal - Doğru/Yanlış)

print("Yaş:", yas)
print("İsim:", isim)
print("Sıcaklık:", sicaklik)
print("Kabul Edildi mi?:", kabul_edildi)

# Çoklu Atama (Aynı satırda birden fazla değişkene atama yapma)
a, b, c = 10, 20, "Merhaba"
print("\nÇoklu atama -> a:", a, "b:", b, "c:", c)

# Aynı Değeri Birden Fazla Değişkene Atama
x = y = z = 100
print("x, y, z değerleri:", x, y, z)


#--------------------------------------------------------
print("\n---Degisken İsimlendirme Kuralları---")

# 1. Kural: Değişken isimleri rakam ile başlayamaz.
# 1sayi = 10       # YANLIŞ! SyntaxError (Sözdizimi hatası) verir.
sayi1 = 10         # DOĞRU!

# 2. Kural: Değişken isimlerinde boşluk bırakılamaz, alt çizgi (_) kullanılır.
# ogrenci numarasi = 123  # YANLIŞ!
ogrenci_numarasi = 123    # DOĞRU! (Buna 'snake_case' isimlendirme denir ve Python'da yaygındır)

# 3. Kural: Sadece harfler, rakamlar ve alt çizgi (_) kullanılabilir. Özel karakterler (@, !, #, % vb.) kullanılamaz.
# mail@adresi = "a@a.com" # YANLIŞ!
mail_adresi = "a@a.com"   # DOĞRU!

# 4. Kural: Büyük-küçük harf duyarlılığı vardır (Case Sensitive).
Sayi = 50
sayi = 100
print(f"Büyük 'S' ile: {Sayi}, Küçük 's' ile: {sayi}") # İkisi bellekte farklı yer tutan farklı değişkenlerdir.

# 5. Kural: Python'a ait özel anahtar kelimeler (keywords) değişken ismi olarak kullanılamaz.
# (Örnek: if, for, while, def, class, True, False, and, or vb.)
# if = "Koşul"     # YANLIŞ! 'if' Python'a ait bir komuttur.

# 6. Kural: Türkçe karakter kullanımı Python 3'te desteklense de (ç, ş, ğ, ü, ö, ı), evrensel standartlar gereği KULLANILMAMASI önerilir.
# kullanıcı_yaşı = 20  # ÇALIŞIR, ancak iyi bir pratik değildir.
kullanici_yasi = 20    # DOĞRU PRATİK!

# 7. Kural: Degisken isimleri mumkunse kisa olmalı, ancak anlamlı olmalıdır. Anlamlı isimler, kodun okunabilirliğini artırır.
Tum_Siniflardaki_Öğrenci_Sayısı = 30  # Anlamlı ama uzun
ogrenci_sayisi = 30                   # Anlamlı ve kısa (iyi bir pratik)
