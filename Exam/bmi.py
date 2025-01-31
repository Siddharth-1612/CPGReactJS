def calc_bmi(wt,ht):
    ht2=ht*ht
    bmi=float(wt/ht2)
    print(bmi)
    if bmi<18.5:
        print("You are unfortunately underweight :((")
    elif bmi>=18.5 and bmi<=24.9:
        print("Congratulations you are healthy!!!")
    else:
        print("You are Overweight,recommend you to exercise")
        
def main():
    weight=float(input("enter the weight of the person in kg: "))
    height=float(input("enter the height of the person in metres: "))
    calc_bmi(weight,height)
main()