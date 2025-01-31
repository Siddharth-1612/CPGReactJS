def display(data):
    # function to display the biggest number
    print(f"the biggest number is:{data}")

def get_input_and_comp():
    # function to get input
    n1=input("first number is:")
    temp=n1
    vr='n1'
    n2=input("second number is:")
    if n2>temp:
        temp=n2
        vr='n2'
    n3=input("third number is:")
    if n3>temp:
        temp=n3
        vr='n3'
    return (temp,vr)
def main():
    #main function
    maxx=get_input_and_comp()
    display(maxx)
main()    
