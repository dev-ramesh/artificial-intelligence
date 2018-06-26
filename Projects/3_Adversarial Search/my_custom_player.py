
from sample_players import DataPlayer


class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only *required* method. You can modify
    the interface for get_action by adding named parameters with default
    values, but the function MUST remain compatible with the default
    interface.

    **********************************************************************
    NOTES:
    - You should **ONLY** call methods defined on your agent class during
      search; do **NOT** add or call functions outside the player class.
      The isolation library wraps each method of this class to interrupt
      search when the time limit expires, but the wrapper only affects
      methods defined on this class.

    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.
    **********************************************************************
    """

    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller is responsible for
        cutting off the function after the search time limit has expired. 

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        depth = 1
        while depth < 100:
            # (my_moves - opponent_moves) heuristic from lecture
            self.queue.put(self.minimax(state, depth))
            # (my_moves / opponent_moves) heuristic from mine
            # self.queue.put(self.minimax(state, depth, True))
            depth += 1

    def minimax(self, state, depth, custom=False):

        alpha = float("-inf")
        beta = float("inf")
        best_move = None
        for a in state.actions():
            v = self.min_value(state.result(a), depth - 1, alpha, beta, custom)
            if v > alpha:
                alpha = v
                best_move = a
        return best_move

    def min_value(self, state, depth, alpha, beta, custom):
        if state.terminal_test():
            return state.utility(self.player_id)
        if depth <= 0:
            return self.score(state, custom)
        value = float("inf")
        for action in state.actions():
            value = min(value, self.max_value(
                state.result(action), depth - 1, alpha, beta, custom))
            beta = min(beta, value)
            if beta <= alpha:
                return value
        return value

    def max_value(self, state, depth, alpha, beta, custom):
        if state.terminal_test():
            return state.utility(self.player_id)
        if depth <= 0:
            return self.score(state, custom)
        value = float("-inf")
        for action in state.actions():
            value = max(value, self.min_value(
                state.result(action), depth - 1, alpha, beta, custom))
            alpha = max(alpha, value)
            if alpha >= beta:
                return value
        return value

    def score(self, state, custom):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        if custom:
            return len(own_liberties) / len(opp_liberties)
        else:
            return len(own_liberties) - len(opp_liberties)
