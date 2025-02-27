using System;

abstract class Shape
{
    public abstract double CalculateArea();
}

class Circle : Shape
{
    private double radius;

    public Circle(double radius) => this.radius = radius;

    public override double CalculateArea() => Math.PI * radius * radius;
}

class Rectangle : Shape
{
    private double breadth, length;

    public Rectangle(double breadth, double length)
    {
        this.breadth = breadth;
        this.length = length;
    }

    public override double CalculateArea() => breadth * length;
}

class Program
{
    static void Main()
    {
        Console.Write("Enter circle radius: ");
        double r = Convert.ToDouble(Console.ReadLine());
        Shape circle = new Circle(r);

        Console.Write("Enter rectangle breadth: ");
        double w = Convert.ToDouble(Console.ReadLine());
        Console.Write("Enter rectangle length: ");
        double h = Convert.ToDouble(Console.ReadLine());
        Shape rectangle = new Rectangle(w, h);

        Console.WriteLine($"\nCircle Area: {circle.CalculateArea()}");
        Console.WriteLine($"Rectangle Area: {rectangle.CalculateArea()}");
    }
}
