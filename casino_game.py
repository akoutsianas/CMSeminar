import numpy as np


class CasinoGame:

    def __init__(self, strategy):
        self.strategy = strategy

    def single_game(self, wallet, goal, p=0.5, perc=0.5):
        if self.strategy == 'timid_play':
            return self._timid_single_game(wallet, goal, p=p)
        elif self.strategy == 'bold_play':
            return self._bold_single_game(wallet, goal, p=p, perc=perc)
        elif self.strategy == 'third_stategy':
            return self._third_strategy(wallet, goal, p)
        else:
            print(f"I do not know this strategy!")

    def _timid_single_game(self, wallet, goal, p=0.5):
        num_of_rounds = 0
        while wallet > 0 and wallet < goal:
            profit = np.random.choice([1, -1], p=[p, 1 - p])
            wallet += profit
            num_of_rounds += 1
        if wallet == goal:
            return 1, num_of_rounds
        else:
            return 0, num_of_rounds

    def _bold_single_game(self, wallet, goal, p=0.5, perc=0.5):
        num_of_rounds = 0
        while wallet > 0 and wallet < goal:
            profit_sign = np.random.choice([1, -1], p=[p, 1 - p])
            if wallet <= goal * perc:
                wallet += wallet * profit_sign
            else:
                wallet += (goal - wallet) * profit_sign
            num_of_rounds += 1
        if wallet == goal:
            return 1, num_of_rounds
        else:
            return 0, num_of_rounds

    def _third_strategy(self, wallet, strategy, p=0.5):
        pass

