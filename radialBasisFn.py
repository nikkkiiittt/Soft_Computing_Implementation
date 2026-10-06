import numpy as np

from scipy.linalg import norm, pinv
from matplotlib import pyplot as plt


class RBF:

    def __init__(self, indim, numCenters, outdim):

        self.indim = indim
        self.outdim = outdim
        self.numCenters = numCenters

        self.centers = [
            np.random.uniform(-1, 1, indim)
            for _ in range(numCenters)
        ]

        self.beta = 8

        self.W = np.random.random(
            (self.numCenters, self.outdim)
        )

    def _basisfunc(self, c, d):

        assert len(d) == self.indim

        return np.exp(
            -self.beta * norm(c - d) ** 2
        )

    def _calcAct(self, X):

        # Calculate activations of RBFs
        G = np.zeros(
            (X.shape[0], self.numCenters),
            float
        )

        for ci, c in enumerate(self.centers):

            for xi, x in enumerate(X):

                G[xi, ci] = self._basisfunc(c, x)

        return G

    def train(self, X, Y):

        """
        X: matrix of dimensions n x indim
        Y: column vector of dimension n x 1
        """

        # Choose random center vectors from training set
        rnd_idx = np.random.permutation(
            X.shape[0]
        )[:self.numCenters]

        self.centers = [
            X[i, :] for i in rnd_idx
        ]

        print("centers:", self.centers)

        # Calculate activations of RBFs
        G = self._calcAct(X)

        print("activations G:", G)

        # Calculate output weights using pseudoinverse
        self.W = np.dot(
            pinv(G),
            Y
        )

    def test(self, X):

        """
        X: matrix of dimensions n x indim
        """

        G = self._calcAct(X)

        Y = np.dot(
            G,
            self.W
        )

        return Y


if __name__ == '__main__':

    # 1D Example
    n = 100

    x = np.mgrid[
        -1:1:complex(0, n)
    ].reshape(n, 1)

    # Set y
    y = np.sin(
        3 * (x + 0.5) ** 3 - 1
    )

    # RBF regression
    rbf = RBF(
        1,
        10,
        1
    )

    rbf.train(
        x,
        y
    )

    z = rbf.test(x)

    # Plot original data
    plt.figure(
        figsize=(12, 8)
    )

    plt.plot(
        x,
        y,
        'k-',
        label='Original data'
    )

    # Plot learned model
    plt.plot(
        x,
        z,
        'r-',
        linewidth=2,
        label='Learned model'
    )

    # Plot RBF centers
    plt.plot(
        rbf.centers,
        np.zeros(rbf.numCenters),
        'gs',
        label='RBF centers'
    )

    # Plot individual RBFs
    for c in rbf.centers:

        c = c[0]

        cx = np.arange(
            c - 0.7,
            c + 0.7,
            0.01
        )

        cy = [
            rbf._basisfunc(
                np.array([cx_]),
                np.array([c])
            )
            for cx_ in cx
        ]

        plt.plot(
            cx,
            cy,
            '-',
            color='gray',
            linewidth=0.2
        )

    plt.xlim(
        -1.2,
        1.2
    )

    plt.legend()

    plt.show()


# Radial Basis Function Network is a type of
# Artificial Neural Network that uses radial basis
# functions as activation functions.
#
# It is commonly used for function approximation
# and interpolation tasks.