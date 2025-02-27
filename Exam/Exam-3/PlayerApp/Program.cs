using System;

interface IPlayable
{
    void Play();
}

class MusicPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing music...");
    }
}

class VideoPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing video...");
    }
}

class Program
{
    static void Main()
    {
        IPlayable music = new MusicPlayer();
        IPlayable video = new VideoPlayer();

        music.Play();
        video.Play();
    }
}
