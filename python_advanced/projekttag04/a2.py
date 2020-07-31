import pickle
import numpy as np
from pathlib import Path

path = Path(__file__).parent
feat_path = path / "feat.pkl"
targ_path = path / "targ.pkl"


class Main:
    def __init__(self):
        self.pickle1 = pickle.load(open(feat_path, "rb"))
        self.pickle2 = pickle.load(open(targ_path, "rb"))
        self.pickle1 = self.reshape_for_conv(self.pickle1)
        self.pickle2 = self.reshape_for_conv(self.pickle2)

    def reshape_for_conv(self, input):
        input = input/255
        return input.reshape(*input.shape, 1)

    def __str__(self):
        return str(self.pickle1) + str(self.pickle2)


if __name__ == "__main__":
    test = Main()
    print(test)
