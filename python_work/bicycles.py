#Cписки
#Рекомендуется присваивать спискам множественное число названиям переменных напр: names
#В Puthon список обозначается []

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Обращение к элементам списка  Индексы начинаются с 0 , а не с 1

print(bicycles[0]) #Обратились к первому индексу переменной  !!!

print(bicycles[0].title()) #Использовали метод из главы 2 и первая буква стала большой

print(bicycles[-1])  # -1 возвращает и выводит последней элемент в списке

print(bicycles[-2])  #Возвращает второй элемент с конца списка

#Использование отдельных элементов из списк
#Использование f строк со списком

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}"

print(message)





