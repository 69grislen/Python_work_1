# Создание ЧИСЛОВЫХ списков

# Функция range()
for value in range(1, 5):
    print(value)  # Это пример смещения на 1  !!!!!!!!

print("Подставим range(1,6)")

# Чтобы вывести числа от 1 до 5, используйте вызов range(1,6):
for value in range(1, 6):
    print(value)

#Если ваша программа при использовании range() выводит не тот результат, на
#который вы рассчитывали, попробуйте увеличить конечное значение на 1.

print("Подставим range(6)")
for value in range(6):
    print(value) #Будет считать от 0 до 5

#Использование range() для создания числового списка
print("Создание числового списка")
#Заключим функцию range() в функцию list()
numbers = list(range(1,6))  #Создали список с помошью функций
print(numbers)








