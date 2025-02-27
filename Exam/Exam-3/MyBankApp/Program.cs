using System;

class BankAccount
{
    private decimal balance; 

    public BankAccount(decimal initialBalance)
    {
        if (initialBalance < 0)
        {
            throw new ArgumentException("Initial balance cannot be negative.");
        }
        balance = initialBalance;  
    }

    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            balance += amount;
            Console.WriteLine($"Deposited: {amount:C}. New Balance: {balance:C}");
        }
        else
        {
            Console.WriteLine("Deposit must be positive.");
        }
    }

    public void Withdraw(decimal amount)
    {
        if (amount > 0 && amount <= balance)
        {
            balance -= amount;
            Console.WriteLine($"Withdrawn: {amount:C}. New Balance: {balance:C}");
        }
        else
        {
            Console.WriteLine("Invalid withdrawal amount.");
        }
    }

    public void DisplayBalance()
    {
        Console.WriteLine($"Current Balance: {balance:C}");
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Enter initial balance: ");
        decimal initialBalance = Convert.ToDecimal(Console.ReadLine());
        BankAccount account = new BankAccount(initialBalance);

        while (true)
        {
            Console.WriteLine("\nChoose an action: 1-Deposit  2-Withdraw  3-Show Balance  4-Exit");
            string choice = Console.ReadLine();

            if (choice == "1")
            {
                Console.Write("Enter deposit amount: ");
                decimal amount = Convert.ToDecimal(Console.ReadLine());
                account.Deposit(amount);
            }
            else if (choice == "2")
            {
                Console.Write("Enter withdrawal amount: ");
                decimal amount = Convert.ToDecimal(Console.ReadLine());
                account.Withdraw(amount);
            }
            else if (choice == "3")
            {
                account.DisplayBalance();
            }
            else if (choice == "4")
            {
                Console.WriteLine("Exiting...");
                break;
            }
            else
            {
                Console.WriteLine("Invalid choice. Try again.");
            }
        }
    }
}
