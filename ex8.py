formatter = "%s %s %s %s"

print formatter % (1,2,3,4)
print formatter % ("one what the fuck.","two what the fuck.","three what't the fuck.","four what the fuck.")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ("I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight.")
print formatter % ("I had this thing.","But it didn't sing.","That you could type up right.","So I said goodnight.")