 

#   What is the time complexity of this problem? 
#   This formula prints all numbers less than the square root of n


    def foo(n):
        sq_root = int(math.sqrt(n))

        for i in range(0, sq_root):
            print(i)

# Time complexity is O(n^1/2) ( "O of the square root of n")



# Sums up the product of each number pair from 0 to 9
# Double nested for loops

    def bar(n):
        s = 0
        for j in range(n):
            s+= i * j
        return s
# Time complexity is O(n^2)



FIBONACCI

def fib(n, cache=None):
    print(n)
    # cache takes the result of an operation and stores it
    # this reduces the number of operations because they're all done inside of the cache
    if cache is None:
        cache = {}
    # Base case 
    if n <=2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        answer = fib(n-1, cache) + fib(n-2, cache)
        cache[n] = answer
        # Recursive call, should move toward base case
        return answer

#  Time complexity is O(2^n)

#  Fib without cache is in GH repo lol 
