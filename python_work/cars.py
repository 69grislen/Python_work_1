#Упорядочивания списка

#Использования метода.sort  (в возрастающем или убывающем порядке)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #упорядочил по алфовиту
print(cars)

# в обратонм алфовитном порядке
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #к методу .sort() применили аргумент reverse
print(cars)

#Временная сортировка списка функцией sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ") #список выводится в новом порядке
print(sorted(cars))

print("\nHere is the original list: ") #все еще храниться в исъодно порядке
print(cars)


#Вывод списка в обратном порядке
#Чтобы переставить элементы списка в обратном порядке, используйте метод
#reverse()    не только в самом .sort() но и сам может

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse() #переходит к обратному порядка списка!!
print(cars)

#Определение длины списка
#с помощью len

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) #Применили метод len и узнали сколько элементов в списке
#При использовании len Python начинает счиатть элементы списка с 1 (одного) ,
# те смещения на 1 уже не будет



