# for loop

ismlar = ['Javohir','Fayzullo', 'Muhtorjon', 'Abdulaziz', 'Nurmuhammad']
i = 0
for ism in ismlar:
    print(f"Assalomu alaykum {ism}")
    i += 1
print(f"Kod {i} marta takrorlandi")

sonlar = list(range(10,101))
for son in sonlar:
    print(son)
    
kinolar = []
print("5 ta eng sevimli kinongizni kiriting:")
for i in range(5):
    kinolar.append(input(f"{i + 1}-kinongizni kiriting: "))
print(kinolar)

odamlar = []
n = int(input("Bugun nechta odam bilan suhbatlashdingiz: "))
for i in range(n):
    odamlar.append(input(f"{i+1}-odamni kiriting: "))
print(odamlar)
    
