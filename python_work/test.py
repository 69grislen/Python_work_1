import random

random_number = random.randint(1,5)
user_number = input("Угадай число (от 1 до 5)")

if int(user_number)==random_number:
    print("Вы угадали число :)")

else:
    print("Вы не угадали число :(")

print(f"Было загадоно число {user_number}")