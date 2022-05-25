from random import randint
from nextcord import FFmpegPCMAudio
import yt_dlp
import os

def techQuotes():
    files = open(os.path.dirname(os.path.realpath(__file__)) + '/Quotes/' + 'Funnytechquotes.txt', 'r')
    quote = ''
    randomquote = randint(1, 62)
    for counter in range(randomquote):
        quote = files.readline()
    print('\nQuote number ' + str(randomquote) + ' was printed')
    files.close()
    return quote

def seanQuotes():
    files = open(os.path.dirname(os.path.realpath(__file__)) + '/Quotes/' + 'Seanquotes.txt', 'r')
    quote = ''
    randomquote = randint(2, 117)
    for counter in range(randomquote):
        quote = files.readline()
    print('\nSean Quote number ' + str(randomquote) + ' was printed')
    files.close()
    return quote

def oneSeam():
    files = open(os.path.dirname(os.path.realpath(__file__)) + '/Quotes/' + 'Seanquotes.txt', 'r')
    quote = ''
    quote = files.readline()
    print('\nSean Quote number ' + str(1) + ' was printed')
    files.close()
    return quote

class loggerOutputs:
    def error(msg):
        with open('logs.txt', 'a+') as file:
            file.write("Error: " + msg + "\n")
            print("Error: " + msg)
    def warning(msg):
        with open('logs.txt', 'a+') as file:
            file.write("Warning: " + msg + "\n")
            print("Warning: " + msg)
    def debug(msg):
        with open('logs.txt', 'a+') as file:
            file.write("Log: " + msg + "\n")
            print("Log: " + msg)
        
ydl_opts = {
'format': 'bestaudio/best',
'postprocessors': [{
    'key':'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
}]
}

def retrieveAudio(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        title = info.get('title', None)
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    source = FFmpegPCMAudio('song.mp3')
    return source, title

def retrievePlaylist(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        title = info.get('title', None)
    songlist = []
    counter = 0
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song-" + str(counter) +".mp3")
            songlist.append('song-' + str(counter) +'.mp3')
            counter = counter + 1
    print(songlist)
    return songlist, title
    
