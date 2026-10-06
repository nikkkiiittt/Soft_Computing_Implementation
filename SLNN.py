x = float(input("Enter the value of x: "))
w = float(input("Enter the value of weight w: "))
b = float(input("Enter the value of bias b: "))


total = int(w*x+b)

if total <0:
    output = 0
elif total>0 and total<1:
    output = total
else:
    output = 1



print("The total value is: ", total)
print("The output of the SLNN is: ", output)

#simple linear neural network (SLNN) is a type of artificial neural network that consists of a single layer of neurons. It is used for regression tasks, where the goal is to predict a continuous output variable based on one or more input variables. The SLNN takes the weighted sum of the inputs, adds a bias term, and applies an activation function to produce the output. The weights and bias are learned during the training process using optimization algorithms such as gradient descent. The SLNN is a simple yet powerful model that can be used for various applications, including predicting stock prices, weather forecasting, and image recognition.