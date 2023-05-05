array = [3, 55, 33, 32, 7, 51, 84, 45, 67]

def buble_sort(array: list)->list:
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] <= array[j]:
                array[i], array[j] = array[j], array[i]
    return array

print(buble_sort(array))
    

array= []
def tartiblash(word: str)-> str:
    for i in word:
        array.append(i)
    array.sort()
    for i in array:
        print(i, end=' ')

def qiduruv(array: list, value: str)-> str:
    j = 0
    for i in array:
        if value == i:
            print(f"{value} {j} da joylashgan!")

full_name = 'sharobiddinovnurmuhammad'
value = 'v'
tartiblash(full_name)
qiduruv(array, value)


