using System;
using System.Collections.Generic;

class Book
{
    public string Title { get; }
    public string Author { get; }
    public string ISBN { get; }

    public Book(string title, string author, string isbn)
    {
        Title = string.IsNullOrWhiteSpace(title) ? "Unknown" : title;
        Author = string.IsNullOrWhiteSpace(author) ? "Unknown" : author;
        ISBN = string.IsNullOrWhiteSpace(isbn) ? "N/A" : isbn;
    }

    public void Display() => Console.WriteLine($"Title: {Title}, Author: {Author}, ISBN: {ISBN}");
}

class Program
{
    static void Main()
    {
        Console.Write("Enter number of books: ");
        int count = Convert.ToInt32(Console.ReadLine());

        List<Book> books = new List<Book>();

        for (int i = 1; i <= count; i++)
        {
            Console.WriteLine($"\nBook {i}:");
            Console.Write("Title: ");
            string title = Console.ReadLine();
            Console.Write("Author: ");
            string author = Console.ReadLine();
            Console.Write("ISBN: ");
            string isbn = Console.ReadLine();

            books.Add(new Book(title, author, isbn));
        }

        Console.WriteLine("\nBook List:");
        books.ForEach(book => book.Display());
    }
}
