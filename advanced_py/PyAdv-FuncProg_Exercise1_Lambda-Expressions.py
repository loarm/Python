my_list = [5,4,3]

print(list(map(lambda item: item ** 2, my_list))) # square

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# сравнить второй элемент каждого кортежа
# отсортировать список

print(sorted(a, key=(lambda i: i[1])))

print(sorted(range(-5, 6), key=lambda x: x * x))