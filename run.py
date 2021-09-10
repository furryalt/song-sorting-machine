import lyricsgenius as genius
import PySimpleGUI as sg
artistent = [[sg.Text("input artist's name")], [sg.Input(key = "artist_name")], [sg.Text("amount of songs")], [sg.Input(key = "max_songs")], [sg.Button("enter")]]


window = sg.Window('hello', artistent)
count=0

#api key
geniusly = genius.Genius("xB4UsUST9Wx-Ns3emec3xOkK-GhFsWmwFH7tWNBbQjvJrR7nPpYYgPnEcEyFNLWF")
api = genius.Genius("xB4UsUST9Wx-Ns3emec3xOkK-GhFsWmwFH7tWNBbQjvJrR7nPpYYgPnEcEyFNLWF")

#creates GUI window for getting artist name
event, values = window.read()
    
#   get varibles used for searching songs
#artist_name = input("artist name\n")
#number = input("how many songs\n")
#number = int(number)
number = values["max_songs"]
max_songs = values["max_songs"]
artist_name = values["artist_name"]

max_songs = int(max_songs)
#search song
artist = api.search_artist(artist_name, max_songs)

#integrate old sort into this file
#puts songs into text files
for song in artist.songs:
    #input string name
    bible = song.lyrics
    count = int(count) +1
    print(count)
    #makes words lower case
    bible=bible.lower()
    #cleans input words
    biblesort1 = str(bible).replace(",", "")
    biblesort2 = str(biblesort1).replace("?", "")
    biblesort3 = str(biblesort2).replace("(", " ")
    biblesort4 = str(biblesort3).replace("\n", " ")
    biblesort5 = str(biblesort4).replace("\\n", " ")
    biblesort6 = str(biblesort5).replace("\\", " ")
    biblesort7 = str(biblesort6).replace('"', " ")
    biblesort8 = str(biblesort7).replace(")", " ")
    biblesort9 = str(biblesort8).replace("[", " ")
    biblesort10 = str(biblesort9).replace("]", " ")
    biblesort11 = str(biblesort10).replace("-", " ")
    bible = str(biblesort11).replace(")", "")
    
    #sorts words
    bible = bible.split()
    bibletext = bible
    bibletext.sort()
    biblesort = str(bibletext)
    bibletext.sort()
    
    #cleans output words
    biblesort1 = str(bibletext).replace(",", "")
    biblesort2 = str(biblesort1).replace("'", "")
    biblesort3 = str(biblesort2).replace("(", "")
    biblesort5 = str(biblesort3).replace(")", "")
    biblesort6 = str(biblesort5).replace('"', "")
    biblesort7 = str(biblesort6).replace("[", "")
    bibleend = str(biblesort7).replace("]", "")
    
    
    #output varible
    final = bibleend

    weewoo = "final" + str(count) + ".txt"
    #code from the internet im using to output a file
    
    f = open("./output/" + weewoo, 'w')
    f.write(repr(bibleend))
    f.close()
