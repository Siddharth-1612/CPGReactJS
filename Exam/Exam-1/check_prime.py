def check_prime(n):
    if(n<=1):
        return False
    for i in range(2,int(n**(0.5)+1)):
        if(n%i==0):
            return False
    return True
def main():
    a1=int(input("enter the first number of range"))
    b1=int(input("enter the last number of range"))
    if(b1>a1):
        for i in range(a1,b1+1):
            if(check_prime(i)):
                print(i)
    else:
        print("The lower limit is greater than upper limit")
main()