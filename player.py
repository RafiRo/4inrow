class Player(object):
    players = {}
    counter = 0
    name = None
    in_use = 0

    def __new__(cls, name):
        if name in Player.players:
            print("EXISTS")
            return Player.players[name]
        else:
            print("NEW")
            return super(Player, cls).__new__(cls)

    def __init__(self, name):
        self.name = name
        Player.counter = Player.counter + 1
        Player.players[name] = self

    def __del__(self):
            del Player.players[self.name]
            Player.counter = Player.counter - 1


