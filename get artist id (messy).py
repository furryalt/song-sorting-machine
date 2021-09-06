#if you dont know what this does then how did you find your way into a text editor
import lyricsgenius as genius

#input artist name
print("the output of this command is messy, so i suggest putting it into a text file\nand deleting the artist paragraphs you dont want")
artist = input("artists name\n")
#api key (is this safe to put onto the internet?)
genius = genius.Genius("xB4UsUST9Wx-Ns3emec3xOkK-GhFsWmwFH7tWNBbQjvJrR7nPpYYgPnEcEyFNLWF")

#searches for artists
artist = genius.search_artists(artist)


#sorts output so its a tiny bit more readable, its my best attempt
biblesort1 = str(artist).replace(",", "")
biblesort2 = str(biblesort1).replace("'", "")
biblesort3 = str(biblesort2).replace("(", "")
biblesort5 = str(biblesort3).replace(")", "")
biblesort6 = str(biblesort5).replace("is_meme_verified: False is_verified:", "")
biblesort7 = str(biblesort6).replace("[", "")
biblesort8 = str(biblesort7).replace("]", "")
biblesort9 = str(biblesort8).replace("sections: {type:", "")
biblesort10 = str(biblesort9).replace("slug:", "")
biblesort11 = str(biblesort10).replace("{highlights:  index: artist type: artist result:", "")

#hi phil
print(biblesort11)

