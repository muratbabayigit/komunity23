'''
Kullanicidan gun ismini alin ve haftaici veya hafta sonu oldugunu yazdirin
       Ornek:  gun=Pazar output = “Hafta sonu”  gun=Sali output = “Hafta ici”
'''

# and operatörü:  iki koşulunda aynı anda doğru olması gerektiğinde kullanılır
# or operatörü: iki koşuldan sadece biri doğru olduğunda kullanılır

gun=input("Lütfen bugün hangi gün yazınız: ")
print(gun.lower())
if gun.lower()=="pazar" or gun.lower()=="cumartesi":
    print("Bugün",gun," ve hafta sonu bir gün")
else:
    print("Bugün",gun," ve hafta içi bir gün")