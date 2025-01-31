def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i  
    return result

def main():
    fact = int(input("Enter your number: "))
    if fact == 0 or fact == 1:
        return 1  
    elif fact < 0:
        print("Enter a valid non-negative number")
    else:
        return factorial(fact)  # Call factorial function and return the result

# Call the main function
result = main()
if result is not None:  
    print("Factorial:", result)
