# for loop sikli

#--------------------------------------

ismlar = ['Hasan', 'Husan', 'Ali', 'Vali', 'Karim']
n = 0
for ism in ismlar:
    print(f"Assalomu alaykum, {ism}")
    n += 1
print(f"Kod {n} marta takrorlandi")

#--------------------------------------

toq_sonlar = []
for son in range(10, 100):
    if son % 2 != 0:
        toq_sonlar.append(son)
print(toq_sonlar)

#--------------------------------------

kinolar = []
for i in range(5):
    kinolar.append(input(f"{i+1}-sevimli kinongizni kiriting: "))
print(kinolar)

#--------------------------------------

suhbatdoshlar = []
n = int(input("Nechta odam bilan suhbatlashdingiz: "))
for i in range(n):
    suhbatdoshlar.append(input(f"{i+1}-suhbatdoshingiz ismini kiriting: "))
print(suhbatdoshlar)

#--------------------------------------