#Перебор всего списка
#цикл for используется для вывода имен фокусников:

# for = для    in = в
magicians = ['alice', 'david', 'caroline'] #есть список фокусников
for magician in magicians:   #используем for и in в конце ставим :
    print(magician)
#в данном случае создает и сохраняет имя в переменной magician
#затем повторяет это зацикленное количество раз


#Подробнее о циклах

#Для циклов for временной переменной
#для текущего значения из списка можно присвоить любое имя.
# Однако на практике рекомендуется выбирать осмысленное имя, описывающее отдельный элемент
#списка. Несколько примеров:
#for cat in cats:
#for dog in dogs:

#Более сложные действия в циклах for
magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!") #использовали f строки в цикле for
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# \n символ новой строки !!!
#Выполнение действий после цикла for
print("Thank you, everyone. That was a great magic show!") # без tab (табуляции) ,
# больше не относится к циклу for и выводится как общая информация







