db_pass=134679
us_pass=int(input("Sifrenizi Giriniz: "))


yas_sinir=18
user_age=int(input("Yasinizi Giriniz: "))
yas_check= user_age>=yas_sinir or db_pass==us_pass
#yas_check= user_age>=yas_sinir and db_pass==us_pass
print(yas_check)


