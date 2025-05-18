from matplotlib.dates import num2timedelta

print("1 = add")
print("2 = subtract")
print("3 = multply")
print("4 = divide")
print("5 = modulase")
option = int(input("choose on operation: "))
if(option in [1,2,3,4]):
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second  number"))
    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 // num2
    elif(option == 5):
        result = num1 % num2

print("the result is {}".format(result))


