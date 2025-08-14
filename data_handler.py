import numpy as np

class DataHandler:
    def __init__(self):
        self.X = np.empty((0, 2))
        self.y = np.array([])

    def add_point(self, x, y_label):
        self.X = np.vstack([self.X, x])
        self.y = np.append(self.y, y_label)

    def clear(self):
        self.X = np.empty((0, 2))
        self.y = np.array([]) //
