def gen_multi_table(number,end):
    for i in range(1, end + 1):
        print(f"{number} x {i} = {number * i}")

def main():
    # Input number and range from user
    number = int(input("Enter the number for the multiplication table: "))
    end = int(input("Enter the ending range: "))
    
    gen_multi_table(number,end)

main()
