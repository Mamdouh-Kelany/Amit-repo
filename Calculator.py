print ("Welcome to the simple Calculator!")


operation = input("choose your operation please ... [+,-,*,/] : ")



if operation == "+" :
    print ("Addition")
    x = float(input("the 1st number : "))
    y = float(input("the 2nd number : "))
    Addition = x + y
    print (f"{x} + {y} = {Addition}")

elif operation == "-" :
    print ("Subtraction") 
    x = float(input("the 1st number : "))
    y = float(input("the 2nd number : "))  
    Subtraction = x - y    
    print (f"{x} - {y} = {Subtraction}")  

  
elif operation == "*" : 
    print ("Multiplication")  
    x = float(input("the 1st number : "))
    y = float(input("the 2nd number : "))
    Multiplication = x * y    
    print (f"{x} * {y} = {Multiplication}")    
    
elif operation == "/" :
    print ("Division")
    x = float(input("the 1st number : "))
    y = float(input("the 2nd number : "))
    Division = x / y
    print (f"{x} / {y} = {Division}")


else :
    print ("!!! please chose again !!!")
