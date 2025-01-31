def list_palindrome(arr):
    print(arr)
    return arr==arr[::-1]
def take_input():
    return list(input("enter the string: "))
def main():
        str=take_input()
        print(list_palindrome(str))
main()