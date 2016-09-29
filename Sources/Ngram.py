import re

query_File = open("corrected_location.txt", "r")
output_File = open(r"N_gram_results.txt", "w")

n = 4  # value of n to form ngrams
threshold = 80  # threshold for similarity percentage
noCount = 0

for query in query_File:
    query_list = query.split()
    numPattern = len(zip(*[''.join(query_list)[i:] for i in range(n)]))  # list of ngrams in the pattern query
    lineCount = 0
    tweet_File = open("corrected_Tweets.txt", "r")

    for line in tweet_File:
        words = line.split()
        strings = zip(*[words[i:] for i in range(len(query_list))])
        for token in strings:
            char = ''.join(token)
            substrings = zip(*[char[i:] for i in range(n)])  # list of substrings in the string
            numNgrams = len(substrings)
            queryCount = 0
            for substring in substrings:
                n_gram = ''.join(substring)
                if re.search(n_gram, ''.join(query_list)):  # searching for the presence of ngram in the pattern
                    queryCount += 1

            if numNgrams != 0 and numPattern != 0 and (queryCount * 100 / numPattern) > threshold:
                print 'No.', noCount
                print query
                noCount += 1
                output_File.write("NO." + "%d" % noCount + '\n')
                output_File.write("Query: " + query)
                output_File.write("Similarity: " + str(queryCount * 100 / numPattern) + '%\n')
                output_File.write("Approximate matching: " + ' '.join(token) + '\n')
                tweets = open("yuchenq_tweets.txt", "r")
                tweetCount = 0
                for tweet in tweets:
                    if tweetCount == lineCount and len(tweet.split()) > 1:
                        output_File.write("Tweet's ID: ")
                        output_File.write(str(tweet.split()[1]) + '\n')
                        break
                    tweetCount += 1
                output_File.write("Content: ")
                output_File.write(line + '\n\n')
                tweets.close()
                
        lineCount += 1
    tweet_File.close()
