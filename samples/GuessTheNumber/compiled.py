# < THIS FILE WAS AUTOMATICALLY COMPILED BY Gangpy COMPILER. >
# < https://github.com/realbxnnie/gangpy >

from random import *
from math import * 

НоваяИгра = None

class Игра:
    def __init__(self):
        выбор = input("Добро пожаловать в игру 'Угадай число'! Начинаем? [Y/n]: ")
        if выбор.lower() == "y":
            число = randint(1, 10)
            Игра.вводЧисла(число)
        else:
            exit()
            
    def вводЧисла(число):
        числоВыбор = int(input("Введите число от 1 до 10: "))
        match числоВыбор:
                case _ if числоВыбор < число:
                    print("Ваше число меньше чем загаданное число.")
                    Игра.вводЧисла(число)
                case _ if числоВыбор > число:
                    print("Ваше число больше чем загаданное число.")
                    Игра.вводЧисла(число)
                case число:
                    print("Вы угадали число!")
                    НоваяИгра = Игра()

if __name__ == "__main__":
    НоваяИгра = Игра()
