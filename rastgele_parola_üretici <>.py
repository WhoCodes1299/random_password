"""
string.ascii_letters = ascii_lowercase ve ascii_uppercase string sabitlerinin değerlerini gösterir.
string.printable = basılabilen tüm ASCII karakterleri içeren stringi döndürür.
string.whitespace = boşluk bırakan tüm çıkış (escape) karakterlerinden oluşan stringi üretir.
string.capwords(s) = s stringindeki kelimelerin (words) baş harflerini büyük harfe dönüştürür.
"""

import string
import random

s1 = string.ascii_lowercase  # küçük harf
s2 = string.ascii_uppercase  # büyük harf
s3 = string.punctuation  # özel karakterler
s4 = string.digits  # rakam


pUz = int(input("Parola Length: "))

s = []  # boş liste tanımı

s.extend(list(s1))  # s1'i listeye dönüştür ve s listesine ekle
s.extend(list(s2))  # s listesini s2 ile genişlet
s.extend(list(s3))  # s listesini s3 ile genişlet

print("Generated Password - 1: ")  # pUz değeri kadar örnek al

print("".join(random.sample(s, pUz)))  # tüm basılabilen karakterlerden oluşur.

print("Generated Password - 2: ")

s5 = string.printable

print("".join(random.sample(s5, pUz)))