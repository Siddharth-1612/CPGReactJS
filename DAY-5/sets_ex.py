def main():
    s1={}
    print("this is an empty set: ",s1)
    s1={1,"abc",3.14159}
    print("the new set is: ",s1)
    s1.add("location")
    print("the new set after adding element is : ",s1)
    s1.remove(1)
    print("the set after removing element is: ",s1)
    s2={2,"john",3.8}
    print("the combined set or union is: ",s1|s2)
    s3={'veg:','dal','biryani','curry',}
    s4={'non veg:','chicken','biryani','curry'}
    print("the intersection is: ",s3&s4)    
    l1=[1,2,3,3,2]
    print(f"new set after conversion of {l1} is: ",set(l1))
main()