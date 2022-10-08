# Toplama Fonksiyonu

def Topla(x, y):
    return x + y


# Çıkarma Fonksiyonu

def Topla(x, y):
    return x - y


# Çarpma Fonksiyonu

def Topla(x, y):
    return x * y


# Bölme Fonksiyonu

def Topla(x, y):
    return x / y


sayi1 = int(input("1.Sayı : "))

print("Yapılacak İşlemi Seçiniz.")
print("=========================")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")


# Kullanıcıdan Seçim İste

secim = input("Yapmak İstedğiniz İşlemi Seçiniz :")
sayi2 = int(input("2.Sayı : "))


if secim == '1':

    topla = sayi1 + sayi2
    print(sayi1, " + ", sayi2, " = ", topla)

elif secim == '2':

    topla = sayi1 - sayi2
    print(sayi1, " - ", sayi2, " = ", topla)

elif secim == '3':

    topla = sayi1 * sayi2
    print(sayi1, " * ", sayi2, " = ", topla)

elif secim == '4':

    topla = sayi1 / sayi2
    print(sayi1, " / ", sayi2, " = ", topla)

else:
    print("Geçersiz Seçim..")
