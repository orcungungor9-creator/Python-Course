# Python Temelleri -2- Matematiksel Operatorler

# Python'da matematiksel işlemler için çeşitli operatörler kullanılır.
# Bu operatörler, sayılar üzerinde toplama, çıkarma, çarpma, bölme ve diğer matematiksel işlemleri gerçekleştirmek için kullanılır.
# Aşağıda, Python'da kullanılan temel matematiksel operatörler ve örnek kullanımları gösterilmektedir.
# Degiskenler ve operatörler kullanılarak yapılan işlemler, programlama mantığını anlamak için önemlidir.
# Işlem önceliği ve parantez kullanımı, karmaşık matematiksel ifadelerin doğru bir şekilde hesaplanmasını sağlar.
# Islem sonucumuz tam sayi bile olsa , bölme işlemi her zaman float tipinde sonuç döndürür. 
# Bu nedenle, tam sayı bölmesi için // operatörü kullanılır.  


a = 10 # Bir tam sayı (integer) değişkeni
b = 3  # Bir tam sayı (integer) değişkeni

print("Python'da Matematiksel Operatörler Kullanımı")


#--------------------------------------------------------
print("--- Temel Operatörler ---")

# Toplama
print("Toplama (a + b):", a + b)       
# Çıkarma
print("Çıkarma (a - b):", a - b)       
# Çarpma
print("Çarpma (a * b):", a * b)        
# Bölme (Sonuç her zaman float döner)
print("Bölme (a / b):", a / b)         


# --------------------------------------------------------
print("\n--- Gelişmiş Operatörler ---")

# Tam Sayı Bölmesi (Küsüratı atar, tam kısmı alır)
print("Tam Sayı Bölmesi (a // b):", a // b)  
# Mod Alma (Bölümden kalanı bulur)
print("Mod Alma (a % b):", a % b)      
# Üs Alma (a'nın b kuvvetini alır)
print("Üs Alma (a ** b):", a ** b)     


#--------------------------------------------------------
print("\n--- Kısa Atama (Kısaltılmış) Operatörleri ---")

x = 5
print("Başlangıç değeri x:", x)
x += 5  # x = x + 5 işleminin kısaltmasıdır
print("x += 5 sonrası yeni x:", x)
x *= 2  # x = x * 2 işleminin kısaltmasıdır
print("x *= 2 sonrası yeni x:", x)