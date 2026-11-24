a=int(input("Enter The Value of A  \t"))
b=int(input("Enter the value of B  \t"))
print(" 1 = +\n 2 = -\n 3 = * \n 4 = /\n")
n=int(input('what you want to calculate \t'))
match n:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("Invalid choice")