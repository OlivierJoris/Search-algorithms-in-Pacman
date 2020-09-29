# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import PriorityQueue

def key_game_state(state):
        """
        Given a pacman game state, returns a key that uniquely identifies a
        pacman game state.

        Argument:
        ----------
        - `state`: the current state of the game.

        Returns:
        --------
        - A hashable key that uniquely identifies a pacman game state.
        """

        return (state.getPacmanPosition(), state.getFood())

class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Argument:
        ---------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.moves = []

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Argument:
        ---------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Returns:
        --------
        - A legal move as defined in `game.Directions`.
        """

        if not self.moves:
            self.moves = self.bfs(state)

        try:
            return self.moves.pop(0)
        except IndexError:
            return Directions.STOP

    def bfs(self, state):
        """
        Given a pacman game state, returns a sequence of legal moves
        to achieve the goal.

        Argument:
        ---------
        - `state`: the current game state.

        Return:
        -------
        - A sequence of legal moves.
        """

        path = []
        fringe = PriorityQueue()
        closed = set()

        fringe.push((state, path, 0), 0)
        # item = (state, path, g(state))

        while True:
            if fringe.isEmpty():
                return [] # error
            
            item = fringe.pop()[1]

            if item[0].isWin():
                return item[1] # path

            key_current_state = key_game_state(item[0])

            if key_current_state not in closed:
                closed.add(key_current_state)

                for next_state, action in item[0].generatePacmanSuccessors():
                    if key_game_state(next_state) not in closed:
                        cost = item[2] + len(item[1])
                        eval_function = cost 
                        fringe.update((next_state, item[1] + [action], cost), eval_function)
            
        return path
