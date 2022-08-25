#4_13  Шведский стол
buffets = ('Köttbullar', 'Surströmming', 'Ärtsoppa', 'Kroppkakor', 'Isterband')
for buffet in buffets:
    print(buffet)  #вывод всех блюд

#buffets[2] = "что то там" #python выдает ошибку и подчеркивает это
#изменить элементы кортежа нельзя !!!!!!

print("\nресторан изменил меню")
buffets = ('Köttbullar', 'Surströmming', 'Ärtsoppa', 'щи', 'борщ') #заменили полностью значение так можно
for buffet in buffets:
    print(buffet)








