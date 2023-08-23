# for loop sikli

#--------------------------------------

names = ['Hasan', 'Husan', 'Ali', 'Vali', 'Karim']
user_count = 0
for name in names:
    print(f"Assalomu alaykum, {name}")
    user_count += 1
print(f"Kod {user_count} marta takrorlandi")

#--------------------------------------

odd_numbers = []
for number in range(10, 100):
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)

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