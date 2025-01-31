def display(name):
    print(f"The student's name is {name}")

def calc_marks(s1, s2, s3, s4, s5):
    total = s1 + s2 + s3 + s4 + s5
    avg = total / 5
    grade = ""
    
    if s1 < 40 or s2 < 40 or s3 < 40 or s4 < 40 or s5 < 40:
        grade = "Fail"
        print("The student has failed in the exam")
    elif avg < 40:
        grade = "Fail"
        print("The student has failed")
    elif avg >= 40 and avg < 60:
        grade = "C"
        print("Grade: C")
    elif avg >= 60 and avg < 80:
        grade = "B"
        print("Grade: B")
    elif avg >= 80 and avg <= 100:
        grade = "A"
        print("Grade: A")

    return total, avg, grade

def main():
    name = input("Enter the name of the student: ")
    display(name)
    
    sub1 = int(input("Enter marks for 1st subject: "))
    sub2 = int(input("Enter marks for 2nd subject: "))
    sub3 = int(input("Enter marks for 3rd subject: "))
    sub4 = int(input("Enter marks for 4th subject: "))
    sub5 = int(input("Enter marks for 5th subject: "))
    
    total, avg, grade = calc_marks(sub1, sub2, sub3, sub4, sub5)
    print(f"Total Marks: {total}")
    print(f"Percentage: {avg:.2f}%")
    print(f"Grade: {grade}")

main()
