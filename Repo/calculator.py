def add(num1,num2):
    result=num1+num2
    print(f"Addition of {num1} and {num2} is {result}")
def sub(num1,num2):
    result=num1-num2
    print(f"Subtraction of {num1} and {num2} is {result}")
def mul(num1,num2):
    result=num1*num2
    print(f"Multiplication of {num1} and {num2} is {result}")
def div(num1,num2):
    if num1 or num2==0:
        print("Division by zero")
    else:
        result=num1+num2
        print(f"Addition of {num1} and {num2} is {result}")
print("-------ARITHMETIC CALCULATOR--------")
num1=int(input("\nEnter number 1 :"))
num2=int(input("\nEnter number 2 :"))
choice=int(input("\nEnter your choice : 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n"))
if choice==1:
    add(num1,num2)
elif choice==2:
    sub(num1,num2)
elif choice==3:
    mul(num1,num2)
elif choice==4:
    div(num1,num2)
else:
    print("Invalid choice")