def separate_odd_even(numbers):
    odd = []
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd, even

def main():
    n = int(input("Enter the number of elements: "))  
    numbers = []
    print(f"Enter {n} numbers:")
    for i in range(n):
        num = int(input())  
        numbers.append(num)  
    
    odd, even = separate_odd_even(numbers)
    print("Odd numbers:", odd)
    print("Even numbers:", even)

main()
