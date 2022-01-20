from views.map import MapView
from models.maze import Maze

class MazeCoreController: 

    def __init__(self, command):
        self._view = MapView()
        self._command = command

    @classmethod
    def add_random_items(cls):
        count = 0
        while count < 5:
            spot = cls._maze.find_random_spot()
            cls._maze.map[spot[0]][spot[1]] = "O"
            count += 1

    @classmethod
    def start_app(cls):
        cls._maze = Maze()

    def move(self):
        x  = self._maze.player.x
        y = self._maze.player.y

        if (self._command == 'a'):
            if self._maze.can_move_to(x, y-1):
                return self.move_player(x, y-1)
        if (self._command == 's'):
            if self._maze.can_move_to(x+1, y):
                return self.move_player(x+1, y)
        if (self._command == 'd'):
            if self._maze.can_move_to(x, y+1):
                return self.move_player(x, y+1)
        if (self._command == 'w'):
            if self._maze.can_move_to(x-1, y):
                return self.move_player(x-1, y)
        return True


    def display(self):
        self._view.display(self._maze.map)

    
    def display_result(self):
        self._view.display_result(self._maze.player.backpack)

    def move_player(self, x, y):
        if self._maze.is_item(x,y):
            self._maze.player.backpack += 1
        if self._maze.is_exit(x,y):
            return False

        self._maze.map[x][y] = 'P'
        self._maze.map[self._maze.player.x][self._maze.player.y] = " "
        self._maze.player.x = x
        self._maze.player.y = y
        return True


