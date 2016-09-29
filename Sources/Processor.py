import re

tweetFile = open('yuchenq_tweets.txt','r')
output_Tweets = open(r'corrected_Tweets.txt', 'w')

locationFile = open('US.txt','r')
output_Locations = open(r'corrected_location.txt', 'w')

s = set()

try:
    for line in tweetFile:
        pattern = re.compile('[^a-zA-Z ]*')
        line = re.sub(pattern, '', line)
        line = line.lower()
        output_Tweets.write(line + '\n')

    for line in locationFile:
        pattern = re.compile('[^a-zA-Z ]*')
        line = re.sub(pattern, '', line)
        line = line.lower()
        s.add(line)
    for L in s:
        output_Locations.write(L + '\n')
    print 'all corrected!'
except Exception as e:
    print ('error happened', e)

tweetFile.close()
output_Tweets.close()
locationFile.close()
output_Locations.close()