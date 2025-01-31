def display(data):
    print(f"the average is:{data}")

def get_input():
    n1=input("first number is:")
    n2=input("second number is:")
    n3=input("third number is:")
    n4=input("fourth number is:")
    return int(n1),int(n2),int(n3),int(n4)

def comp_sum(n1,n2,n3,n4):
    comp_sum=int(n1)+int(n2)+int(n3)+int(n4)
    return comp_sum

def comp_avg(comp_sum):
    comp_avg=(comp_sum)/4
    return comp_avg

def main():
    (n1,n2,n3,n4)=get_input()
    sum=comp_sum(n1,n2,n3,n4)
    avg=comp_avg(sum)
    display(avg)
main()