def check_prime(n):
    if(n<=1):
        print("number cannot be prime ")
    i=2
    while(i<int(n**0.5)+1):
            if(n%i==0):
                return False
            i+=1
    return True
def main():
    a=int(input("enter LL"))
    b=int(input("enter UL"))
    if(a>b):
        print("INVLD")
    else:
        for i in range(a,b+1):
            if(check_prime(i)):
                print(i)
main()