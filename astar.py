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


def step_cost(state, next_state):
        """
        Given two pacman game states, returns the step cost between `state`
        and `next_state`.

        Arguments:
        ----------
        - `state`: the current state of the game.
        - `next_state`: the next state of the game.

        Returns:
        --------
        - The step cost between `state` and `next_state`.
          1 if Pacman goes to a cell with a food dot.
          10 if Pacman goes to a cell without a food dot.
        """

        return 1 if next_state.getNumFood() < state.getNumFood() else 10


def heuristic(state):
        """
        Given a pacman game state, returns the heuristic value for the
        given state.

        Argument:
        ---------
        - `state`: the current state of the game.

        Returns:
        --------
        - The Manhattan distance between pacman position and the fahrest
          food dot in the maze.
        """

        if state.getNumFood() == 0:  # goal node
            return 0

        pacman_position = state.getPacmanPosition()
        food_matrix = state.getFood()

        max_distance = 0

        for i in range(food_matrix.width):
            for j in range(food_matrix.height):
                if food_matrix[i][j]:
                    distance = abs(pacman_position[0] - i)\
                               + abs(pacman_position[1] - j)
                    if distance > max_distance:
                        max_distance = distance

        return max_distance


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
            self.moves = self.astar(state)

        try:
            return self.moves.pop(0)

        except IndexError:
            return Directions.STOP

    def astar(self, state):
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

        while True:
            if fringe.isEmpty():
                return []  # error

            state, path, priority = fringe.pop()[1]

            if state.isWin():
                return path

            key_current_state = key_game_state(state)

            if key_current_state not in closed:
                closed.add(key_current_state)

                for next_state, action in state.generatePacmanSuccessors():
                    if key_game_state(next_state) not in closed:
                        cost = priority + step_cost(state, next_state)
                        eval_function = cost + heuristic(next_state)
                        fringe.update(
                            (next_state, path + [action], cost),
                            eval_function
                        )

        return path
