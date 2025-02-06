def loan_approval(sal,age,credit):
    if age<18:
        print("Sorry you are underage you cant get a loan")
    elif sal<25000:
        print("Sorry your salary is below the loan approval limit")
    elif credit<700:
        print("sorry you have a low credit score")
    else:
        print("Congratulations your loan has been approved")
def main():
    salary=int(input("Please enter your monthly salary: "))
    age=int(input("Please enter your age: "))
    credit_score=int(input("Please enter your credit score: "))
    loan_approval(salary,age,credit_score)
main()
