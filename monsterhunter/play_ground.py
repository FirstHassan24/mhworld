"""
Python Playground - Practice Exercises
Complete each function according to its docstring.
Run the script to test your solutions!
"""

# ===== Exercise 1: Basic Pattern Matching =====
def describe_number(x):
    """
    Return a description of the number using match-case.
    - If x is 0, return "Zero"
    - If x is 1, 2, or 3, return "Small number"
    - If x is between 4 and 10 (inclusive), return "Medium number"
    - For any other number, return "Big number"
    - If x is not a number, return "Not a number"
    """
    # Your code here:
    # x is the userinput
    match x:
        #checks if the user matches any of these and outputs then return the result:
        case 0:
            return "zero"
        case 1 |2 |3:
            return "small number"
        case 4|5|6|7|8|9|10:
            return "medium number"
        case str():
            return "not a number"
        case _:
            return "Big number"
        

# ===== Exercise 2: Recursive Factorial =====
def factorial(n):
    """
    Calculate the factorial of n using recursion.
    Remember: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    #the number keeps going down everytime its multiplied
    # Your code here:
    if n ==0: #what if n isnt 0?
        return 1
    return n * factorial(n - 1)
def factorial(n):
    print(f"Calculating factorial({n})")
    if n == 0 or n == 1:
        print(f"Base case: factorial({n}) = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"Returning {n} * factorial({n-1}) = {result}")
        return result
    

# ===== Exercise 3: Pattern Matching with Data Structures =====
def process_data(data):
    """
    Process different data structures using pattern matching.
    - If data is a list with one element, return that element
    - If data is a tuple with two elements, return their sum
    - If data is a dictionary with a 'value' key, return that value
    - For anything else, return "Unknown format"
    """
    # Your code here
    pass

# ===== Testing Area =====
if __name__ == "__main__":
    # Test Exercise 1
    print("Testing describe_number():")
    print(f"0: {describe_number(0)}")        # Should print "Zero"
    print(f"2: {describe_number(2)}")        # Should print "Small number"
    print(f"7: {describe_number(7)}")        # Should print "Medium number"
    print(f"42: {describe_number(42)}")      # Should print "Big number"
    print(f"'hello': {describe_number('hello')}")  # Should print "Not a number"
    print()
    
    # Test Exercise 2
    print("Testing factorial():")
    for i in range(6):
        print(f"factorial({i}) = {factorial(i)}")  # Should print factorials from 0! to 5!
    print()
    
    # Test Exercise 3
    # print("Testing process_data():")
    # print(process_data([42]))                # Should print 42
    # print(process_data((10, 20)))           # Should print 30
    # print(process_data({"value": 100}))     # Should print 100
    # print(process_data("something else"))   # Should print "Unknown format
    
    #chat::
    def trace(n):
    print(f"Entering trace({n})")

    if n == 0:
        print("Base case reached! Returning 0")
        return 0

    # recursive call
    result = trace(n - 1)

    print(f"the outer function is waiting for {result}")# ??? ← you fill in this line
    # This line runs AFTER the inner trace(n-1) finishes.

    print(f"Returning from trace({n})")
    return n
