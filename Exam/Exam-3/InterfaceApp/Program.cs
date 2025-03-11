using System;

interface IMovable
{
    void Move();
}

class Machine
{
    public void Start()
    {
        Console.WriteLine("Machine started.");
    }
}

class Robot : Machine, IMovable
{
    public void Move()
    {
        Console.WriteLine("Robot is moving.");
    }
}

class Program
{
    static void Main()
    {
        Robot robot = new Robot();
        robot.Start();
        robot.Move();
    }
}
