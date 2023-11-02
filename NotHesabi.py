'''
SORU:
Öğrenci notunu harf notuna dönüştüren bir kod yazınız
        85-100 -----> AA
        80-85 ------> BA
        75-80 ------> BB
        65-75 ------> CB
        50-65 ------> CC
        50 Altı ise  ------> FF
'''

print("---- NOT - HARF DÖNÜŞÜM UYGULAMASI ----")
notu = int(input("Notunuzu tamsayı olarak giriniz: "))

if notu>=85 and notu<100:
    harf_notu="AA"
elif notu>=80 and notu<85:
    harf_notu="BA"
elif notu>=75 and notu<80:
    harf_notu="BB"
elif notu>=65 and notu<75:
    harf_notu="CB"
elif notu>=50 and notu<65:
    harf_notu="CC"
else:
    harf_notu="FF"
print(f"Girdiğiniz notun Karşılığı olan harf notu: :{harf_notu}")
