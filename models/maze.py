from models.player import Player
import random

class Maze:

    def __init__(self, file=None):
        self._file = file
        self._map = []
        if not file:
            self._file = 'maze.txt'
        with open(self._file, 'r') as f:
            i = 0
            for element in f:
                j = 0
                element = element.strip("\n")
                line = list(element)
                self._map.append(line)
                for player_loc in line:
                    if (player_loc == "P"):
                        self.player = Player(i, j)
                    j += 1
                i += 1

    @property
    def map(self):
        return self._map


    def can_move_to(self, line_no, column_no):
        try:
            if self._map[line_no][column_no] != 'X':
                return True
        except IndexError:
            return False

    def display(self):
        for line in self._map:
            print(''.join(line))

    def find_random_spot(self):
        while True:
            row = random.randint(0,len(self.map)-1)
            column = random.randint(0,len(self.map[row])-1)
            if self.can_move_to(row, column):
                return (row, column)


    def is_item(self, row_num, column_num):
        if (self.map[row_num][column_num] == 'X') or (self.map[row_num][column_num] == ' '):
            return False
        else:
            return True


    def is_exit(self, row_num, column_num):
        return self.map[row_num][column_num] == 'E'
    

