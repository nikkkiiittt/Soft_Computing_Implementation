import numpy as np


# Input binary patterns
data = np.array([
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 1]
])


# Vigilance parameter
rho = 0.7

clusters = []
cluster_labels = []

print("Input Patterns:\n")
print(data)
print()


# ART1 Clustering
for pattern in data:

    assigned = False

    for i, cluster in enumerate(clusters):

        # Intersection
        match = np.logical_and(
            pattern,
            cluster
        ).astype(int)

        # Match ratio
        similarity = (
            np.sum(match) /
            np.sum(pattern)
        )

        if similarity >= rho:

            clusters[i] = match

            cluster_labels.append(i)

            assigned = True

            break

    if not assigned:

        clusters.append(
            pattern.copy()
        )

        cluster_labels.append(
            len(clusters) - 1
        )


# Display Results
print("Cluster Representatives:\n")

for i, c in enumerate(clusters):

    print(
        "Cluster",
        i,
        ":",
        c
    )


print("\nCluster Assignment:\n")

for pattern, label in zip(
    data,
    cluster_labels
):

    print(
        pattern,
        "--> Cluster",
        label
    )


## ART1 clustering is a type of unsupervised learning algorithm that groups binary input patterns into clusters based on their similarity. The algorithm uses a vigilance parameter to determine the threshold for similarity, allowing it to adaptively form clusters as new patterns are presented. The resulting clusters can be used for pattern recognition, data compression, and other applications where grouping similar data is beneficial.
#art is used for clustering binary input patterns based on their similarity. It adaptively forms clusters using a vigilance parameter, allowing for pattern recognition and data compression.