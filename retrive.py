import lyricsgenius as genius

count=0
ly1="hello"
geniusly = genius.Genius("xB4UsUST9Wx-Ns3emec3xOkK-GhFsWmwFH7tWNBbQjvJrR7nPpYYgPnEcEyFNLWF")
artist_name = input("artist name\n")
number = input("how many songs\n")
number = int(number)

api = genius.Genius("xB4UsUST9Wx-Ns3emec3xOkK-GhFsWmwFH7tWNBbQjvJrR7nPpYYgPnEcEyFNLWF")

artist = api.search_artist(artist_name, max_songs=number)

for song in artist.songs:
    count =count + 1
    print(count)
    ly1 = ly1 + song.lyrics
ly2 =ly1 + str(song.lyrics)
ly3 =ly2
    



    
print(ly3)
f = open( 'abc.txt', 'w' )
f.write(repr(ly3))
f.close()

import sort
