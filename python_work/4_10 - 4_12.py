#4_10
my_foods = ['pizza', 'falafel', 'carront cake']
friend_foods = my_foods[:]

my_foods.append("cannoli")
my_foods.append("cape")
friend_foods.append("ice cream")

print("Мои любимые блюда это:")
print(my_foods)

print("\n У моего друга любимые блюда это:")
print(friend_foods)

print("The irst three items in the list are:")
print(my_foods[:3])  # первые три элемента

print("Three items from the middle of the list are:")
print(my_foods[1:4])  #три элемента из середины

print("The last three items in the list are:")
print(my_foods[-3:])  #последние три элемента


#4_11
#Без цикла for
friend_pizzas = ["margaret", "four cheeses", "hawaiian"]
my_pizzas = friend_pizzas[:]

friend_pizzas.append("peperoni")
my_pizzas.append("macharello")

print("My favorite pizzas are:")
print(my_pizzas)

print("My friend’s favorite pizzas are:")
print(friend_pizzas)

#С циклом for
pizzas = ["margaret", "four cheeses", "hawaiian"]
friend_pizzas = pizzas[:]
for pizza in pizzas:

    pizzas.append("qwe")
    friend_pizzas.append("peperoni")

print("My favorite pizzas are:")
print(pizzas)

print("My friend’s favorite pizzas are:")
print(friend_pizzas)


#4_12
my_foods = ['pizza', 'falafel', 'carront cake']
for foods in my_foods:
    friend_foods = my_foods[:]

    my_foods.append("cannoli")
    friend_foods.append("ice cream")

print("Мои любимые блюда это:")
print(my_foods)

print("\n У моего друга любимые блюда это:")
print(friend_foods)

# неудачный файл







