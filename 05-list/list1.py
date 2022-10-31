# list insert(), append(), del, remove(), pop()

ismlar = ['Fayzullo','Nurmuhammad','Javohir']
print(ismlar[2],"Frontend dasturchi!")
print(ismlar[0],"Frontend dasturchi!")
print(ismlar[1],"Backend dasturchi!")

sonlar = [-1, -2, 0, 1, 2, 3.14, 2.71, 36_765_345]
print(sonlar)
sonlar[0] = -23
sonlar[3] = 9.81
sonlar[1] = 9 + sonlar[1]
sonlar[-1] = 1200 + sonlar[-1]
print(sonlar)

t_shaxlar = ['Nyuton','Beruniy','Amir Temur']
z_shaxlar = ['Ilon Mask','Bill Gates','Shavkat Mirziyoyev']
t_shaxs = t_shaxlar.pop(0)
z_shaxs = z_shaxlar.pop(2)
print(f"Men tarixiy shaxslardan {t_shaxs} bilan,"
      f"zamonaviy shaxlardan esa {z_shaxs} bilan suhbat qilishni istar edim.")

friends = ['Qobiljon','Nurmuhammad','Javohir','Abdulaziz','Fayzullo','Muhtorjon']
print(friends)
friends.remove('Abdulaziz')
friends.remove('Muhtorjon')
friends.append('Zaribjon')
friends.insert(0,'Shohjahon')
friends.insert(3,'Sherzod')
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(3))
print(mehmonlar)
