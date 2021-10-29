import lyricsgenius as genius
import PySimpleGUI as sg
windowcfg = [[sg.Text("input artist's name:")], [sg.Input(key = "artist_name")], [sg.Text("amount of songs:")], [sg.Input(key = "max_songs")], [sg.Checkbox("single output file?", default=True, key="single")], [sg.Checkbox("sort text?", default=True, key="sort")], [sg.Button("enter")]]
window = sg.Window("mercury UwU", windowcfg)
api = genius.Genius("xB4UsUST9Wx-Ns3emec3xOkK-GhFsWmwFH7tWNBbQjvJrR7nPpYYgPnEcEyFNLWF")
event, values = window.read()
finala = ""
count=0
  
#retrive varibles from gui used for searching songs
max_songs = int(values["max_songs"])
artist_name = values["artist_name"]
individual_out = values["single"]
sort = values["sort"]

#search song
artist = api.search_artist(artist_name, max_songs)

for song in artist.songs:
    bible = song.lyrics
    count = int(count) +1
    print(count)
    #makes words lower case
    bible=bible.lower()
    #cleans input words
    biblesort3 = str(bible).replace("(", " ")
    biblesort4 = str(biblesort3).replace("\n", " ")
    biblesort5 = str(biblesort4).replace("\\n", " ")
    biblesort6 = str(biblesort5).replace("\\", " ")
    biblesort7 = str(biblesort6).replace('"', " ")
    biblesort8 = str(biblesort7).replace(")", "")
    biblesort9 = str(biblesort8).replace("[", "")
    biblesort10 = str(biblesort9).replace("]", "")
    bibleprepared = str(biblesort10).replace("-", " ")
    
    if sort:
        #sorts words
        sorter = bibleprepared.split()
        sorter.sort()
        bibletext = str(sorter)
        biblesort1 = str(bibletext).replace(",", "")
        biblesort2 = str(biblesort1).replace("'", "")
        biblesort3 = str(biblesort2).replace("(", "")
        biblesort5 = str(biblesort3).replace(")", "")
        biblesort6 = str(biblesort5).replace('"', "")
        biblesort7 = str(biblesort6).replace("[", "")
        biblesort8 = str(biblesort7).replace("?", "")
        biblesort9 = str(biblesort8).replace(":", "")
        bibleend = str(biblesort9).replace("]", "")
    else:
        bibleend = bibleprepared
    final = bibleend
    
    if individual_out:
        #NOTE TO MY FORGETFULL FUTURE SELF: dumb workaround logic for the api because of the way it handles storing each song
        #but basically, finala = finala(at start is blank) + final(current song stored in sorting system), if you ask for 3 songs
        #lyricsgenius will load in one song, sort it and move on to the next song.... meaning the current sorted song is wiped from memory. 
        #this function accumulates it into one permenant list. DONT REMOVE.
        finala = finala + final
        weewoo = "final.txt"
        f = open("./output/" + weewoo, 'w')
        f.write(repr(finala))
        f.close()
    else:
        weewoo = "final" + str(count) + ".txt"
        f = open("./output/" + weewoo, 'w')
        f.write(repr(bibleend))
        f.close()