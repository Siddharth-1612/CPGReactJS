using System;

class Vehicle
{
    public string Brand { get; set; }
    public int Speed { get; set; }

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"Brand: {Brand}, Speed: {Speed} km/h");
    }
}

class Car : Vehicle
{
    

    public override void DisplayInfo()
    {
        base.DisplayInfo(); 
        
    }
}

class Bike : Vehicle
{

    public override void DisplayInfo()
    {
        base.DisplayInfo(); 
        
    }
}

class Program
{
    static void Main()
    {
        Car car = new Car { Brand = "Tesla", Speed = 200};
        Bike bike = new Bike { Brand = "Yamaha", Speed = 150};

        Console.WriteLine("Car Details:");
        car.DisplayInfo();

        Console.WriteLine("\nBike Details:");
        bike.DisplayInfo();
    }
}
