using System;

interface IDiscountStrategy
{
    decimal ApplyDiscount(decimal total);
}

class NoDiscount : IDiscountStrategy
{
    public decimal ApplyDiscount(decimal total) => total;
}

class PercentageDiscount : IDiscountStrategy
{
    private readonly decimal _percentage;
    public PercentageDiscount(decimal percentage) => _percentage = percentage;
    
    public decimal ApplyDiscount(decimal total) => total - (total * _percentage / 100);
}

class FixedAmountDiscount : IDiscountStrategy
{
    private readonly decimal _amount;
    public FixedAmountDiscount(decimal amount) => _amount = amount;
    
    public decimal ApplyDiscount(decimal total) => total - _amount < 0 ? 0 : total - _amount;
}

class ShoppingCart
{
    private IDiscountStrategy _discountStrategy;

    public void SetDiscountStrategy(IDiscountStrategy discountStrategy)
    {
        _discountStrategy = discountStrategy;
    }

    public void Checkout(decimal total)
    {
        decimal finalTotal = _discountStrategy.ApplyDiscount(total);
        Console.WriteLine($"Total after discount: {finalTotal:C}");
    }
}

class Program
{
    static void Main()
    {
        ShoppingCart cart = new ShoppingCart();

        Console.Write("Enter total amount: ");
        decimal total = Convert.ToDecimal(Console.ReadLine());

        Console.WriteLine("Choose discount type:\n1. No Discount\n2. Percentage Discount\n3. Fixed Amount Discount");
        int choice = Convert.ToInt32(Console.ReadLine());

        switch (choice)
        {
            case 1:
                cart.SetDiscountStrategy(new NoDiscount());
                break;
            case 2:
                Console.Write("Enter discount percentage: ");
                decimal percentage = Convert.ToDecimal(Console.ReadLine());
                cart.SetDiscountStrategy(new PercentageDiscount(percentage));
                break;
            case 3:
                Console.Write("Enter fixed discount amount: ");
                decimal amount = Convert.ToDecimal(Console.ReadLine());
                cart.SetDiscountStrategy(new FixedAmountDiscount(amount));
                break;
            default:
                Console.WriteLine("Invalid choice, applying no discount.");
                cart.SetDiscountStrategy(new NoDiscount());
                break;
        }

        cart.Checkout(total);
    }
}
