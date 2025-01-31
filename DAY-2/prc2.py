def check_prime(n):
    if(n<=1):
        print("number can not be prime")
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return False
        return True
def main():
    a=int(input("enter the lower limit"))
    b=int(input("enter the upper limit"))
    if(a>b):
        print("Invalid range")
    else:
        for i in range(a,b+1):
            if(check_prime(i)):
                print(i)
main()  