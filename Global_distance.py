def global_distance(str1, str2, length = 1):
    """Calculate the Global distance from String 1 to String 2 via Needleman Wunsch algorithm."""
    len1 = len(str1)
    len2 = len(str2)
    array_a = [[0] * (len2 + 1) for j in range(len1 + 1)]

    for i in xrange(len1 + 1):
        for j in xrange(len2 + 1):
            if min(i, j) == 0:
                array_a[i][j] = max(i, j)
            else:
                add_value = 0 if str1[i-1] == str2[j-1] else length
                array_a[i][j] = min(array_a[i-1][j-1] + add_value,array_a[i-1][j] + 1,array_a[i][j-1] + 1)

    return array_a[len1][len2]


query_File = open("corrected_location.txt", "r")
output_File = open(r"Global_distance_results.txt", "w")
# threshold = 35  # threshold for dissimilar percentage
threshold = 80
numCount = 0

for query in query_File:
    queryCount = 0
    query_list = query.split()
    Tweet_file = open("corrected_Tweets.txt", "r")
    for line in Tweet_file:
        words = line.split()
        tokens = zip(*[words[i:] for i in range(len(query_list))])

        for i in range(0, len(tokens)):
            dissimilar = []
            for j in range(0, len(query_list)):
                dissimilar.append(((global_distance(query_list[j], tokens[i][j])) * 100) / len(query_list[j]))
            dissimilarity = sum(dissimilar) / len(dissimilar)
            similarity = 100 - dissimilarity

            if similarity >= threshold:
                print 'No.', numCount
                print query
                numCount += 1
                output_File.write("NO." + "%d" % numCount + '\n')
                output_File.write("Query: " + query)
                output_File.write("Similarity: " + str(similarity) + '%\n')
                output_File.write("Approximate matching: " + ' '.join(tokens[i]) + '\n')
                original_tweets = open("yuchenq_tweets.txt", "r")
                tweetCount = 0

                for tweet in original_tweets:
                    if tweetCount == queryCount and len(tweet.split()) > 1:
                        output_File.write("Tweet's ID: ")
                        output_File.write(str(tweet.split()[1]) + '\n')
                        break
                    tweetCount += 1
                output_File.write("Content: ")
                output_File.write(line + '\n\n')
                original_tweets.close()

    queryCount += 1
Tweet_file.close()
