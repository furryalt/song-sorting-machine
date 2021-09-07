

sortvar1 = "\n"
sortvar2 = "\\n"
#input string name
txtdir = "abc.txt"

#reads text file
with open(txtdir) as f:
    bible = f.read()

#makes words lower case
bible=bible.lower()
#cleans input words
biblesort1 = str(bible).replace(",", "")
biblesort2 = str(biblesort1).replace("'", "")
biblesort3 = str(biblesort2).replace("(", "")
biblesort4 = str(biblesort3).replace(sortvar2, " ")
biblesort5 = str(biblesort4).replace(sortvar1, "")
biblesort6 = str(biblesort5).replace("\\", "")
biblesort7 = str(biblesort6).replace('"', "")
biblesort8 = str(biblesort7).replace(")", "")
biblesort9 = str(biblesort8).replace("[", "")
biblesort10 = str(biblesort9).replace("]", "")
biblesort11 = str(biblesort10).replace("-", "")
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
biblesort6 = str(biblesort5).replace("", "")
biblesort7 = str(biblesort6).replace("[", "")
bibleend = str(biblesort7).replace("]", "")


#output varible
final = bibleend

print(final) 
#code from the internet im using to output a file

f = open( 'final.txt', 'w' )
f.write(repr(bibleend))
f.close()
