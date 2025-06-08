from sys import breakpointhook

while True :
    num1 = int(input("enter num1 "))
    oper = input("enter operation +-*/ ")
    num2 = int(input("enter num1 "))
    def numb (  ):
        if oper == "+" :
            return num1 + num2
        elif oper == "-" :
            return num1 - num2
        elif oper == "*" :
            return num1 * num2
        elif oper == "/" :
            return num1 / num2
        else :
            return breakpointhook(1)

    print (numb (  ))



