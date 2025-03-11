using System;

class Employee
{
    public string Name { get; set; }
    public int Salary { get; set; }

    public Employee(string Name, int Salary)
    {
        this.Name = Name; 
        this.Salary = Salary;
    }

    public void Display()
    {
        Console.WriteLine($"Employee Name: {Name}, Employee Salary: {Salary} Rs");
    }
}

class Manager : Employee
{
    public int Bonus { get; set; }

    public Manager(string name, int salary, int bonus) : base(name, salary)
    {
        this.Bonus = bonus;  
    }

    public void DisplayManagerInfo()
    {
        Display();  
        Console.WriteLine($"Bonus: {Bonus} Rs");
    }
}

class Program
{
    static void Main()  
    {
        Manager mgr = new Manager("John Doe", 250000, 5000);
        mgr.DisplayManagerInfo();  
    }
}
