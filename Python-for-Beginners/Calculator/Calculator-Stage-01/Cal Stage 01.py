def select_op(choice):
    opt = ["","+","-","*","/","^","%"]
    if choice == "#":
        return 7
    
    elif choice in opt:
        return opt.index(choice)
        
# take input from the user
def getin():
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    
    num = select_op(choice)
    
    if "$" in choice:
        getin()
    elif (num == 7):
    #program ends here
        print("Done. Terminating")
        exit()  
        
            
    elif num in range(1,7):
        
        num1 = input("Enter first number: ")
        print(num1)
        # num2 = input("Enter second numer: ")
        # print(num2)
        if "$" in num1:
            go()
        elif "#" in num1:
            print("Done. Terminating")
            exit()
        num1 = float(num1)
            
        num2 = input("Enter second number: ")
        print(num2)
        if "$" in num2:
            go()
        elif "#" in num2:
            print("Done. Terminating")
            exit()
        num2 = float(num2)
    
        if num == 1:
            print(num1,"+",num2,"=",(num1+num2))
        elif num == 2:
            print(num1,"-",num2,"=",(num1-num2))
        elif num == 3:
            print(num1,"*",num2,"=",(num1*num2))
        elif num == 4:
            if num2 == 0:
                print("float division by zero")
                print(num1,"/",num2,"=","None")
            else:
                print(num1,"/",num2,"=",(num1/num2))
        elif num == 5:
            print(num1,"^",num2,"=",(num1**num2))
        elif num == 6:
            print(num1,"%",num2,"=",(num1%num2))
        else:
            print("Unrecognized operation")
            
def go():           
    while True:
        print("Select operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Terminate: # ")
        print("8.Reset    : $ ")
        getin()
  
go()
  
