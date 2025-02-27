using System;

interface IVehicle
{
    void Drive();
}

class Car : IVehicle
{
    public void Drive() => Console.WriteLine("Driving a car...");
}

class Bike : IVehicle
{
    public void Drive() => Console.WriteLine("Riding a bike...");
}

class VehicleFactory
{
    public static IVehicle GetVehicle(string type)
    {
        return type.ToLower() switch
        {
            "car" => new Car(),
            "bike" => new Bike(),
            _ => throw new ArgumentException("Invalid vehicle type")
        };
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Enter vehicle type (Car/Bike): ");
        string type = Console.ReadLine();

        IVehicle vehicle = VehicleFactory.GetVehicle(type);
        vehicle.Drive();
    }
}
