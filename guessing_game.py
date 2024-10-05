def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1
import random
import time
seconds_start = time.time()
list_01 = list(set([random.randint(1, 10) for i in range(10)]))
list_01.sort()
index = random.randint(0, len(list_01) - 1)
print(list_01)
number = int(input("Я загадал число, попробуй угадать: "))
while index != binary_search(list_01, number):
    if binary_search(list_01, number) == -1:
        print("Ты слепой")
    elif index > binary_search(list_01, number):
        print("Число больше")
    elif index < binary_search(list_01, number):
        print("Число меньше")
    number = int(input("Попробуй еще: "))
print("Ты угадал")
seconds = time.time()
print(f'Ты потратил на это {int(round(seconds-seconds_start, 0))} секунд')
