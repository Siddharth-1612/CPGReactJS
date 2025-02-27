using System;

class Student
{
    private string name;
    private int rollNo;

    public string Name
    {
        get => name;
        set => name = string.IsNullOrWhiteSpace(value) ? "Unknown" : value;
    }

    public int RollNo
    {
        get => rollNo;
        set => rollNo = value < 0 ? 0 : value;
    }

    public void Display() => Console.WriteLine($"Name: {Name}, Roll No: {RollNo}");
}

class Program
{
    static void Main()
    {
        Student student = new Student();

        Console.Write("Enter Name: ");
        student.Name = Console.ReadLine();

        Console.Write("Enter Roll No: ");
        student.RollNo = Convert.ToInt32(Console.ReadLine());

        student.Display();
    }
}
