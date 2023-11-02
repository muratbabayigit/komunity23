# If türkçe karşılığı olan eğer kelimesinden de hatırlanabileceği üzere bazı koşul durumlarına göre
# cevaplar veren ya da işlemler yapan durumdur.
# Bu koşul durumlarının kullanımında if,elif ve else kullanılır.
# if ile belirtilen koşul sağlanırsa o işlem yapılır
# elif ise if ile olmayan ama başka bir koşulun olmasına bağlı ise kullanılır
# else tüm olası durumların olmadığı durumlarda kullanılır

'''
Soru: Markete gelen kişiye yaşını soran ve 18  yaşından küçük ise
Sigara satışı yapılamayacağınıız, büyükse satın alabilirsiniz diye söyleyen kodu yazın
'''

print("==== Sanal Marketimize Hoş Geldiniz ====")
print("........................................................")
yas=int(input("Lütfen Yaşınızı Giriniz: "))


if yas>18:
    print("Satın Alabilirsiniz")
else:
    print("Yaşınız ",yas, "olduğu için satın alamazsınız")