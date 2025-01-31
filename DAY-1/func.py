def display(data):
    print(f"the area is {data}")

def welcome():
    print("your welcome")

def get_input():
    recieved_length=input("length:")
    recieved_breadth=input("breadth:")
    return(recieved_length,recieved_breadth)

def area(len,brd):
    area=int(len)*int(brd)
    return area
    
def  main():
    welcome()
    (len,brd)=get_input()
    comp_area=area(len,brd)
    display(comp_area)
main()        