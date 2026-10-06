import numpy as np
import time

np.set_printoptions(precision=2)

x = np.zeros((3,))
weights = np.zeros((3,))
desired = np.zeros((3,))
actual = np.zeros((3,))

for i in range(3):
    x[i] = float(input("Initial input x[{}]: ".format(i)))

for i in range(3):
    weights[i] = float(input("Initial weight w[{}]: ".format(i)))

for i in range(3):
    desired[i] = float(input("Desired output d[{}]: ".format(i)))

a = float(input("Enter learning rate: "))

actual = x * weights

print("Initial actual output:", actual)
print("Desired output:", desired)

while True:

    if np.array_equal(desired, actual):
        break  # no change needed

    else:
        for i in range(3):
            weights[i] = weights[i] + a * (desired[i] - actual[i])

        actual = x * weights

        print("Updated weights:", weights)
        print("Actual output:", actual)
        print("Desired output:", desired)
        print("*" * 30)

print("Final output")
print("Corrected weights:", weights)
print("Actual output:", actual)
print("Desired output:", desired)


#delta rule is used to update the weights based on the inputs, desired outputs, and actual outputs. The weights are updated by adding the product of the learning rate and the difference between the desired and actual outputs to the old weights. The process continues until the actual output matches the desired output.