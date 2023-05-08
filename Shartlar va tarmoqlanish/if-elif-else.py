# IF-elif-else tarmoqlanish

#1-topshiriq
son = float(input("Son kiriting: "))
if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas")

#2-topshiriq
yosh = int(input("Yoshingizni kiriting: "))
if yosh < 4 or yosh > 60:
    price = 0
elif yosh < 18:
    price = 10000
else:
    price = 20000
print(f"Sizga kirish {price} so'm")    

#3-topshiriq
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")

#4-topshiriq
mahsulotlar = ['anor', 'uzum', 'olma', 'nok', 'banan', 'limon', 'shaftoli', 'ananas']
savat = []
for i in range(5):
    savat.append(input(f"Savatga {i+1} mahsulotni qo'shing: "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")

#5-topshiriq
mahsulotlar = ['anor', 'uzum', 'olma', 'nok', 'banan', 'limon', 'shaftoli', 'ananas']
savat = []
bor_mahsulotlar = []
mavjud_emas = []

for i in range(5):
    savat.append(input(f"Savatga {i+1} mahsulotni qo'shing: "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for i in mavjud_emas:
        print(i)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#6-topshiriq
foydalanuvchilar = ['anvar', 'nurmuhammad', 'javohir', 'fayzullo', 'muhtorjon', 'abdulaziz']
username = input("Foydalanuvchi nomi: ")
if username.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {username}")

#7-topshiriq
son = float(input("Son kiriting: "))
for i in range(2, 11):
    if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")