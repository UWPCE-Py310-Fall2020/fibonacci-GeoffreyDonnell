def fibonacci(n):
    '''Returns the nth value of the Fibonacci sequence

    Important notes that are considered:
    For values of n = 0 or n = 1 is relies on a simple if statements.
    This is required because in a for loop it is impossible to consider these initial two values.
    For example n = 0 given the formula's structure: f(o) = f(-1) + f(-2). It is impossible to use a negative
    value to pull data from the variable "nth"

    '''
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n>=2:
        nth = [0]*(n+1) #the 1st value of the array is index with 0 hence why need the "n+1"
        nth[0] = 0
        nth[1] = 1
        for i in range (2,n+1):
            nth[i] = nth[i-1] + nth[i-2]
        return nth[n]
    pass

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1

    if n>=2:
        nth = [0]*(n+1) #the 1st value of the array is index with 0 hence why need the "n+1"
        nth[0] = 2
        nth[1] = 1
        for i in range (2,n+1):
            nth[i] = nth[i-1] + nth[i-2]
        return nth[n]
    pass

def sum_series(n, n0=0, n1=1):
    if n == 0:
        return n0
    if n == 1:
        return n1

    if n>=2:
        nth = [0]*(n+1) #the 1st value of the array is index with 0 hence why need the "n+1"
        nth[0] = n0
        nth[1] = n1
        for i in range (2,n+1):
            nth[i] = nth[i-1] + nth[i-2]
        return nth[n]
    pass

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")