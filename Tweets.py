dictionary = {}
times = []
hashes = []

firsttag = 0
secondtag = 0
thirdtag = 0

s = [[200908041311,'I love puppies and cats equally #cats #dogs. Happy Friday! #Ilovefridays!'], [2014071220,'Brazil looks really bad #WorldCup2014'], [2012010101,'Happy New Year everybody!']]
def compileHashTags(s):
    for count in range(len(s)):
        string = s[count][1]
        q = range(len(s[count][1]))
        y = string.replace('.',' ')
        x = y.replace(',',' ')
        timeCount = 0
        for q in range(len(x)):

            
            
            if x[q] == '#':
                
                counter = 1
                tags = []
                hashtag = None
                while x[q+counter] != ' ' :
                    
                    if q+counter == len(x)-1:
                        hashtag = x[q+1:q+counter+1]
                        pass
                        break
                    else:
                        counter += 1
                        hashtag = x[q+1:q+counter]
                dictionary[hashtag] = s[count][0]
                hashes.append(hashtag)
    print(dictionary)
            




def extractHashTags(s):    #this code took me 5 hours
    string = s
    q = range(len(s))
    z = string.replace('.',' ')
    x = z.replace(',',' ')
    
    for q in range(len(x)):
        if x[q] == '#':
            counter = 1
            tags = []
            
            while x[q+counter] != ' ' :
                if q+counter == len(x)-1:
                    hashtag = x[q+1:q+counter+1]
                    pass
                    break
                else:
                    counter += 1
                    hashtag = x[q+1:q+counter]
            hashes.append(hashtag)
    return hashes

