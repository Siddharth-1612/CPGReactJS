using System;

class Person
{
    protected string Name;
    public Person(string name) => Name = name;
    public virtual void GetDetails() => Console.WriteLine($"Name: {Name}");
}

class Student : Person
{
    private int RollNo;
    public Student(string name, int rollNo) : base(name) => RollNo = rollNo;
    public override void GetDetails() => Console.WriteLine($"Student: {Name}, Roll No: {RollNo}");
}

class Teacher : Person
{
    private string Subject;
    public Teacher(string name, string subject) : base(name) => Subject = subject;
    public override void GetDetails() => Console.WriteLine($"Teacher: {Name}, Subject: {Subject}");
}

class Program
{
    static void Main()
    {
        Person student = new Student("Alice", 101);
        Person teacher = new Teacher("Mr.Bob", "Mathematics");

        student.GetDetails(); // Calls Student's GetDetails()
        teacher.GetDetails(); // Calls Teacher's GetDetails()
    }
}
