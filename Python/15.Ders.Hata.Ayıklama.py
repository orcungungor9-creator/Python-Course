# Python Temelleri -15- Hata Yakalama (Exception Handling)

# Programlarımızı yazarken bazen bizim kontrolümüz dışında (kullanıcının yanlış veri girmesi, 
# dosyanın bulunamaması, internetin kopması gibi) durumlarda hatalar oluşabilir.
# Python'da bir hata (Exception) meydana geldiğinde program aniden çöker (crash) ve çalışmayı durdurur.
# "Hata Yakalama" mekanizmaları (try-except) sayesinde, programın çökmesini engeller 
# ve hata durumlarında ne yapılması gerektiğini Python'a söyleyebiliriz.

# --------------------------------------------------------
# 1. BÖLÜM: TEMEL TRY - EXCEPT YAPISI
# --------------------------------------------------------

print("--- 1. TEMEL TRY-EXCEPT KULLANIMI ---\n")

# try bloğu: Hata çıkarma potansiyeli (riski) olan kodları buraya yazarız.
# except bloğu: Eğer try içindeki kodda BİR HATA ÇIKARSA, program çökmek yerine bu bloğa atlar.

try:
    print("Riskli işlem deneniyor...")
    # int() fonksiyonu harfleri sayıya çeviremez. Bu satır normalde ValueError verip programı çökertir.
    hatali_sayi = int("on beş") 
    print("Bu satır asla çalışmayacak çünkü üstte hata oldu!")
except:
    # Hata oluştuğunda program çökmek yerine kullanıcıya dostça bir mesaj verir.
    print("HATA YAKALANDI: Girilen veri bir tam sayıya çevrilemedi!")

print("\nProgram çökmediği için bu satır sorunsuz çalışmaya devam ediyor.\n")

# --------------------------------------------------------
# 2. BÖLÜM: ÖZEL HATA TÜRLERİNİ (SPESİFİK) YAKALAMA
# --------------------------------------------------------

# Her hatayı tek bir 'except' ile yakalamak iyi bir pratik değildir.
# Hatanın türüne göre (Örn: Sıfıra bölme hatası, Yanlış değer hatası) farklı tepkiler vermeliyiz.

print("--- 2. SPESİFİK HATALARI YAKALAMA ---\n")

bolunen = 100
bolen = 0 # Bir sayı sıfıra bölünemez! (ZeroDivisionError)

try:
    sonuc = bolunen / bolen
    print(f"Bölme İşlemi Sonucu: {sonuc}")
except ZeroDivisionError:
    # Sadece sıfıra bölme hatası olursa burası çalışır.
    print("MATEMATİK HATASI: Herhangi bir sayı 0'a bölünemez!")
except TypeError:
    # Sadece yanlış veri tipiyle işlem yapılmaya çalışılırsa burası çalışır (Örn: "Elma" / 5).
    print("TİP HATASI: Matematiksel işlemler sadece sayılarla yapılabilir!")
except Exception as e:
    # Yukarıdakiler dışındaki TıM bilinmeyen hataları yakalar. Hatanın sistemdeki adını 'e' değişkenine atar.
    print(f"BİLİNMEYEN BİR HATA OLUŞTU. Hata detayı: {e}")

# --------------------------------------------------------
# 3. BÖLÜM: ELSE VE FINALLY BLOKLARI
# --------------------------------------------------------

# try ve except'e ek olarak iki opsiyonel bloğumuz daha vardır:
# else    : Eğer try bloğunda HİÇBİR HATA ÇIKMAZSA çalışır.
# finally : Hata çıksa da çıkmasa da EN SONUNDA MUTLAKA çalışır. Genelde açık dosyaları/veritabanlarını kapatmak için kullanılır.

print("\n--- 3. ELSE VE FINALLY KULLANIMI ---\n")

try:
    print("Analiz için veritabanına bağlanılıyor...")
    # Burada başarılı bir işlem simüle ediyoruz.
    veri_sayisi = 1500
except ValueError:
    print("Veri okuma hatası oluştu!")
else:
    # Hata olmadığı için bu blok çalışacak.
    print(f"BAŞARILI: Veritabanından toplam {veri_sayisi} satır veri çekildi.")
finally:
    # Her senaryoda çalışıp sistemi temizleyecek kısım.
    print("KAPANIŞ: Veritabanı bağlantısı güvenli bir şekilde sonlandırıldı.")

# --------------------------------------------------------
# 4. BÖLÜM: BİLİNÇLİ HATA FIRLATMA (RAISE)
# --------------------------------------------------------

# Bazen kodumuz teknik olarak doğru (hata vermeyen) bir kod olsa bile, 
# bizim kurduğumuz iş mantığına ters düşen durumlarda manuel olarak hata fırlatmak isteyebiliriz.

print("\n--- 4. BİLİNÇLİ HATA FIRLATMA (RAISE) ---\n")

def yas_dogrula(yas):
    if yas < 0:
        # Sistem negatif yaşı tam sayı olarak algılar ama insan yaşı negatif olamaz!
        # Burada kendi kuralımız için bilinçli bir ValueError fırlatıyoruz.
        raise ValueError("Yaş değeri sıfırdan küçük (negatif) olamaz!")
    else:
        print(f"Doğrulanan Yaş: {yas}")

try:
    yas_dogrula(-5)
except ValueError as hata_mesaji:
    print(f"SİSTEM UYARISI: {hata_mesaji}")