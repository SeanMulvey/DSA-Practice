def main():
    val = input("Enter an integer between 0 and 255 to convert to binary: ")

    if not val.isnumeric():
        print("Enter a valid integer between 0 and 255!")
        main()
    val = int(val)

    if val > 255 or val < 0:
        print("Enter a valid integer between 0 and 255!")
        main()
    print(performCalculation(val))
    main()



def performCalculation(val):
    stack = []
    res = ""
    e = 7
    while e > 0:
        print(val)
        if val - 2**e > 0:
           stack.append("1")
           val -= 2 ** e
        else:
           stack.append("0")
        e -= 1
    
    # while stack:
    #     res += stack.pop()
    return int(stack)
       


main()