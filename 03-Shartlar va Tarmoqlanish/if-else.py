# Shartlar va Tarmoqlanish 

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

#--------------------------------------------------

for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

#--------------------------------------------------

login = input("Login: ")

if login.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yhatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}")

#-------------------------------------------------

num1 = float(input("Birinchi sonni kiriting: "))
num2 = float(input("Ikkinchi sonni kiriting: "))

if num1 == num2: print("Sonlar teng!")

#--------------------------------------------------

number = float(input("Son kiriting: "))

print("Musbat son") if number > 0 else print("Manfiy son")

#--------------------------------------------------

number = float(input("Son kiriting: "))
print(number ** (1/2)) if number > 0 else print("Musbat son kiriting!")

#--------------------------------------------------

yosh = int(input("Yoshingizni kiriting: "))

if yosh <= 4:
    print("Kirish bepul")
elif yosh <= 12:
    print("Kirish 5000 ming so'm")
else:
    print("Kirish 10000 ming so'm")
