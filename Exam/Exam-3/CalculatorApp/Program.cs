using System;

class Calculator
{
    public int Add(int a, int b) => a + b;
    public int Add(int a, int b, int c) => a + b + c;
    public double Add(double a, double b) => a + b;
}

class Program
{
    static void Main()
    {
        Calculator calc = new Calculator();
        Console.WriteLine(calc.Add(2, 3));          
        Console.WriteLine(calc.Add(1, 2, 3));      
        Console.WriteLine(calc.Add(2.5, 3.5));     
    }
}
