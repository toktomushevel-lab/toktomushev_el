data_tuple = ['h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g']
numbers = []
letters = []


for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

print(numbers)  
print(letters)  


if True in numbers:
    numbers.remove(True)
    letters.append(True)




if 1 in numbers and 3 in numbers:
    index_1 = numbers.index(1)
    index_3 = numbers.index(3)
    if index_1 < index_3:  
        numbers.insert(index_3, 2)
    else:  
        numbers.insert(index_1, 2)

numbers.remove(6.13)
print(numbers)

letters.reverse()
print(letters)

numbers.sort()

numbers.insert(7, 'True')
print(numbers)


letters[1] = 'G'
letters[-2] = 'c'
letters.remove(True)

print(letters)

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)
