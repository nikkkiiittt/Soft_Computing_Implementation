import numpy as np

print('Enter weights')

w11 = int(input('Weight w11='))
w12 = int(input('Weight w12='))
w21 = int(input('Weight w21='))
w22 = int(input('Weight w22='))
v1 = int(input('Weight v1='))
v2 = int(input('Weight v2='))

print('Enter Threshold Value')
theta = int(input('theta='))

x1 = np.array([0, 0, 1, 1])
x2 = np.array([0, 1, 0, 1])
z = np.array([0, 1, 1, 0])

con = 1

y1 = np.zeros((4,))
y2 = np.zeros((4,))
y = np.zeros((4,))

while con == 1:

    zin1 = x1 * w11 + x2 * w21
    zin2 = x1 * w12 + x2 * w22

    print("zin1", zin1)
    print("zin2", zin2)

    for i in range(0, 4):
        if zin1[i] >= theta:
            y1[i] = 1
        else:
            y1[i] = 0

        if zin2[i] >= theta:
            y2[i] = 1
        else:
            y2[i] = 0

    yin = y1 * v1 + y2 * v2

    for i in range(0, 4):
        if yin[i] >= theta:
            y[i] = 1
        else:
            y[i] = 0

    print("yin", yin)

    print('Output of Net')

    y = y.astype(int)

    print("y", y)
    print("z", z)

    if np.array_equal(y, z):
        con = 0
    else:
        print("Net is not learning. Enter another set of weights and Threshold value")

        w11 = int(input("Weight w11="))
        w12 = int(input("weight w12="))
        w21 = int(input("Weight w21="))
        w22 = int(input("Weight w22="))
        v1 = int(input("weight v1="))
        v2 = int(input("weight v2="))
        theta = int(input("theta="))

print("McCulloch-Pitts Net for XOR function")

print("Weights of Neuron Z1")
print(w11)
print(w21)

print("Weights of Neuron Z2")
print(w12)
print(w22)

print("Weights of Neuron Y")
print(v1)
print(v2)

print("Threshold value")
print(theta)

#XOR function is a logic gate that outputs true or 1 only when the two binary input values are unequal. The McCulloch-Pitts model is a mathematical model of a neuron that can be used to implement logic gates, including the XOR function. In this code, the user inputs weights and a threshold value for the neurons in the network, and the program calculates the output of the network for all possible input combinations. If the output matches the expected output for the XOR function, the program confirms that the network has learned the function.
#XOR function using McCulloch-Pitts neural net 
#what is mcCulloch-Pitts neural net? in 1 line A McCulloch-Pitts neural net is a simplified mathematical model of a biological neuron that can perform logical operations and is used as a building block for artificial neural networks.