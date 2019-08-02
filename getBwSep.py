def getBewSeps(instring,sep1,sep2):
    return instring.partition(sep1)[2].partition(sep2)[0]

teststr = r'hello (12345) World'
print(getBewSeps(teststr,'(',')'))
print(teststr.partition('('))
