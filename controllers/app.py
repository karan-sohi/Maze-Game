
from controllers.maze_core_controller import MazeCoreController
from controllers.maze_controller import MazeController

class App:
    """ This is the main class of our application
    
    """
    def __init__(self, filename=None):
        self._filename = filename
        if not filename:
            self._filename = 'maze.txt'


    def run(self):
        core_controller = MazeCoreController.start_app()
        MazeCoreController.add_random_items()
        running = True
        user_command = ' '
        maze_controller = MazeController()
        core_controller = MazeCoreController(user_command)
        while running:
            core_controller.display()
            user_command = maze_controller.get_user_input()
            core_controller = MazeCoreController(user_command)
            running = core_controller.move()

        core_controller.display_result()
            
