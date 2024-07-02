#Реализация алгоритма сортировки quicksort
def quicksort(arr: list)->list:
    if (len(arr) <= 1):
        return arr
    
    #Находим центральный элемент в массиве
    pivot = arr[len(arr)//2]
    
    #Помещаем в массив left все элементы меньше pivot
    left = [x for x in arr if x < pivot]
    
    #Помещаем в массив middle все элементы равные pivot
    middle = [x for x in arr if x == pivot]
    
    #Помещаем в массив right все элементы больше pivot
    right = [x for x in arr if x > pivot]
    
    #Рекурсивно вызываем quicksort для элементов меньше и больше pivot и склеиваем массивы
    return quicksort(left) + middle + quicksort(right)


#массив корректно сортируется
arr = [1,4,63,24,1,-234, 22, 441, 324]
print(quicksort(arr))