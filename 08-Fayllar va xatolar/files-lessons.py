# fayl = open('pi.txt')
# pi = fayl.read()
# print(pi)
# fayl.close()

# with open('pi.txt') as fayl:
#     pi = fayl.read()

# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# print(pi)

# with open('talabalar.txt') as file:
#     for line in file:
#         print(line)

# with open('talabalar.txt') as file:
#     first_line = file.readline()
#     second_line = file.readline()
#     print(first_line)
#     print(second_line)
#     talabalar = file.readlines()

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar) 

file_name = 'ustozlar.txt'
# full_name = 'Sharobiddinov Nurmuhammad'
# birth_date = 2003

# with open(file_name, 'w') as file: # w - write
#     file.write(full_name + ' ')
#     file.write(str(birth_date))

# with open(file_name, 'a') as file: # a - apppend
#     file.write('Fayzulloxon Turubxonov ')
#     file.write('2003\n')

import pickle

# # talaba1 = {'ism':'Nurmuhammad', 'familya':'Sharobiddinov', 'tyil':2003, 'kurs':3}
# # talaba2 = {'ism':'Javohir', 'familya':'To\'xtasinov', 'tyil':2003, 'kurs':4}

# with open('info', 'wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)


with open('info', 'rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)