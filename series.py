def fibonacci(n):
    '''Returns the nth value of the Fibonacci sequence

    Important notes that are considered:
    For values of n = 0 or n = 1 is relies on a simple if statements.
    This is required because in a for loop it is impossible to consider these initial two values.
    For example n = 0 given the formula's structure: f(o) = f(-1) + f(-2). It is impossible to use a negative
    value to pull data from the variable "nth"

    '''
    if n == 0:
        print(0)
    if n == 1:
        print(1)

    if n>=2:
        nth = [0]*(n+1) #the 1st value of the array is index with 0 hence why need the "n+1"
        nth[0] = 0
        nth[1] = 1
        for i in range (2,n+1):
            nth[i] = nth[i-1] + nth[i-2]
        print(nth[n])
    pass


def lucas(n):
    if n == 0:
        print(2)
    if n == 1:
        print(1)

    if n>=2:
        nth = [0]*(n+1) #the 1st value of the array is index with 0 hence why need the "n+1"
        nth[0] = 2
        nth[1] = 1
        for i in range (2,n+1):
            nth[i] = nth[i-1] + nth[i-2]
        print(nth[n])
    pass


def sum_series(n, n0=0, n1=1):
    if n == 0:
        print(n0)
    if n == 1:
        print(n1)

    if n>=2:
        nth = [0]*(n+1) #the 1st value of the array is index with 0 hence why need the "n+1"
        nth[0] = n0
        nth[1] = n1
        for i in range (2,n+1):
            nth[i] = nth[i-1] + nth[i-2]
        print(nth[n])


    pass

#print(fibonacci.__doc__) #checking to make sure my docstring works
fibonacci()
sum_series(13)
