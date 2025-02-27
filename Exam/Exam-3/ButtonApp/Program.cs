using System;

class Button
{
    public delegate void ClickHandler();
    public event ClickHandler OnClick;

    public void Click()
    {
        Console.WriteLine("Button clicked!");
        OnClick?.Invoke();
    }
}

class Program
{
    static void Main()
    {
        Button button = new Button();

        button.OnClick += () => Console.WriteLine("Action executed on button click!");

        button.Click();
    }
}
