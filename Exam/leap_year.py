def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    while True:
        year = int(input("Enter a year to check if it's a leap year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
        
        another_check = input("Do you want to check another year? (yes/no): ")
        if another_check != 'yes':
            break

main()
