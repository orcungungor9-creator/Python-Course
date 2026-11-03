# Python Temelleri -4- Temel Veri Tipleri ve İnput

# Günlük programlamada en sık kullanılan temel 5 veri tipi:
# 1. str   : Metinler (Karakter dizileri)
# 2. int   : Tam sayılar
# 3. float : Ondalıklı sayılar
# 4. bool  : Mantıksal değerler (True / False)
# 5. list  : Listeler (Birden çok veriyi sıralı tutan yapılar)

# --------------------------------------------------------
# 1. BÖLÜM: DEĞİŞKENLERE TEMEL 5 VERİ TİPİNİ ATAMA
# --------------------------------------------------------

metin_veri     = "Python Öğreniyorum"      # str
tam_sayi_veri  = 10                        # int
ondalikli_veri = 3.14                      # float
mantiksal_veri = True                      # bool
liste_veri     = [1, 2, "Elma", True]      # list

# --------------------------------------------------------
# 2. BÖLÜM: DEĞİŞKENLERİ VE TİPLERİNİ YAZDIRMA
# --------------------------------------------------------

print("--- EN TEMEL 5 VERİ TİPİ ---\n")

print(f"1. str   (Metin)     : {metin_veri} \t Tipi: {type(metin_veri)}")
print(f"2. int   (Tam Sayı)  : {tam_sayi_veri} \t\t\t Tipi: {type(tam_sayi_veri)}")
print(f"3. float (Ondalıklı) : {ondalikli_veri} \t\t\t Tipi: {type(ondalikli_veri)}")
print(f"4. bool  (Mantıksal) : {mantiksal_veri} \t\t\t Tipi: {type(mantiksal_veri)}")
print(f"5. list  (Liste)     : {liste_veri} \t Tipi: {type(liste_veri)}")

# --------------------------------------------------------
# 3. BÖLÜM: KULLANICIDAN VERİ ALMA (INPUT)
# --------------------------------------------------------

# Python'da kullanıcıdan veri almak için input() fonksiyonu kullanılır.
# ÖNEMLİ KURAL: input() fonksiyonundan gelen her veri, varsayılan olarak "str" (metin) tipindedir.
# Matematiksel işlem yapabilmek için tip dönüşümü (Type Casting) yapmamız gerekir.

print("\n--- KULLANICIDAN VERİ ALMA ---\n")

# 1. Standart Kullanım (Metin olarak alır)
isim = input("Lütfen adınızı giriniz: ")

# 2. Tam Sayı (int) Olarak Veri Alma
# Kullanıcının girdiği metni int() fonksiyonu ile tam sayıya çeviriyoruz.
yas = int(input("Lütfen yaşınızı giriniz: "))

# 3. Ondalıklı Sayı (float) Olarak Veri Alma
# Kullanıcının girdiği metni float() fonksiyonu ile ondalıklı sayıya çeviriyoruz.
boy = float(input("Lütfen boyunuzu metre cinsinden giriniz (Örn: 1.75): "))

# Alınan verileri ve dönüşmüş tiplerini ekrana yazdıralım:
print("\n--- GİRİLEN VERİLER VE YENİ TİPLERİ ---")
print(f"Merhaba {isim}, sisteme hoş geldin! \t Tipi: {type(isim)}")
print(f"Yaşınız: {yas} \t\t\t\t Tipi: {type(yas)}")
print(f"Boyunuz: {boy} \t\t\t\t Tipi: {type(boy)}")