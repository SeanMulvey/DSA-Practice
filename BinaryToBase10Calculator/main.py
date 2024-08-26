def main():
    val = input("Enter an 8-bit binary value to convert: ")
    val = str(val)

    if len(val) != 8:
        print("Enter a valid 8-bit value!")
        main()
    for i in range(len(val)):
        if val[i] != "1" and val[i] != "0":
            print("Enter a valid 8-bit value!")
            main()
    
    print(performCalculation(val))
    main()   

    
def performCalculation(val):
    stack = []
    e = 0
    res = 0
    for i in range(len(val)):
        stack.append(val[i])

    while stack:
        if stack.pop() == "1":
            res += 2 ** e
        e += 1
    return res
main()





