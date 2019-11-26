import Loto


def choice_of_opponents(num_of_player):
    pl = None
    while pl not in ['c', 'h']:
        print(num_of_player, " игроком будет человек или компьютер?")
        pl = input("(c/h): ")
    if pl == "c":
        return Loto.Computer()
    return Loto.Human()


print("Добро пожловоать в игру 'Лото'! Время выбрать игроков")
count_of_players = int(input("Введите количество игроков: "))
players = []
for i in range(count_of_players):
    player = choice_of_opponents(i + 1)
    players.append(player)
hat = Loto.Hat()
while hat.chips:
    num = hat.take_chip()
    for i in range(count_of_players):
        if not isinstance(players[i], Loto.Loser):
            print("Ходит", i + 1, " игрок.")
        if not players[i].move(num):
            players[i] = Loto.Loser()
        if players[i].is_winning():
            print(i + 1, " игрок победил")
            break
