using System;

interface ILogger
{
    void Log(string message);
}

class FileLogger : ILogger
{
    public void Log(string message)
    {
        Console.WriteLine($"File Log: {message}");
    }
}

class LoggerDecorator : ILogger
{
    protected ILogger _logger;

    public LoggerDecorator(ILogger logger)
    {
        _logger = logger;
    }

    public virtual void Log(string message)
    {
        _logger.Log(message);
    }
}

class TimestampLogger : LoggerDecorator
{
    public TimestampLogger(ILogger logger) : base(logger) { }

    public override void Log(string message)
    {
        string timestampedMessage = $"[{DateTime.Now}] {message}";
        base.Log(timestampedMessage);
    }
}

class ErrorCategoryLogger : LoggerDecorator
{
    private string _category;

    public ErrorCategoryLogger(ILogger logger, string category) : base(logger)
    {
        _category = category;
    }

    public override void Log(string message)
    {
        string categorizedMessage = $"[{_category}] {message}";
        base.Log(categorizedMessage);
    }
}

class Program
{
    static void Main()
    {
        ILogger logger = new FileLogger();

        ILogger timestampLogger = new TimestampLogger(logger);

        ILogger categorizedLogger = new ErrorCategoryLogger(timestampLogger, "ERROR");

        
        categorizedLogger.Log("Something went wrong!");
    }
}
