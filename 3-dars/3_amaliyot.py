# String va uning metodlari

#----------------------------------------

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

#----------------------------------------

print(kocha, "ko'chasi,", mahalla, "mahallasi,", tuman, "tumani,", viloyat, "viloyati")

#----------------------------------------

kocha = input("Ko'cha: ")
mahalla = input("Mahalla: ")
tuman = input("Tuman: ")
viloyat = input("Viloyat: ")

#-----------------------------------------

print(kocha, "ko'chasi,\n", mahalla, "mahallasi,\n", tuman, "tumani,\n", viloyat, "viloyati")

#-----------------------------------------

manzil = f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati"
print(manzil)

#-----------------------------------------

print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())

#----------------------------------------

