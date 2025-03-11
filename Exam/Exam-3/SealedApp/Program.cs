using System;

class Account
{
    public virtual void CalculateInterest()
    {
        Console.WriteLine("Calculating interest for a general account.");
    }
}

class SavingsAccount : Account
{
    public sealed override void CalculateInterest()
    {
        Console.WriteLine("Calculating interest for a savings account.");
    }
}

class Program
{
    static void Main()
    {
        SavingsAccount savings = new SavingsAccount();
        savings.CalculateInterest();
    }
}
