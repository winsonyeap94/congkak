import sys


# Class for individual Congkak holes
class CongkakHole:
    def __init__(self, player, type):
        self.player = player
        self.type = type

        # Initialising marble count for score and house
        if type == "score":
            self.marbles = 0
        elif type == "house":
            self.marbles = 7
        else:
            sys.exit("Invalid type input found. Expected 'score' or 'house' but got {} instead.".format(type))


# Class for entire Congkak board, which will consist of individual holes of class CongkakHole
class CongkakBoard:
    def __init__(self):
