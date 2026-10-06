
num_ip = int(input("Enter the number of inputs: "))


w1 = 1
w2 = 1

print(f"For the {num_ip} inputs, calculate the net input using Yin = x1*w1 + x2*w2")


x1 = []
x2 = []


for j in range(num_ip):
    ele1 = int(input("x1 = "))
    ele2 = int(input("x2 = "))
    x1.append(ele1)
    x2.append(ele2)


print("x1 = ", x1)
print("x2 = ", x2)


n = [x * w1 for x in x1]
m = [x * w2 for x in x2]

Yin = [n[i] + m[i] for i in range(num_ip)]

print("Yin = ", Yin)


n = [x * w1 for x in x1]
m = [x * (-w2) for x in x2]


Yin = [n[i] + m[i] for i in range(num_ip)]

print("After assuming one weight as excitatory and the other as inhibitory, Yin = ", Yin)


Y = []

for i in range(num_ip):
    if Yin[i] >= 1:
        Y.append(1)
    else:
        Y.append(0)


print("Y = ", Y)

#the theory part for viva quetion
#this code is a simple implementation of a perceptron model that takes two inputs and calculates the net input (Yin) using weights (w1 and w2). It then applies a threshold function to determine the output (Y) based on whether Yin is greater than or equal to 1. The code also demonstrates how to handle excitatory and inhibitory weights by negating one of the weights.
#the method used in this code is the perceptron learning algorithm, which is a supervised learning algorithm used for binary classification tasks. The code calculates the net input (Yin) by multiplying each input by its corresponding weight and summing the results. It then applies a threshold function to determine the output (Y) based on whether Yin is greater than or equal to 1. The code also demonstrates how to handle excitatory and inhibitory weights by negating one of the weights.