using System;

class Bank
{
    public static double InterestRate { get; private set; } = 5.0;

    public static void SetInterestRate(double rate) => InterestRate = rate;
}

class Program
{
    static void Main()
    {
        Console.WriteLine($"Initial Interest Rate: {Bank.InterestRate}");
        Bank.SetInterestRate(6.5);
        Console.WriteLine($"Updated Interest Rate: {Bank.InterestRate}");
    }
}
