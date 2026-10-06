import numpy as np
import matplotlib.pyplot as plt


class SOM:

    def __init__(
        self,
        grid_size,
        num_iterations,
        learning_rate=0.05
    ):
        self.grid_size = grid_size
        self.num_iterations = num_iterations
        self.learning_rate = learning_rate
        self.sigma = max(grid_size) / 2.0

        self.weights = np.random.rand(
            grid_size[0],
            grid_size[1],
            3
        )

    def _find_bmu(self, x):

        # Compute the distance from the input vector to each weight vector
        dist = np.linalg.norm(
            self.weights - x,
            axis=2
        )

        # Find the index of the BMU
        return np.unravel_index(
            np.argmin(dist),
            dist.shape
        )

    def _update_weights(
        self,
        x,
        bmu_idx,
        iteration
    ):

        # Compute the learning rate and sigma for the current iteration
        lr = self.learning_rate * (
            1 - iteration / self.num_iterations
        )

        sigma = self.sigma * (
            1 - iteration / self.num_iterations
        )

        # Update weights
        for i in range(self.grid_size[0]):

            for j in range(self.grid_size[1]):

                dist = np.linalg.norm(
                    np.array([i, j]) -
                    np.array(bmu_idx)
                )

                h = np.exp(
                    -dist / (2 * sigma**2)
                )

                self.weights[i, j, :] += (
                    lr *
                    h *
                    (x - self.weights[i, j, :])
                )

    def train(self, data):

        for iteration in range(
            self.num_iterations
        ):

            for x in data:

                bmu_idx = self._find_bmu(x)

                self._update_weights(
                    x,
                    bmu_idx,
                    iteration
                )

    def plot(self):

        plt.imshow(
            self.weights,
            origin='lower'
        )

        plt.title('SOM Color Map')
        plt.axis('off')
        plt.show()

    def get_mapped_indices(self, data):

        mapped = np.array([
            self._find_bmu(x)
            for x in data
        ])

        return mapped


if __name__ == "__main__":

    # Define colors and their names
    colors = np.array([

        [0., 0., 0.],
        [0., 0., 1.],
        [0., 0., 0.5],
        [0.125, 0.529, 1.0],
        [0.33, 0.4, 0.67],
        [0.6, 0.5, 1.0],
        [0., 1., 0.],
        [1., 0., 0.],
        [0., 1., 1.],
        [1., 0., 1.],
        [1., 1., 0.],
        [1., 1., 1.],
        [0.33, 0.33, 0.33],
        [0.5, 0.5, 0.5],
        [0.66, 0.66, 0.66]
    ])

    color_names = [

        'black',
        'blue',
        'darkblue',
        'skyblue',
        'greyblue',
        'lilac',
        'green',
        'red',
        'cyan',
        'violet',
        'yellow',
        'white',
        'darkgrey',
        'mediumgrey',
        'lightgrey'
    ]

    # Initialize and train the SOM
    som = SOM(
        grid_size=(20, 30),
        num_iterations=400,
        learning_rate=0.05
    )

    som.train(colors)

    # Plot the SOM color map
    som.plot()

    # Get the mapped indices
    # and plot the color names
    mapped_indices = som.get_mapped_indices(
        colors
    )

    plt.imshow(
        som.weights,
        origin='lower'
    )

    plt.title('Color SOM')

    for i, (r, c) in enumerate(
        mapped_indices
    ):

        plt.text(
            c,
            r,
            color_names[i],
            ha='center',
            va='center',
            bbox=dict(
                facecolor='white',
                alpha=0.5,
                lw=0
            )
        )

    plt.show()
    
    
#kohonen self-organizing map (SOM) is an unsupervised learning algorithm that maps high-dimensional data to a lower-dimensional grid while preserving the topological structure of the data. The code defines a SOM class that initializes a grid of weights, finds the best matching unit (BMU) for each input vector, updates the weights based on the BMU and the input vector, and trains the SOM over multiple iterations. The trained SOM can be visualized as a color map, and the mapped indices of the input colors can be displayed with their corresponding names.
#why kohonen is used? 
#Kohonen Self-Organizing Maps (SOMs) are used for several reasons:
#1. Dimensionality Reduction: SOMs can reduce high-dimensional data to a lower-dimensional representation while preserving the topological relationships between data points.
#2. Visualization: SOMs provide a visual representation of complex data, making it easier to                        

