def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def Div(x,y):
    return x / y
#vvvvvvvvvvvvvvvvvvvvvvvvrrrr
while True:

    op = input("select your operation : [ + , - , * , / ]) : ")

    if op in ('+','-','*','/'):
        try:
            x = float(input("input num1  : "))
            y = float(input("input num2  : "))
        except ValueError:
            continue
    if op == "+" :
        print (x,"+",y, "=", add(x,y))

    elif op == "-" :
        print (x,"-",y, "=", sub(x,y))
 
    elif op == "*" :
        print (x,"*",y, "=", mult(x,y))
    
    elif op == "/" :
        print (x,"/",y, "=", Div(x,y))
            
    else:
        print ("invaild input")
        
    another_op = input("do you want another operation? (y/n): ")
    
    if another_op == "n":
        break
    

     

         