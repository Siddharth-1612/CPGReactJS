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
