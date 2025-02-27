using System;

sealed class SecuritySystem
{
    public void Authenticate() => Console.WriteLine("Authentication Successful");
}


class Program
{
    static void Main()
    {
        SecuritySystem sec = new SecuritySystem();
        sec.Authenticate();
    }
}
