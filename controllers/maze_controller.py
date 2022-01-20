class MazeController:

    def __init__(self):
        pass

    def get_user_input(self):
        while True:
            user_command = self._ask_for_input()
            return user_command

    
    def _ask_for_input(self):
        allowed_commands = ['a', 's', 'w', 'd']
        user_input = ' '
        while user_input not in allowed_commands:
            user_input = input("a/s/w/d: ")
            if user_input not in allowed_commands:
                print("Please enter a valid move")

        return user_input