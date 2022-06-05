#for adding the two number
def add(a,b):
    return int(a)+int(b)

#for subtracting the two number
def sub(a,b):
    return int(a)-int(b)

#for multiplying the two number
def mul(a,b):
    return int(a)*int(b)

#for dividing the two number
def div(a,b):
    return float(a)/float(b)

operator=input('Entre the operator "+" or "-" or "*" or "/" ')
num1= input("Enter first number: ")
num2= input("Enter first number: ")


if(operator=="+"):
    print(add(num1,num2))
elif(operator=="-"):
    print(sub(num1,num2))
elif(operator=="*"):
    print(mul(num1,num2))
elif(operator=="/"):
    print(div(num1,num2))
else:
    print("Please Entre valid operator!!!")
