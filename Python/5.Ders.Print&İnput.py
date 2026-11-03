# Python Temelleri -5- Print ve Input Fonksiyonları

# Bu derste Python'da kullanıcı ile etkileşime geçmemizi sağlayan iki temel fonksiyonun detaylarını inceleyeceğiz:
# 1. print() : Ekrana çıktı (mesaj/veri) yazdırmak için kullanılır.
# 2. input() : Kullanıcıdan klavye aracılığıyla veri (girdi) almak için kullanılır.

# --------------------------------------------------------
# 1. BÖLÜM: PRINT() FONKSİYONUNUN DETAYLARI VE PARAMETRELERİ
# --------------------------------------------------------

# Standart kullanım:
print("Merhaba, Python eğitimine hoş geldin!")

# Birden fazla değeri aralarına virgül koyarak aynı satırda yazdırabiliriz:
dil = "Python"
seviye = "Temel"
print("Öğrenilen Dil:", dil, "Seviye:", seviye)

# sep (Ayırıcı) Parametresi: Virgülle ayrılan değerlerin arasına ne konulacağını belirler.
# Varsayılan değeri bir adet boşluktur (" ").
print("Gün", "Ay", "Yıl", sep="/") 
print("Veri", "Analizi", "Dersleri", sep="-")

# end (Sonlandırma) Parametresi: print işlemi bitince cümlenin sonuna ne ekleneceğini belirler.
# Varsayılan değeri alt satıra geçme karakteridir ("\n").
print("Bu cümle bitince alt satıra geçmeyecek.", end=" ---> ")
print("Buradan devam edecek!")

# f-string (Formatlı string): Metinlerin içine değişkenleri doğrudan gömmek için en pratik yöntem.
puan = 95
print(f"Seçilen dil {dil}, sınav puanı ise {puan}.")

# --------------------------------------------------------
# 2. BÖLÜM: INPUT() FONKSİYONU İLE KULLANICI ETKİLEŞİMİ
# --------------------------------------------------------

# Kullanıcıya bir soru sorup cevabını bir değişkende saklarız.
# KURAL REHBERİ: Bir önceki derste gördüğümüz gibi input() her zaman veriyi 'str' (metin) olarak getirir!

print("\n--- KULLANICI BİLGİ SİSTEMİ ---\n")
kullanici_sehir = input("Hangi şehirde yaşıyorsunuz?: ")
print(f"Ne güzel, {kullanici_sehir} harika bir şehirdir!")

# --------------------------------------------------------
# 3. BÖLÜM: INPUT VE TİP DÖNÜŞÜMÜ (TYPE CASTING) İLE MATEMATİK
# --------------------------------------------------------

# Eğer kullanıcıdan sayısal bir değer istiyorsak, gelen metni sayıya çevirmeliyiz (int veya float).

print("\n--- MİNİ YAŞ HESAPLAMA UYGULAMASI ---\n")
# Gelen string değeri int() ile tam sayıya çeviriyoruz.
dogum_yili = int(input("Lütfen doğum yılınızı giriniz (Örn: 1995): "))
guncel_yil = 2026

# Artık dogum_yili bir tam sayı (int) olduğu için matematiksel çıkarma işlemi yapabiliriz.
hesaplanan_yas = guncel_yil - dogum_yili

print(f"Siz {hesaplanan_yas} yaşındasınız!")

print("\n--- MİNİ HESAP MAKİNESİ ---\n")
# Gelen string değeri float() ile ondalıklı sayıya çeviriyoruz.
sayi1 = float(input("Lütfen ondalıklı veya tam bir sayı girin (Örn: 5.5): "))
sayi2 = float(input("Lütfen ikinci sayıyı girin: "))

toplam = sayi1 + sayi2
print(f"Girdiğiniz {sayi1} ve {sayi2} sayılarının toplamı = {toplam}")