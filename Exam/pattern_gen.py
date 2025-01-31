def print_pattern(n, reverse=False):
    if reverse:
        for i in range(n, 0, -1):
            print('*' * i)
    else:
        for i in range(1, n + 1):
            print('*' * i)

def main():
    n = int(input("Enter the number of rows: "))
    reverse = input("Do you want the pattern in reverse? (yes/no): ").lower()
    
    print_pattern(n, reverse == 'yes')

main()
