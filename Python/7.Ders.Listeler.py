# Python Temelleri -7- Listeler (Lists)

# Listeler (list), birden fazla veriyi tek bir değişkende sıralı bir şekilde tutmamızı sağlar.
# Köşeli parantezler [] kullanılarak oluşturulur ve elemanlar virgül ile ayrılır.
# Stringlerin (metinlerin) aksine, listeler "değiştirilebilir" (mutable) yapıdadır; 
# yani oluşturulduktan sonra içindeki elemanları güncelleyebilir, silebilir veya yeni eleman ekleyebiliriz.

# --------------------------------------------------------
# 1. BÖLÜM: LİSTE TANIMLAMA VE FARKLI VERİ TİPLERİ
# --------------------------------------------------------

# Bir liste aynı tipte veya tamamen farklı tipte veriler barındırabilir.
sayilar = [10, 20, 30, 40, 50]
isimler = ["Ali", "Ayşe", "Mehmet"]
karisik_liste = [1, "Python", 3.14, True, [5, 6]] # Listenin içinde başka bir liste bile olabilir!

print("--- LİSTE OLUŞTURMA VE UZUNLUK (LEN) ---\n")
print(f"Sayılar listesi : {sayilar}")
print(f"İsimler listesi : {isimler}")
print(f"Karışık liste   : {karisik_liste}")

# len() fonksiyonu karakter dizilerinde olduğu gibi listelerde de eleman sayısını verir.
print(f"\nSayılar listesinde {len(sayilar)} adet eleman var.")

# --------------------------------------------------------
# 2. BÖLÜM: İNDEKSLEME, DİLİMLEME VE ELEMAN DEĞİŞTİRME
# --------------------------------------------------------

# Listelerde de indeksleme 0'dan başlar.
programlama_dilleri = ["Python", "Java", "C++", "R", "SQL"]

print("\n--- İNDEKSLEME VE ELEMAN GÜNCELLEME ---\n")
print("İlk dil       :", programlama_dilleri[0])
print("Son dil       :", programlama_dilleri[-1])
print("İlk 3 dil     :", programlama_dilleri[0:3]) # Dilimleme (Slicing)

# Listelerin değiştirilebilir (mutable) olduğunu söylemiştik. 
# İndeks belirterek mevcut bir elemanı başka bir değerle değiştirebiliriz.
print("\nGüncellemeden önce:", programlama_dilleri)
programlama_dilleri[1] = "JavaScript" # 1. indeksteki "Java"yı "JavaScript" yaptık
print("Güncelledikten sonra:", programlama_dilleri)

# --------------------------------------------------------
# 3. BÖLÜM: EN SIK KULLANILAN LİSTE METODLARI
# --------------------------------------------------------

sepet = ["Elma", "Armut", "Muz"]

print("\n--- LİSTE METODLARI ---\n")

# 1. append(yeni_eleman): Listenin en sonuna yeni bir eleman ekler.
sepet.append("Çilek")
print("append('Çilek') sonrası :", sepet)

# 2. insert(indeks, yeni_eleman): Belirtilen indekse yeni eleman ekler, diğerlerini sağa kaydırır.
sepet.insert(1, "Kavun") # 1. indekse ekle
print("insert(1, 'Kavun')      :", sepet)

# 3. remove(eleman): Belirtilen değere sahip ilk elemanı listeden siler.
sepet.remove("Armut")
print("remove('Armut') sonrası :", sepet)

# 4. pop(indeks): Belirtilen indeksteki elemanı siler ve sildiği değeri bize döndürür.
# İndeks yazılmazsa listenin en sonundaki elemanı siler.
silinen_meyve = sepet.pop() # En sondaki "Çilek" silinir
print(f"pop() ile silinen       : {silinen_meyve}")
print("pop() sonrası sepet     :", sepet)

# 5. sort(): Listenin elemanlarını küçükten büyüğe (veya alfabetik olarak) sıralar.
# reverse() metodu veya reverse=True parametresi ile tersten sıralama yapılabilir.
rakamlar = [8, 1, 5, 2, 9]
rakamlar.sort()
print("\nsort() ile sıralanmış rakamlar :", rakamlar)

rakamlar.sort(reverse=True) # Büyükten küçüğe sıralar
print("Büyükten küçüğe sıralanmış     :", rakamlar)