from sys import argv

#input the filename
script,filename = argv

#open the file
txt = open(filename)

print "Here's your file %r:"%filename
#read the file
print txt.read()

txt.close()

print "Type the filename again:"
#input a file name
file_again = raw_input(">")
#open the file
txt_again = open(file_again)
#read the file
print txt_again.read()

txt_again.close()