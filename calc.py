
con =  "H"
while True:
    number = float(input("choose number"))
    number_2 = float(input("choose second number"))
    print("Print H to stop")
    oper = input("choose operation")
    if oper == "H":
        break
    if oper == "+":
        print(number + number_2)
    elif oper == "-":
        print(number - number_2)
    elif oper == "*":
        print(number * number_2)
    elif oper == "/":
        if number_2 == 0.0:
            print("unable to divide by 0")
        else:
            print(number / number_2)
    else:
        print("error")






