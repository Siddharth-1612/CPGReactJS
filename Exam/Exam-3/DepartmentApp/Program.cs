using System;

class Manager
{
    public string Name { get; set; }
}

class Department
{
    public string Name { get; set; }
    public Manager DeptManager { get; set; }

    public Department ShallowCopy()
    {
        return (Department)this.MemberwiseClone();
    }

    public Department DeepCopy()
    {
        return new Department
        {
            Name = this.Name,
            DeptManager = new Manager { Name = this.DeptManager.Name }
        };
    }
}

class Program
{
    static void Main()
    {
        Department original = new Department { Name = "HR", DeptManager = new Manager { Name = "Alice" } };

        Department shallowCopy = original.ShallowCopy();
        Department deepCopy = original.DeepCopy();

        original.DeptManager.Name = "Bob";

        Console.WriteLine($"Original Manager: {original.DeptManager.Name}");
        Console.WriteLine($"Shallow Copy Manager: {shallowCopy.DeptManager.Name}");
        Console.WriteLine($"Deep Copy Manager: {deepCopy.DeptManager.Name}"); 
    }
}
