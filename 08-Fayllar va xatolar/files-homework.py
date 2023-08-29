import pickle

with open('fayllar-malumot.txt') as file:
    malumot = file.read()

print(malumot)
#--------------------------------------------------

with open('pi_million_digits.txt') as file:
    PI = file.read()

PI = PI.strip()
PI = PI.replace('\n', '')
PI = PI.replace(' ', '')

t_kun_yil = '192003'

print(t_kun_yil in PI)

#---------------------------------------------------

PI = float(PI)

with open('pi_number.dat', 'wb') as file:
    pickle.dump(PI, file)

#---------------------------------------------------

while True:
    text = input('Xabar kiriting: ')
    if not text: break
    with open('message.txt', 'a') as file:
        file.write(text + '\n')