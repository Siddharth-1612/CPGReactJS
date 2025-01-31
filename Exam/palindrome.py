def is_palindrome(value):
    value = str(value)
    
    start = 0
    end = len(value) - 1
    
    while start < end:
        if value[start] != value[end]:
            return False
        start += 1
        end -= 1
    
    return True

def main():
    while True:
        user_input = input("Enter a string or number to check for palindrome: ")

        if user_input == 'N' or user_input=='n':
            print("Exiting the program.")
            break
        
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is not a palindrome.")

main()
