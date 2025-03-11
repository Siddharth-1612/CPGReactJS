using System;

class Vehicle
{
    public string Brand { get; set; }  
    public int Speed { get; set; }     

    public void DisplayInfo()
    {
        Console.WriteLine($"Brand: {Brand}, Speed: {Speed} km/h"); 
    }
}

class Car : Vehicle
{
    public Car(string brand, int speed)
    {
        Brand = brand;
        Speed = speed;
    }

    public void CarDetails()
    {
        Console.WriteLine("Car Details:");
        DisplayInfo();  
    }
}

class Bike : Vehicle
{
    public Bike(string brand, int speed)
    {
        Brand = brand;
        Speed = speed;
    }

    public void BikeDetails()
    {
        Console.WriteLine("Bike Details:");
        DisplayInfo();  
    }
}

class Program
{
    static void Main()
    {
        Car myCar = new Car("Toyota", 180);
        myCar.CarDetails();

        Console.WriteLine();

        Bike myBike = new Bike("Yamaha", 120);
        myBike.BikeDetails();
    }
}
