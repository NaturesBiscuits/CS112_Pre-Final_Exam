print("CS1112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: John Vincent Flores")

while True:
    start = eval(input("\nEnter a number [Start]: "))
    if start == 0:
        print("Program terminated.")
        break
    else:

        while start < 1:
            print("Enter a non-negative number")
            start = eval(input("\nEnter a number [Start]: "))

        end = eval(input("Enter a number [End]: "))
        while start > end:
            print(f"Enter a number greater than {start}")
            end = eval(input("\nEnter a number [End]: "))

        primeList = []

        for calPrime in range(start, end + 1):
            if calPrime > 1:
                for posPrime in range(2, calPrime):
                    if (calPrime % posPrime) == 0:
                        break
                else:
                    primeList.append(calPrime)

        print(f"Prime numbers between {start} and {end} are:", *primeList, sep=' ')