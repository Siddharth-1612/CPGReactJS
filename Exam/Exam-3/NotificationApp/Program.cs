using System;
using System.Collections.Generic;

interface INotificationObserver
{
    void ReceiveNotification(string message);
}

class EmailNotifier : INotificationObserver
{
    public void ReceiveNotification(string message)
    {
        Console.WriteLine($"Email received: {message}");
    }
}

class SMSNotifier : INotificationObserver
{
    public void ReceiveNotification(string message)
    {
        Console.WriteLine($"SMS received: {message}");
    }
}

class NotificationService
{
    private List<INotificationObserver> observers = new List<INotificationObserver>();

    public void Subscribe(INotificationObserver observer)
    {
        observers.Add(observer);
    }

    public void NotifyAll(string message)
    {
        foreach (var observer in observers)
        {
            observer.ReceiveNotification(message);
        }
    }
}

class Program
{
    static void Main()
    {
        NotificationService service = new NotificationService();

        EmailNotifier email = new EmailNotifier();
        SMSNotifier sms = new SMSNotifier();

        service.Subscribe(email);
        service.Subscribe(sms);

        service.NotifyAll("You have a new message!");
    }
}
