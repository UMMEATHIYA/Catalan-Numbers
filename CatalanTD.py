# This program is used for the Naive or Top Down Approach for calculating the number of multiplications using Catalan Numbers.
def CatalanTD(n):
    # declaration of a global variable -> multiplication_counter so that it can be accessed outside the function anywhere !
    global multiplication_counter
    # Checking the number of multiplications here ..> only for my use.
    # print(f"global multiplication {n} counter here ", multiplication_counter)

    # inside the function checking for the conditions
    if n == 0:
        return 1
    
    # this block is a recursive call
    total = 0
    for i in range(1, n+1):
        multiplication_counter += 1
        total += CatalanTD(i-1) * CatalanTD(n-i)
    return total

def main():
    # redeclaring the global variable here so that it can be accessed in here and also changed within this block.
    global multiplication_counter
    # taking user input.. Enter a value of n here to computer the Catalan number as well as number of multiplication.
    n = int(input("Enter the value of n: "))
    multiplication_counter = 0

    # calls the method for computation. 
    final_result = CatalanTD(n)

    # prints the final result and the number of multiplications performed.
    print(f" The Catalan number of C({n}) is: ", final_result)
    print(f" The Number of multiplications through a Naive or Top Down Approach is : ", multiplication_counter)


# Calling the main function
if __name__ == "__main__":
    main()