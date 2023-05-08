# If-Else tarmoqlanish

#1-topshiriq

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#1-usul
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
#2-usul
for car in cars:
    print(car.upper()) if car == 'gm' else print(car.title())

#2-topshiriq
for car in cars:
    print(car.title()) if car != 'gm' else print(car.upper())

#3-topshiriq
username = input("Ism: ")
if username == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")  
else:
    print(f"Xush kelibsiz, {username}!")

#4-topshiriq
a = float(input("1-son: "))
b = float(input("2-son: "))
if a == b:
    print("Sonlar teng!")
else:
    print("Sonlar bir-biridan farq qiladi!")

#5-topshiriq
son = float(input("Son kiriting: "))
if son > 0:
    print("Musbat son")
elif son < 0:
    print("Manfiy son")
else:
    print("Son nolga teng")

#6-topshiriq
son = float(input("Son kiriting: "))
if son >= 0:
    print(son**(1/2))
else:
    print("Musbat son kiriting!")

