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
