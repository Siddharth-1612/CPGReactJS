using System;

class Product
{
    public string Name { get; set; }
    public double Price { get; set; }

    public Product(string name, double price)
    {
        Name = name;
        Price = price;
    }

    public virtual void GetDiscountedPrice()
    {
        Console.WriteLine($"Product: {Name}, Price: {Price}");
    }
}

class ElectronicProduct : Product
{
    public ElectronicProduct(string name, double price) : base(name, price) { }

    public override void GetDiscountedPrice()
    {
        base.GetDiscountedPrice();
        Console.WriteLine($"For electronics, 15% discount: {Price * 0.85}");
    }
}

class ClothingProduct : Product
{
    public ClothingProduct(string name, double price) : base(name, price) { }

    public override void GetDiscountedPrice()
    {
        base.GetDiscountedPrice();
        Console.WriteLine($"For clothes, 25% discount: {Price * 0.75}");
    }
}

class Program
{
    static void Main()
    {
        ClothingProduct cloth = new ClothingProduct("T-Shirt", 1000);
        ElectronicProduct electronic = new ElectronicProduct("Smartphone", 50000);

        cloth.GetDiscountedPrice();
        Console.WriteLine();
        electronic.GetDiscountedPrice();
    }
}
