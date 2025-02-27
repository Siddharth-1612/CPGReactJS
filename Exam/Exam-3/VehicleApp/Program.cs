using System;

class Vehicle
{
    public virtual void Start() => Console.WriteLine("Vehicle is starting...");
}

class Car : Vehicle
{
    public override void Start() => Console.WriteLine("Car is starting...");
}

class Bike : Vehicle
{
    public override void Start() => Console.WriteLine("Bike is starting...");
}

class Program
{
    static void Main()
    {
        Vehicle car = new Car();
        Vehicle bike = new Bike();

        car.Start();  // Calls Car's Start()
        bike.Start(); // Calls Bike's Start()
    }
}
