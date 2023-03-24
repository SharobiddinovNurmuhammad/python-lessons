# Ro'yhat(List)lar 

#--------------------------------------------

ismlar = ['Javohir', 'Abdulaziz', 'Fayzullo', 'Muhtorjon']
print(ismlar)

#--------------------------------------------

print("Assalomu alaykum", ismlar[0])
print(ismlar[1], "dasturlash qanday ketaybdi?")
print(ismlar[-1], "aka sog'liklaringiz yaxshimi?")

#--------------------------------------------

sonlar = [-1, 0, 1, 2.71, -9.81, 36_560_483, 10200]
print(sonlar)

#--------------------------------------------

sonlar[2] = 23
sonlar[-1] = 1923
sonlar[5] = sonlar[-1] + 2000
print(sonlar)

#---------------------------------------------

t_shaxslar = ['Amir Temur', 'Beruniy', 'Navoiy']
z_shaxslar = ['Elon Mask', 'Mark Sukerberg', 'Cristiano']

#---------------------------------------------

t_shaxs = t_shaxslar.pop(2)
z_shaxs = z_shaxslar.pop(0)
print(f"Men tarixiy shaxlardan {t_shaxs} bilan,"
      f"zamonaviy shaxslardan esa {z_shaxs} bilan suhbat qilishni istardim!")

#----------------------------------------------

friends = []
friends.append('Javohir')
friends.append('Yoqubjon')
friends.append('Samandar')
friends.append('Jasur')
friends.append('Qobiljon')
friends.append('Xurshid')
print(friends)

#-----------------------------------------------

friends.remove('Samandar')
friends.remove('Qobiljon')
print(friends)

#-----------------------------------------------

friends.insert(0, 'Muhammadjon')
friends.insert(3, "Sa'dulla")
friends.insert(-1, 'Mashrabjon')
print(friends)

#-----------------------------------------------

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
print(mehmonlar)

#-----------------------------------------------