def find_second_largest(numbers):
    largest = second_largest = float('-inf')  
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return "No second largest number found."
    return second_largest

def main():
    
    numbers = []
    n = int(input("Enter the number of elements in the list: "))
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    second_largest = find_second_largest(numbers)
    print("Second largest number:", second_largest)

main()
