#Реализация с помощью списка и указателей на начало и конец
class CircularBufferList:
    def __init__(self, size: int) -> None:
        self.size = size
        self.buffer = [None]*size
        self.head = 0
        self.tail = 0
        self.count = 0
    
    #Запись в буфер
    def write(self, item) -> None:
        #Выдаем ошибку если пытаемся записать в полный буфер
        if (self.count >= self.size):
            raise OverflowError("buffer is full")
        
        #Добавляем в конец буфера item
        self.buffer[self.tail] = item
        
        #Циклически инкрементируем указатель tail
        self.tail = (self.tail + 1) % self.size
        
        #Инкрементируем счетчик элементов
        self.count += 1
        
    #Чтение из буфера
    def read(self):
        #Ошибка если пытаемся читать из пустого буфера
        if (self.count <= 0):
            raise IndexError("Buffer is empty")
        
        #Получаем первый элемент и циклически инкрементируем указатель head
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        
        #Декрементируем счетчик элементов
        self.count -= 1
        
        #Возвращаем элемент
        return item
    
    #Проверить заполнен ли буфер
    def is_full(self)->bool:
        return self.size >= self.count
    
    #Проверить пуст ли буфер
    def is_empty(self)->bool:
        return self.count <= 0
        
        

#Реализация с помощью collections.deque
from collections import deque

class CircularBufferDeque:
    def __init__(self, size: int) -> None:
        self.size = size
        self.buffer = deque(maxlen=size)
        
    #Запись в буфер
    def write(self, item)->None:
        
         #Выдаем ошибку если пытаемся записать в полный буфер
        if (len(self.buffer) >= self.size):
            raise OverflowError("buffer is full")
        
        #Добавляем в конец деки
        self.buffer.append(item)
        
    #Чтение из буфера
    def read(self):
        #Ошибка если пытаемся читать из пустого буфера
        if (len(self.buffer) <= 0):
            raise IndexError("buffer is empty")
        
        #Возвращаем первый элемент деки и удаляем его
        return self.buffer.popleft()
    
    #Проверить заполнен ли буфер
    def is_full(self)->bool:
        return len(self.buffer) >= self.size
    
    #Проверить пуст ли буфер
    def is_empty(self)->bool:
        return len(self.buffer) <= 0
    
