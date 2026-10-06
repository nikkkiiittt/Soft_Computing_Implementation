import numpy as np
import matplotlib.pyplot as plt


def create_distance_function(a, b, c):
    """
    Creates a distance function for the line equation
    0 = ax + by + c.

    Returns a function that calculates the distance of
    a point (x, y) from the line and its position
    relative to the line.
    """

    def distance(x, y):
        """
        Returns tuple (d, pos)

        d is the distance.

        If pos == -1, point is below the line.
        If pos == 0, point is on the line.
        If pos == +1, point is above the line.
        """

        nom = a * x + b * y + c

        if nom == 0:
            pos = 0

        elif (nom < 0 and b < 0) or (nom > 0 and b > 0):
            pos = -1

        else:
            pos = 1

        return (
            np.absolute(nom) /
            np.sqrt(a ** 2 + b ** 2),
            pos
        )

    return distance


# Define points and create plot
points = [
    (3.5, 1.8),
    (1.1, 3.9)
]

fig, ax = plt.subplots()

ax.set_xlabel("sweetness")
ax.set_ylabel("sourness")

ax.set_xlim([-1, 6])
ax.set_ylim([-1, 8])


# Plot points
for index, (x, y) in enumerate(points):

    if index == 0:
        ax.plot(
            x,
            y,
            "o",
            color="darkorange",
            markersize=10
        )

    else:
        ax.plot(
            x,
            y,
            "oy",
            markersize=10
        )


# Define X values for plotting lines
X = np.arange(
    -0.5,
    5,
    0.1
)

step = 0.05


# Iterate over possible slopes
for x in np.arange(
    0,
    1 + step,
    step
):

    slope = np.tan(
        np.arccos(x)
    )

    dist4line1 = create_distance_function(
        slope,
        -1,
        0
    )

    # Calculate Y values for the line
    Y = slope * X

    # Calculate distances for each point
    results = [
        dist4line1(*point)
        for point in points
    ]

    # Plot the line based on the position
    # of the points relative to the line
    if results[0][1] != results[1][1]:

        ax.plot(
            X,
            Y,
            "g-"
        )

    else:

        ax.plot(
            X,
            Y,
            "r-"
        )


plt.show()


#linear separability is a property of a dataset that indicates whether the data points can be separated into distinct classes using a linear boundary, such as a straight line in two-dimensional space or a hyperplane in higher dimensions. In other words, if you can draw a straight line (or hyperplane) that divides the data points of one class from those of another class without any overlap, the dataset is considered linearly separable.
#in easy words, linear separability means that you can separate the data points of different classes using a simple linear decision boundary. If the data points cannot be separated by a straight line or hyperplane, the dataset is considered non-linearly separable.
#it is used when you want to determine if a linear classifier, such as a perceptron or linear regression model, can effectively separate the classes in your dataset. If the data is linearly separable, these models can achieve good classification performance. However, if the data is not linearly separable, more complex models, such as support vector machines with non-linear kernels or neural networks, may be required to achieve accurate classification.