using System;

class User
{
    public string Username { get; set; }
    public string Role { get; set; }

    public virtual void AccessControl() => Console.WriteLine("General User Access");
}

class Admin : User
{
    public override void AccessControl() => Console.WriteLine("Admin: Full Access Granted");
}

class Customer : User
{
    public override void AccessControl() => Console.WriteLine("Customer: Limited Access");
}

class Program
{
    static void Main()
    {
        User user1 = new Admin { Username = "AdminUser" };
        User user2 = new Customer { Username = "RegularCustomer" };

        user1.AccessControl();
        user2.AccessControl();
    }
}
