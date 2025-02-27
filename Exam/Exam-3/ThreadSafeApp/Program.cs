using System;

class ConfigurationManager
{
    private static ConfigurationManager _instance;
    private static readonly object _lock = new object();

    private ConfigurationManager() { }

    public static ConfigurationManager GetInstance()
    {
        if (_instance == null)
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new ConfigurationManager();
                    Console.WriteLine("New ConfigurationManager instance created.");
                }
            }
        }
        return _instance;
    }
}

class Program
{
    static void Main()
    {
        ConfigurationManager config1 = ConfigurationManager.GetInstance();
        ConfigurationManager config2 = ConfigurationManager.GetInstance();

        Console.WriteLine(config1 == config2); 
    }
}
