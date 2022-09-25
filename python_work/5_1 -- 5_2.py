# 5_1
print("первое условие")

user = 'reigan'

if user == 'reigan':
    print(f"Да, имя {user.title()} истинно")

else:
    print("Это имя не истинно , не прошло проверку на равенство")


print("второе условие")

if user == 'abgd':
    print(f"Это имя {user.title()} истинно")

else:
    print(f"К сожалению это ложь , настоящее имя {user.title()}")


# 5_2

school = 'gimnazia 31'

if school == 'normgosschool':
    print("Гимназия 31 нормальная гос школа")

else:
    print("Гимназия 31 худшая школа")


car = 'BMW'

if car.lower() == 'bmw':    #перевел car в нижний регистр и сравнил
    print('Да это бмв ууууу типо мощь')

else:
    print("Этого рекзультата не произойдет")


age = 16

if age < 18:
    print("Да мне меньше 18")

if age > 18:
    print(f"Это ложь тк мне {age} а это не больше 18")

else:
    print("Мне НЕ больше 18")

if age <= 18:
    print(f"Да мне меньше 18 , мой возраст {age}")

if age >= 18:
    print("нет")

else:
    print("да это правда")


car_0 = 1000
car_1 = 100

if car_0 >= 50 and car_1 >= 50:
    print('True')

if car_0 <= 120 and car_1 <= 10:
    print("False1")

else:
    print("False2")


car_0 = 1000
car_1 = 100

if car_0 > 0 or car_1 >100:
    print("Выполнилось одно условие ")


cars = ['a', 'b','s']
car = "d"

if car in cars:     #входит ли переменная car В список cars??
    print('Он входит в список')

else:
    print('Он не входит в список')



pizzas = ['piz1','piz2','piz3']
pizza = 'piz8'

if pizza not in pizzas:    #если переменная НЕ  входит в список то выводим print
    print(f"{pizza} не входит в список")






