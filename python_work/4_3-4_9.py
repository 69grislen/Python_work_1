#4_3
for value in range(1,21): # тут у нас смещение на 1
    print(value)

#4_4 и 4_5
numbers = []
for value in range(1,1_000_001):
    numbers.append(value)
print(numbers) #Создали пустой список и добавили в него value со значениеми из range()

print(min(numbers)) #Минимальное значение

print(max(numbers)) #Максимальное значение

print(sum(numbers)) #Просуммирование миллиона из списка

#4_6
print("Нечетные числа от 1 до 20")
for value in range(1,21,2):
    print(value)

#4_7
print("1 вариант как решить")

numbers = list(range(3,31,3))
print(numbers)

print("2 вариант как решить")
#То же самое но с циклом for
numbers = []
for value in range(3,31,3):
    numbers.append(value)
print(numbers)

#4_8
print("1 способ")

numbers = []
for value in range(1,11):
    numbers.append(value ** 3)
print(numbers)

print("2 способ")

numbers = []
for value in range(1,11):
    number = value ** 3
    numbers.append(number)
print(numbers)

#4_9
print("Генератор списка кубов")

numbers = [value**3 for value in range(1,11)]
print(numbers)
# запомни что тут обязательно [] иначе будет ошибка

riders = [value**3 for value in range(11)]  #тут начинается с 0 тк нету числа start (a,b)
print(riders)


