print("\n========CALCULATOR========\n\n")
calc="y"

while(calc=='y'):
    #user input for calculation
    n1=int(input("Enter first number :"))
    n2=int(input("Enter second number :"))

    #operator input from(+,-,*,/,%,**)
    operator=input("Enter Methmatical operator(+,-,*,/,**,%) :")

    if operator=='+':
        print(n1,"+",n2,"=",n1+n2)
    elif operator=='-':
        print(n1,"-",n2,"=",n1-n2)
    elif operator=='*':
        print(n1,"x",n2,"=",n1*n2)
    elif operator=='/':
        print(n1,"/",n2,"=",round(n1/n2,24))
    elif operator=='%':
        print(n1,"%",n2,"=",n1%n2)

        
    elif operator=='**':
        print(n1,"**",n2,'=',n1**n2)
    else:
        print("Invalid Input....")
    print('\n\n')
    calc=input("Enter 'Y' for more cacuation :").lower()
    print('\n')

print("\n===========================\n")