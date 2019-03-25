from player import Player
from table import Table
from colors import get_color


game_players = []

#TODO: add more Players
game_players.append(Player(input('Enter P' + str(Player.counter+1) + ' Name: ')))
game_players.append(Player(input('Enter P' + str(Player.counter+1) + ' Name: ')))
#TODO: Check if P2 != p1


def next_player(game_players, player_turn):
    if player_turn == len(game_players):
        return 1
    else:
        return player_turn + 1

player_turn = 1
game_table = Table()
win = False

while(True):
    status = None
    print("Player" + str(player_turn) + "'s Turn")
    x = input("Enter row[1-%s]" % str(game_table.x))
    status = game_table.put_in_row(get_color[player_turn], x)


    if status != None:
        if status == True:
            win = True
            print(player_turn)
            print("breaking")
            print(game_table)
            break
        else:
            print(status)
            continue


    print(game_table)

    player_turn = next_player(game_players, player_turn)

    if game_table.place_in_table == 0:
        print("tie")
        break

if win == True:
    print("%s win!" % game_players[player_turn-1].name)
    pass



