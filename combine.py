list_1 = [1, 2, 56, 34, 241]
list_2 = [2, 56, 34, 123, 6]

def combine_and_unique(lst1, lst2):
    # Объединяем списки
    combined = lst1 + lst2
    # Создаем список для уникальных элементов
    unique_list = []
    
    # Добавляем элементы, если их еще нет в unique_list
    for number in combined:
        if number not in unique_list:
            unique_list.append(number)
    
    return unique_list

# Вызываем функцию с нужными аргументами
result = combine_and_unique(list_1, list_2)
print(result)
