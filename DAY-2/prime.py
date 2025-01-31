def check_prime(n):
    if(int(n)<2):
        return False
    if(int(n)==2):
        return True
    if(int(n)%2==0):
        return False
    else:
        for i in range(3,int(n**0.5)+1):
            if(n%i==0):
                return False
    return True
def main():
    x=int(input("Enter the number:"))
    if(check_prime(x)):
        print("It is  prime")
    else:
        print("it is not a prime number")
main()