def split_bill(total_amount, num_people, tip_percentage):
   
    total_with_tip = total_amount + (total_amount * tip_percentage / 100)
    amount_per_person = total_with_tip / num_people
    return total_with_tip, amount_per_person

def main():
    total_amount = float(input("Enter the total bill amount : "))

    num_people = int(input("Enter the number of people: "))
    
    tip_percentage = float(input("Enter the tip percentage: "))

    if num_people <= 0:
        print("Number of people must be greater than 0.")
        return
    
    total_with_tip, amount_per_person = split_bill(total_amount, num_people, tip_percentage)
    

    print(f"Total bill (including tip): {total_with_tip:.2f}")
    print(f"Amount each person has to pay: {amount_per_person:.2f}")

main()
