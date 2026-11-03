# Python Temelleri -14- Fonksiyonlar (Functions)

# Fonksiyonlar, belirli bir görevi yerine getirmek için yazılmış,
# tekrar tekrar kullanılabilen isimlendirilmiş kod bloklarıdır.
# Karmaşık programları daha küçük, yönetilebilir ve okunabilir parçalara böler.
# Python'da fonksiyon tanımlamak için 'def' (define) anahtar kelimesi kullanılır.

# --------------------------------------------------------
# 1. BÖLÜM: FONKSİYON TANIMLAMA VE ÇAĞIRMA
# --------------------------------------------------------

print("--- 1. FONKSİYON TANIMLAMA ---\n")

# Parametre almayan basit bir fonksiyon tanımlayalım:
# İki nokta üst üste (:) sonrası içeriden (girintili) yazılan her şey bu fonksiyona aittir.
def karsilama_mesaji():
    print("Sisteme hoş geldiniz!")
    print("Bugün harika işler başaracağız.\n")

# Fonksiyonu tanımlamak onun çalışması için yeterli değildir.
# Çalışması için fonksiyonu ismiyle "çağırmamız" (call) gerekir.
karsilama_mesaji()
karsilama_mesaji() # İstediğimiz kadar çağırabiliriz, kod tekrarından kurtulduk!

# --------------------------------------------------------
# 2. BÖLÜM: PARAMETRE VE ARGÜMAN KULLANIMI
# --------------------------------------------------------

# Fonksiyonlara dışarıdan dinamik veriler gönderebiliriz. 
# Fonksiyonu tanımlarken yazdığımız değişkenlere "parametre" denir.

print("--- 2. PARAMETRELİ FONKSİYONLAR ---\n")

def platforma_giris(kullanici_adi, platform_ismi):
    print(f"Merhaba {kullanici_adi}, {platform_ismi} sistemine giriş yaptın!")

# Fonksiyonu çağırırken parantez içine gönderdiğimiz gerçek değerlere ise "argüman" denir.
platforma_giris("Orçun", "Analyst Roadmap")
platforma_giris("Ayşe", "Veri Analizi Portalı")

# --------------------------------------------------------
# 3. BÖLÜM: RETURN (DEĞER DÖNDÜRME) İFADESİ
# --------------------------------------------------------

# print() sadece ekrana yazı yazdırır, ürettiği sonucu programın ilerleyen kısımlarında kullanamayız.
# return ifadesi ise fonksiyonun ürettiği sonucu bize geri verir (döndürür),
# böylece bu sonucu bir değişkene atayıp başka hesaplamalarda kullanabiliriz.

print("\n--- 3. RETURN İLE DEĞER DÖNDÜRME ---\n")

# Analitik bir hesaplamada sıkça kullandığımız basit bir ortalama alma fonksiyonu:
def ortalama_hesapla(sayi1, sayi2, sayi3):
    toplam = sayi1 + sayi2 + sayi3
    ortalama = toplam / 3
    return ortalama # Hesaplanan değeri dışarı aktarır ve fonksiyon burada BİTER.

# Fonksiyondan dönen değeri 'sonuc' değişkenine kaydediyoruz.
sonuc = ortalama_hesapla(85, 90, 75)
print(f"Verilerin Ortalaması: {sonuc}")

# Döndürülen değeri başka bir işlemde rahatça kullanabiliriz:
if sonuc >= 80:
    print("Performans durumu: Yüksek")

# --------------------------------------------------------
# 4. BÖLÜM: VARSAYILAN (DEFAULT) PARAMETRELER
# --------------------------------------------------------

# Kullanıcı bir parametre girmezse, fonksiyonun hata vermek yerine 
# bizim belirlediğimiz varsayılan bir değeri kullanmasını sağlayabiliriz.

print("\n--- 4. VARSAYILAN PARAMETRELER ---\n")

# algoritma parametresine varsayılan bir değer atadık:
def model_olustur(bagimsiz_degisken_sayisi, algoritma="Lineer Regresyon"):
    print(f"Seçilen Model: {algoritma}")
    print(f"Değişken Sayısı: {bagimsiz_degisken_sayisi}\n")

# Sadece zorunlu olan 1. argümanı verirsek, algoritma için varsayılanı kullanır:
print("2. argüman verilmediğinde:")
model_olustur(5)

# İki argümanı da verirsek bizim verdiğimiz değer varsayılanı ezer:
print("İki argüman da verildiğinde:")
model_olustur(3, "Lojistik Regresyon")

# --------------------------------------------------------
# 5. BÖLÜM: DOCSTRING (FONKSİYON BELGESİ)
# --------------------------------------------------------

# Fonksiyonların ne işe yaradığını açıklamak için hemen altına üç tırnak (""") ile docstring yazılır.
# Büyük projelerde, kendi yazdığınız aracı aylar sonra okurken veya başka analistlerle çalışırken kritik bir standarttır.

def veri_temizle(veri_listesi):
    """
    Bu fonksiyon, verilen listedeki eksik verileri (None) tespit eder
    ve onları listeden çıkartarak temizlenmiş yeni bir liste döndürür.
    """
    temiz_liste = []
    for eleman in veri_listesi:
        if eleman is not None:
            temiz_liste.append(eleman)
    return temiz_liste

ornek_veri = [10, 25, None, 40, None, 50]

print("--- 5. DOCSTRING VE UYGULAMA ---\n")
print(f"Ham Veri Listesi : {ornek_veri}")
print(f"Temizlenmiş Veri : {veri_temizle(ornek_veri)}")