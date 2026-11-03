# Python Temelleri -12- Koşullu İfadeler (If - Elif - Else)

# Koşullu ifadeler, programlarımızın karar vermesini sağlayan en temel yapılardır.
# Bir önceki derste öğrendiğimiz karşılaştırma ve mantıksal operatörlerden dönen
# True veya False (bool) değerlerine göre programın farklı kod bloklarını çalıştırmasını sağlar.

# ÖNEMLİ KURAL (GİRİNTİ - INDENTATION): 
# Python'da hangi kodun "if" bloğuna ait olduğunu belirtmek için süslü parantez kullanılmaz.
# Bunun yerine "girinti" (Tab tuşu veya 4 boşluk) kullanılır. 
# İki nokta üst üste (:) işaretinden sonraki satır mutlaka içeriden başlamalıdır!

# --------------------------------------------------------
# 1. BÖLÜM: TEMEL IF (EĞER) VE ELSE (DEĞİLSE) YAPISI
# --------------------------------------------------------

print("--- 1. TEMEL IF - ELSE ---\n")

yas = 20

# Eğer yaş 18'den büyük veya eşitse (Sonuç True ise altındaki blok çalışır)
if yas >= 18:
    print("Ehliyet alabilirsiniz.")
    print("Bu satır da if bloğunun içindedir.")
# Eğer yukarıdaki if koşulu False ise (Yani yaş 18'den küçükse) else bloğu çalışır.
else:
    print("Ehliyet almak için yaşınız tutmuyor.")
    
print("Bu satırda girinti yok, o yüzden if-else durumundan bağımsız her zaman çalışır.\n")

# --------------------------------------------------------
# 2. BÖLÜM: ELIF (DEĞİLSE EĞER) İLE ÇOKLU KOŞULLAR
# --------------------------------------------------------

# Sadece iki ihtimal (doğru/yanlış) değil, birden fazla ihtimal varsa 'elif' kullanılır.
# Python yukarıdan aşağıya doğru koşulları kontrol eder. İlk True olan bloğu çalıştırır
# ve diğerlerini kontrol etmeden if-elif-else yapısından çıkar.

print("--- 2. ELIF İLE ÇOKLU KONTROL ---\n")

sinav_notu = 75

if sinav_notu >= 90:
    print("Harf Notunuz: AA")
elif sinav_notu >= 80:
    print("Harf Notunuz: BA")
elif sinav_notu >= 70:
    print("Harf Notunuz: BB")
elif sinav_notu >= 60:
    print("Harf Notunuz: CB")
else:
    print("Dersten kaldınız, Harf Notunuz: FF")

# --------------------------------------------------------
# 3. BÖLÜM: MANTIKSAL OPERATÖRLERLE (AND/OR) KULLANIM
# --------------------------------------------------------

# 11. derste gördüğümüz and, or, not operatörlerini if içinde kullanarak
# birden fazla şartı aynı anda kontrol edebiliriz.

print("\n--- 3. MANTIKSAL OPERATÖRLERLE IF ---\n")

kullanici_adi = "admin"
sifre = "12345"

# Hem kullanıcı adı doğru olmalı AND hem de şifre doğru olmalı
if kullanici_adi == "admin" and sifre == "12345":
    print("Sisteme başarıyla giriş yapıldı!")
else:
    print("Kullanıcı adı veya şifre hatalı!")

# --------------------------------------------------------
# 4. BÖLÜM: İÇ İÇE (NESTED) KOŞULLU İFADELER
# --------------------------------------------------------

# Bir koşulun içinde başka bir koşulu kontrol etmek isteyebiliriz.
# Bu durumda girintinin (indentation) içine bir girinti daha ekleriz.

print("\n--- 4. İÇ İÇE (NESTED) KONTROLLER ---\n")

sayi = 15

if sayi > 0:
    print("Sayı pozitiftir.")
    # Sayı pozitifse, şimdi de çift mi tek mi olduğuna bakalım.
    # Bir sayının 2'ye bölümünden kalan (modülüs %) 0 ise o sayı çifttir.
    if sayi % 2 == 0:
        print("Aynı zamanda bir çift sayıdır.")
    else:
        print("Aynı zamanda bir tek sayıdır.")
elif sayi < 0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")

# --------------------------------------------------------
# 5. BÖLÜM: KISA KULLANIM (TERNARY OPERATOR - TEK SATIRDA IF)
# --------------------------------------------------------

# Basit bir if-else atamasını tek satırda yazarak kodu kısaltabiliriz.
# Formül: [Değer_True_İse] if [Koşul] else [Değer_False_İse]

print("\n--- 5. TEK SATIRDA IF KULLANIMI ---\n")

bakiye = 50
urun_fiyati = 80

# Uzun yazım yerine:
durum = "Satın Alındı" if bakiye >= urun_fiyati else "Bakiye Yetersiz"

print(f"İşlem Durumu: {durum}")