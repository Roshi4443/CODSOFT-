print("calculator")
while True:
 print("choose an operation:")
 print("1. Addition ")    
 print("2. Subtraction")        
 print("3. Multiplication")
 print("4. Division")  
 print("5.exit")
 n1 = float(input("enter the first number: "))   # user taking the inputs are numbers and operation 
 n2 = float(input("enter the second number: "))   #the numbers either float or integer but the result will be in float format .
 operation = input("Choose the operation (1, 2, 3, 4,5): ") 

# choose the operation 
 if operation == '1':
    res = n1 + n2
    print(f"The result is: {res}")
 elif operation == '2':
    res = n1 - n2
    print(f"The result is: {res}")
 elif operation == '3':
    res = n1 * n2
    print(f"The result is: {res}")
 elif operation == '4':
    if n2 != 0:
        res = n1 / n2
        print(f"The result is: {res}")
    else:
        print("Error: Division by zero .")
 elif operation == '5':
     print("exit")
     break
 else:
    print("invalid operation .")
