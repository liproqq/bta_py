import numpy as np
from matplotlib import pyplot as plt


class LinearRegession:
    def __init__(self, eta=1e-4, epochs=25):
        self.eta = eta
        self.epochs = epochs

    def fit(self, X, y):
        # weights: slope weights[1:]
        # bias / intercept: weights[0]
        # y = w*x + b
        # y = sum(w[i]*x[i])+ w[0]
        self.weights = np.zeros(X.shape[1])
        self.bias = 0

        # save error in each epoch
        self.cost = []

        # adjust weights by epoch count
        for _ in range(self.epochs):
            prediction = self.predict(X).reshape(y.shape)

            errors = y - prediction

            mse = (errors**2).mean()

            self.cost.append(mse)

            self.weights += self.eta * X.T.dot(errors.ravel())
            self.bias += self.eta * errors.sum()

        return self

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


if __name__ == "__main__":
    # Create dataset
    X = 2 * np.random.rand(5, 1)

    y = 5 + 2 * X + np.random.rand(5, 1)

    plt.scatter(X, y)

    for i in range(5):
        lr = LinearRegession(epochs=i)
        lr.fit(X, y)
        plt.plot(X, lr.predict(X), label=str(i))
    plt.show()

    plt.plot(range(1, lr.epochs+1), lr.cost)

    print(f"y= {lr.weights[0]:.2f}*x + {lr.bias:.2f}")
    plt.show()
