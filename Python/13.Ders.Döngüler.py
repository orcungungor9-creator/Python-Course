# Python Temelleri -13- Döngüler (Loops - For / While)

# Döngüler, belirli bir kod bloğunu tekrar tekrar çalıştırmamızı sağlayan yapılardır.
# Aynı işlemi defalarca yazmak yerine (DRY - Don't Repeat Yourself / Kendini Tekrar Etme prensibi),
# döngüleri kullanarak kodumuzu kısa, dinamik ve okunabilir hale getiririz.
# Python'da temel olarak iki çeşit döngü vardır: 'for' ve 'while'.

# --------------------------------------------------------
# 1. BÖLÜM: FOR DÖNGÜSÜ VE KOLEKSİYONLAR ÜZERİNDE GEZİNME
# --------------------------------------------------------

# 'for' döngüsü, genellikle eleman sayısı belli olan veri yapılarının (liste, tuple, string, sözlük)
# içinde sırasıyla gezinmek (iterasyon) için kullanılır.

ogrenciler = ["Ali", "Ayşe", "Mehmet", "Zeynep"]

print("--- 1. FOR DÖNGÜSÜ İLE LİSTELERDE GEZİNME ---\n")

# ogrenciler listesindeki her bir eleman sırasıyla 'isim' değişkenine atanır ve içerideki kod çalıştırılır.
for isim in ogrenciler:
    print(f"Öğrenci: {isim}")

print("\n--- STRING (METİN) ÜZERİNDE GEZİNME ---\n")
# Stringler de birer karakter dizisi olduğu için for ile harf harf gezilebilir.
kelime = "Python"
for harf in kelime:
    print(harf)

# --------------------------------------------------------
# 2. BÖLÜM: RANGE() FONKSİYONU İLE FOR DÖNGÜSÜ
# --------------------------------------------------------

# Belirli bir sayıda tekrar yapmasını istediğimiz durumlar için range() fonksiyonu kullanılır.
# range(başlangıç, bitiş, adım_miktarı) şeklinde çalışır. Bitiş değeri dahil DEĞİLDİR!

print("\n--- 2. RANGE() FONKSİYONU ---\n")

# Sadece bitiş değeri verilirse 0'dan başlar (5 dahil değil).
print("range(5) çıktısı:")
for i in range(5):
    print(i, end=" ") # Yan yana yazdırmak için end=" " kullandık.

print("\n\nrange(1, 10, 2) çıktısı (1'den 10'a ikişer):")
for i in range(1, 10, 2):
    print(i, end=" ")

print("\n")

# --------------------------------------------------------
# 3. BÖLÜM: WHILE DÖNGÜSÜ
# --------------------------------------------------------

# 'while' döngüsü, kendisine verilen koşul DOĞRU (True) olduğu sürece çalışmaya devam eder.
# Koşulun bir noktada YANLIŞ (False) olmasını sağlamazsak döngü sonsuza kadar çalışır (Sonsuz Döngü hatası).

print("\n--- 3. WHILE DÖNGÜSÜ ---\n")

sayac = 1

# sayac 5'ten küçük veya eşit olduğu SÜRECE bu blok çalışacak.
while sayac <= 5:
    print(f"Sayaç şu an: {sayac}")
    
    # DİKKAT: Sayacı artırmayı unutursak sonsuz döngüye gireriz!
    sayac += 1 # sayac = sayac + 1 ile aynı anlama gelir.

print("Döngü bitti, sayacın son değeri:", sayac)

# --------------------------------------------------------
# 4. BÖLÜM: DÖNGÜ KONTROL İFADELERİ (BREAK VE CONTINUE)
# --------------------------------------------------------

# Bazen döngülerin normal akışına müdahale etmemiz gerekir.
# break    : Döngüyü anında tamamen sonlandırır ve dışarı çıkar.
# continue : Sadece o anki adımı atlar (pas geçer) ve döngüye sıradaki adımdan devam eder.

print("\n--- 4. BREAK VE CONTINUE İFADELERİ ---\n")

sayilar = [10, 20, 30, 40, 50, 60]

print("BREAK ÖRNEĞİ (30'u görünce dur):")
for sayi in sayilar:
    if sayi == 30:
        print("30 bulundu, döngüden çıkılıyor!")
        break # 30'u görünce döngü tamamen biter, 40,50,60'a bakmaz.
    print("Sayı:", sayi)


print("\nCONTINUE ÖRNEĞİ (Sadece 30'u atla, devam et):")
for sayi in sayilar:
    if sayi == 30:
        print("30 bulundu, bu adım pas geçiliyor!")
        continue # 30 için alttaki kodları çalıştırmaz, başa döner ve 40'tan devam eder.
    print("Sayı:", sayi)