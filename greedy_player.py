import random
import model
import memory

class Player:
    def __init__(self):
        self.gameScore = 0
        self.roundScore = 0
        self.neuralNet = model.Model(12, 6, 6)
        self.memory = memory.Memory(1000)

    def freeze(self, frozen):
        """
            randomly freezes valid dice, so that they will not be rolled again...this is a test function... not used
            for neural net...
        """
        freeze_dice = []
        for i in range(6):
            if frozen[i] is 1:  #
                freeze_dice.append(random.randint(0, 1))
            else:
                freeze_dice.append(0)
        return freeze_dice

    def train(self):
        # use the memory to train the Neural Network
            #  INPUTS
            #  current_state (array)
            #  our frozen_dice (array of zero and ones)

            #  back propagate the score
        return 4

    def decide(self, current_state, frozen_dice):
        # greedy inputs...
            #  current_state (array)
            #  our frozen_dice (array of zero and ones)

        # use the neural net to decide what to do..
            # create NeuralNet

        # outputs...
            # array of 6 zeros and ones...
        return 4
