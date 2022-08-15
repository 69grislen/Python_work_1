#Изменение, добавление и удаление элементов в списке

#Изменение
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #Изменили на другое название
print(motorcycles)

#Добавление элементов в список
#Присоединение в конец списка
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati') #.apped присоединяет строку в () в конец списка
print(motorcycles)

#С помощью .append() можно добавлять элементы в пустой список
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Вставка элементов в список

motorcycles = ['honda', 'yamaha', 'suzuki']
#.insert() добавляет нов элем в выбранную позицию списка
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Удаление элементов из списка
#Используем команду del чтобы удалить элемент если мы знаем его позицию
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] #удаление первой позиции списка
print(motorcycles)

del motorcycles[1] #удаление второго элемента из списка
print(motorcycles)

#Используем команду .pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() # в () можно подставить любую позицию не только пустые скобки но и 0,1,2,...
print(motorcycles)
print(popped_motorcycle)

#Пример использования .pop()

motorcycles = ['honda', 'yamaha', 'suzuke']

last_owned = motorcycles.pop()
print(f"The last motorcycle i owned was a {last_owned.title()}")


