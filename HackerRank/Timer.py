import time
import random

class Game:

    def __init__(self):
        self.waiting_game()

    def waiting_game(self):
        print("In waiting Game")
        target = random.randint(2, 4)
        print("Your target time is {} seconds".format(target))

        input('--Press enter to Begin--')
        start = time.perf_counter()

        input('Press again Enter after {} seconds '.format(target))
        elapsed = time.perf_counter() - start

        print('\nElapsed time :{0:3f} seconds'.format(elapsed))


if __name__ == "__main__":
    Obj = Game()