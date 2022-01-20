class MapView:

    def __init__(self):
        pass


    def display(self, map):
        """ Displays the Maze Map """
        for line in map:
            print(''.join(line))


    def display_result(self, collected_items):
        if (collected_items < 5):
            print(f"You lost!. You have only {collected_items} items.")
        else:
            print(f"Hurray, You won. You have all the {collected_items}. ")


