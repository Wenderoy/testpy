import random, time

starttime = time.time()


mas = []

for i in range(10000):
    mas.append(random.randint(0, 10000))
    
    
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
        
    

mas = insertionSort(mas)
		



endtime = time.time() - starttime

print(mas)
print('Время выполнения', endtime)