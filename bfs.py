# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import Queue

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

        fringe = Queue()
        fringe.push((state, path))

        closed = set()

        while True:
            if fringe.isEmpty():
                return []  # failure

            current, path = fringe.pop()

            if current.isWin():
                return path

            current_key = key_game_state(current)

            if current_key not in closed:
                closed.add(current_key)

                for next_state, action in current.generatePacmanSuccessors():
                    fringe.push((next_state, path + [action]))

        return path
