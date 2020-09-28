# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import PriorityQueue

def key_game_state(state):
        """
        Given a pacman game state, returns a key that uniquely identifies a
        pacman game state.

        Arguments:
        ----------
        - `state`: the current state of the game.

        Return:
        -------
        - A hashable key that uniquely identifies a pacman game state.
        """

        return (state.getPacmanPosition(), state.getFood())

def backward_cost(state, nextState):
        """
        Given two pacman game states, returns the cost between the states.

        Arguments:
        ----------
        - `state`: the current state of the game.
        - `nextState`: the next state of the game we are considering.

        Return:
        -------
        - The cost between `state` and `nextState`.
          1 if Pacman goes to a cell with a food dot.
          10 if Pacman goes to a cell without a food dot.
        """

        return 1 if nextState.getNumFood() < state.getNumFood() else 10

def heuristic(state):
        """
        Given a pacman game state, returns the heuristic value for the
        given state.

        Arguments:
        ----------
        - `state`: the current state of the game.

        Return:
        -------
        - The Manhattan distance between pacman position in the given game
          state and the fahrest food dot.
        """

        pacman_position = state.getPacmanPosition()
        food_matrix = state.getFood()

        max_distance = 0

        for i in range(food_matrix.width):
            for j in range(food_matrix.height):
                if food_matrix[i][j] == True:
                    distance = abs(pacman_position[0] - i)\
                               + abs(pacman_position[1] - j)
                    if distance > max_distance:
                        max_distance = distance

        return max_distance


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.moves = []

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """

        if not self.moves:
            self.moves = self.astar(state)

        try:
            return self.moves.pop(0)
        except IndexError:
            return Directions.STOP

    def astar(self, state):
        """
        Given a pacman game state, returns a sequence of legal moves
        to achieve the goal.

        Arguments:
        ----------
        - `state`: the current game state.

        Return:
        -------
        - A sequence of legal moves.
        """

        path = []
        fringe = PriorityQueue()
        closed = set()

        fringe.push((state, path, 0), 0)

        while True:
            if fringe.isEmpty():
                return [] # error
            
            priority, item = fringe.pop()

            if item[0].isWin():
                return item[1] # path

            key_current_state = key_game_state(item[0])

            if key_current_state not in closed:
                closed.add(key_current_state)

                for next_state, action in item[0].generatePacmanSuccessors():
                    cost = item[2] + backward_cost(item[0], next_state)
                    eval_function = cost + heuristic(next_state)
                    fringe.update((next_state, item[1] + [action], cost), eval_function)
            
        return path
