import random


class Card:
    def __init__(self):
        self.numbers = []
        while len(self.numbers) < 15:
            i = random.randrange(1, 91)
            if i not in self.numbers:
                self.numbers.append(i)
        self.strings = {}
        for i in range(3):
            self.strings[i] = self.numbers[i*5:i*5 + 5]
            self.strings[i].sort()

    def show_card(self, num):
        print("Из бочонка достали число: ", num)
        print("-"*30)
        for i in range(3):
            for num in self.strings[i]:
                print(num, " ", end=" ")
            print("\n")
        print("-" * 30)


class Player:
    def __init__(self):
        self.card = Card()

    def is_winning(self):
        for i in range(3):
            if self.card.strings[i].count("-") < 5:
                return False
        return True


class Human(Player):
    def move(self, num):
        self.card.show_card(num)
        answer = None
        while answer not in ['y', 'n']:
            answer = input("Зачеркнуть число? (y/n) ")
        if answer == "y":
            if num not in self.card.numbers:
                print("Такого числа нет на Вашей карточке! Вы проиграли...")
                return False
            else:
                for i in range(3):
                    if num in self.card.strings[i]:
                        self.card.strings[i][self.card.strings[i].index(num)] = '-'
                        self.card.numbers.pop(self.card.numbers.index(num))
                        return True
        else:
            if num in self.card.numbers:
                print("Такое число есть на Вашей карточке! Вы проиграли...")
                return False
            return True


class Computer(Player):
    def move(self, num):
        self.card.show_card(num)
        if num in self.card.numbers:
            for i in range(3):
                if num in self.card.strings[i]:
                    self.card.strings[i][self.card.strings[i].index(num)] = '-'
                    self.card.numbers.pop(self.card.numbers.index(num))
        return True


class Loser(Player):
    def move(self, num):
        pass


class Hat:
    def __init__(self):
        self.chips = [i for i in range(1, 91)]

    def take_chip(self):
        return self.chips.pop(random.randrange(len(self.chips)))
