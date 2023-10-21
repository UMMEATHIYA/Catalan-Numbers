# This program is using the memoized version or the bottom up approach for computing the number of multiplications using Catalan Number 
# the difference here is.. it keeps track of the number of multiplication and also stores the previously computed values in the array.
# ultimately saves the time to recompute the catalan number recursively, rather fetch it from the stored array.
# Here the number of multiplications performed are lesser when compared to the Naive or the top-down approach.
def CatalanMM(n,C):
    # declaration of a global variable -> multiplication_counter so that it can be accessed outside the function anywhere !
    global multiplication_counter

    # inside the function checking for the conditions
    if n == 0:
        return 1 
    if C[n] != -1:
        return C[n]
    
    # this block is a recursive call
    total = 0
    for i in range(1, n+1):
        multiplication_counter += 1
        total += CatalanMM(i-1, C) * CatalanMM(n-i, C)
    
    C[n] = total
    return total

def main():
    # redeclaring the global variable here so that it can be accessed in here and also changed within this block.
    global multiplication_counter

    # taking user input.. Enter a value of n here to computer the Catalan number as well as number of multiplication.
    n = int(input("Enter the value of n: "))
     
    # the sole purpose for this is it creates a list c of size n+1 filled with -1. This list will be used for memoization. 
    C = [-1] * (n+1)

    # again the multiplication counter is initialized with 0.
    multiplication_counter = 0

    # calls the method for computation.
    result = CatalanMM(n,C)

    # prints the final result and the number of multiplications performed.
    print(f" The {n}th Catalan number is: ", result)
    print(f" The number of multiplications performed ", multiplication_counter)

# Calling the main function
if __name__ == "__main__":
    main()
