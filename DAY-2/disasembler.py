import dis
def sum():
    a=1
    b=2
    sum=a+b
    return sum
def sub():
    a=5
    b=2
    sub=a-b
    return sub
def multiply():
    a=3
    b=2
    mul=a*b
    return mul
def div():
    a=3
    b=1
    div=a/b
    return div
def forloop():
    for i in range(1,3):
        i=i+2
def main():
    dis.dis(sum)
    dis.dis(sub)
    dis.dis(multiply)
    dis.dis(div)
    dis.dis(forloop)
main()