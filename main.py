
while True:
    n, m = map(int, input("\nEnter the 2 numbers separated with space\n").split())
    ch = int(input("\nEnter 1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for exit\n"))
    if ch == 1:
        print("The sum of ", n, " and ", m, " is ", n + m)
    elif ch == 2:
        print("The difference of ", n, " and ", m, " is ", n - m)
    elif ch == 3:
        print("The product of ", n, " and ", m, " is ", n * m)
    elif ch == 4:
        print("The quotient of ", n, " and ", m, " is ", n / m)
    else:
        exit(0)
