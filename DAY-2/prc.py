def display(data):
    print(f"the biggest number is:{data}")

def comp():
    n1=int(input("enter the first number:"))
    temp=n1
    var='n1'
    n2=int(input("enter the sec number:"))
    if(n2>temp):
        temp=n2
        var='n2'
    n3=int(input("enter the third number:"))
    if(n3>temp):
        temp=n3
        var='n3'
    return temp,var
def main():
    maxx=comp()
    display(maxx)
main()