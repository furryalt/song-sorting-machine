
#input string name
textdir = input("text name: \n")

#removes txt from name to add it again so that the user can input both foo or foo.txt 
#(bit hacky but best i could do right now)
tempreplace = textdir.replace(".txt", "")
txtdir = tempreplace.replace(tempreplace, tempreplace+".txt")

#reads text file
with open(txtdir) as f:
    bible = f.read()

#makes words lower case
bible=bible.lower()
#cleans input words
biblesort1 = str(bible).replace(",", "")
biblesort2 = str(biblesort1).replace("'", "")
biblesort3 = str(biblesort2).replace("(", "")
bible = str(biblesort3).replace(")", "")

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
biblesort6 = str(biblesort5).replace("", "")
biblesort7 = str(biblesort6).replace("[", "")
biblesort8 = str(biblesort7).replace("]", "")


#remove duplicates


#output varible
final = biblesort8

print(final) 
#code from the internet im using to output a file

f = open( 'final.txt', 'w' )
f.write(repr(biblesort8))
f.close()
