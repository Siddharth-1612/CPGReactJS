def fibonacci(n):
    n1=0
    n2=-1
    sum=0
    for sum in range(n1,n+1):
        sum=n1+n2
        n1=n2
        n2=sum
    return sum
def main():
    num=input("enter your number: ")
    fibonacci(num)
main()