import random 

# 1. Настройки 
N = 5               # размер массива
num_shuffles = 1000 # сколько раз будем перемешивать

# 2. Создаём исходный список
numbers = []
for i in range(1, N + 1):
    numbers.append(i)

# 3. Создаём таблицу частот (frequency)
frequency = []
for i in range(N):
    row = []             
    for j in range(N):
        row.append(0)    # добавляем нули в строку
    frequency.append(row) # добавляем строку в таблицу

# 4. Основной цикл — повторяем тасовку num_shuffles раз
for s in range(num_shuffles):
    temp = []
    for x in numbers:
        temp.append(x)

    random.shuffle(temp)

    # 5. После тасовки записываем, где какое число оказалось
    for pos in range(N):
        val = temp[pos]                   # число, которое стоит на позиции pos
        frequency[val - 1][pos] += 1     

# 6. Выводим результаты
print("Результаты после", num_shuffles, "тасовок (в процентах):")
for num in range(1, N + 1):
    print("Число", num, "оказывалось на позициях:", end=" ")
    for pos in range(N):
        count = frequency[num - 1][pos]           # сколько раз число num было на позиции pos
        percent = (count * 100.0) / num_shuffles  
        percent = round(percent, 2)               
        print(str(percent) + "%", end="  ")
    print() 
