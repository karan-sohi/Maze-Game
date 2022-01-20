class Player:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._backpack = 0
        self._filename = './maps.txt'
    
    @property
    def backpack(self): 
        return self._backpack

    @backpack.setter
    def backpack(self, value):
        self._backpack = value

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value
    
    @y.setter
    def y(self, value):
        self._y = value


