﻿using System;

interface IPrintable
{
    void Print();
}

interface ISerializable
{
    void Save();
}

class Report : IPrintable, ISerializable
{
    public void Print() => Console.WriteLine("Printing Report...");
    public void Save() => Console.WriteLine("Saving Report...");
}

class Program
{
    static void Main()
    {
        Report report = new Report();
        report.Print();
        report.Save();
    }
}
