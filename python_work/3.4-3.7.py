#3_4
guests = ['andry','kate','alik']
print(f"Добро пожаловать в мой дом , дорогой {guests[0].title()}")
print(f"Добро пожаловать в мой дом , дорогой {guests[1].title()}")
print(f"Добро пожаловать в мой дом , дорогой {guests[-1].title()}")

#3_5
guests = ['andry','kate','alik']
no_vizit_guest = guests.pop(-1)

print(f"К сожалению {no_vizit_guest.title()} прийти не сможет")
print(guests)

guests.append('jaims') #в конец
guests.insert(1, 'rick') #куда выбрал туда и вставил
print(guests)

print(f"Приглашаю тебя ,{guests[0].title()} ,друг мой")
print(f"Приглашаю тебя ,{guests[1].title()} ,друг мой")
print(f"Приглашаю тебя ,{guests[2].title()} ,друг мой")
print(f"Приглашаю тебя ,{guests[3].title()} ,друг мой")

print(guests)
user_score = len(guests)
print(f"Всего гостей у нас {user_score}")
print(guests)

#3_6
guests = ['andry','kate','alik']
print(f"Список наших гостей {guests} будет расширяться")

guests.insert(0,'abraham') #добавили в начало
guests.insert(2,'elizovete') # добавили в середину
guests.append('rayl') # добавили в конец
print(guests)

print(f"Приглашаю тебя {guests[0].title()}")
print(f"Приглашаю тебя {guests[1].title()}")
print(f"Приглашаю тебя {guests[2].title()}")
print(f"Приглашаю тебя {guests[3].title()}")
print(f"Приглашаю тебя {guests[4].title()}")
print(f"Приглашаю тебя {guests[5].title()}")

#3_7
guests =['abraham', 'andry', 'elizovete', 'kate', 'alik', 'rayl']
print(f"К сожалеию на обед могут остаться только 2 гостя из всего списка {guests}")

une_loser = guests.pop()
print(f"Извини но ты {une_loser.title()} должен уйти")

two_loser = guests.pop()
print(f"Извини но ты {two_loser.title()} должен уйти")

three_loser = guests.pop()
print(f"Извини но ты {three_loser.title()} должен уйти")

four_loser = guests.pop()
print(f"Извини но ты {four_loser.title()} должен уйти")

print(guests)

print(f"Эй предложени еще в силе {guests[0].title()} так,что остовайся")
print(f"Эй предложени еще в силе {guests[1].title()} так,что остовайся")

del guests[0]
del guests[-1]

print(guests)









