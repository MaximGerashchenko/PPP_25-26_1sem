Вариант 1:

import os

def rec_dir_walk(path, collected):
    collected.append(path)  # добавляем текущий путь
    if os.path.isdir(path):  # если это папка
        for name in os.listdir(path):  # обходим содержимое папки
            full_path = os.path.join(path, name)
            rec_dir_walk(full_path, collected)  # рекурсивный вызов для каждого вложенного элемента

# Пример:
result = []
rec_dir_walk("путь_к_папке", result)
for item in result:
    print(item)
