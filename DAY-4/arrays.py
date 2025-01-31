def collect(n):
    arr=[]
    i=0
    for i in range(n):
        inp=int(input("enter your number: "))
        arr.append(inp)
    print("your numbers are: ",arr)
def main():
    num=int(input("enter the number of elements: "))
    collect(num)
main()
def main():
    L1=[]
    print("the list is empty",L1)
    L1=[1,2,4,5]
    print("the elements in the list are",L1)
    L1.append(10)
    print("the new list is: ",L1)
    L1=[10,20,30,40]
    print("the 2nd element is: ",L1[2])
    L1=['abc',[10,15,23],'xyz']
    print("the element at L1[1][2] is :",L1[0][2])
    L1=[0,1,2,3,4,5]
    print("the indexed sliced from 2:5 is: ",L1[2:5])
    print("length of the list is: ",len(L1))
    L1=[0,[1,2,3,4],5]
    print("the element at index 0 is:",L1[0])
    print("the element at index [1][3] is:",L1[1][3])
    print("slicing element in the sublist is:",L1[1][2:4])
def main():
    l1=[3,6,2,1,8]
    i=0
    sum=0
    for i in l1:
        sum+=i
    print(sum)
main()
def find_max_min(l1):
    max_elem = float('-inf')
    min_elem = float('inf')
    
    for i in l1:
        if i > max_elem:
            max_elem = i
        if i < min_elem:
            min_elem = i
    
    return max_elem, min_elem

def main():
    num_elements = int(input("Enter the number of elements in the list: "))
    list1 = []  

    for _ in range(num_elements):
        element = int(input("Enter an element: "))  
        list1.append(element)
    
    max_elem, min_elem = find_max_min(list1)
    print(f"Maximum element in the list is: {max_elem}")
    print(f"Minimum element in the list is: {min_elem}")

main()
