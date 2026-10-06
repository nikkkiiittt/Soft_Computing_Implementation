n = int(input("Enter the the number of elements : "))

print("Enter the inputs: ")
inputs=[]

for i in range(0, n):
    ele =float(input())
    inputs.append(ele)
print(input)


print("Enter the weights: ")
weights=[]

for i in range(0,n):
    ele = float(input())
    weights.append(ele)
print(weights)

print("the net input is calculated as Yin = x1*w1 + x2*w2 + x3*w3 + ... + xn*wn ")

Yin =[]

for i in range(0,n):
    Yin.append(inputs[i]*weights[i])
    
print(round(sum(Yin),3))

