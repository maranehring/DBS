import unicodecsv

with open('hashtag.csv', 'r') as inp, open('hashtag3.csv', 'w') as out:
    writer = unicodecsv.writer(out, delimiter=';',lineterminator='\n', encoding='ISO-8859-1')
    stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')
    dict_tweets={}
    dict_retweets = {}
    dict_likes={}
    #defining three dictionaries
    # here we will count the number of tweets one hashtag occurs in
    for row in stuff:
        try:
            if row[13]!="Hashtag": #make sure we don't count the header as an entry for the dictionary
                for i in range (13,19):

                    if row[i] in dict_tweets:
                        dict_tweets[row[i]]+=1 #if the hashtag is already in the dictionary, increase the counter by 1
                    else:
                        dict_tweets[row[i]]=1 #else create a new key "name of hashtag" with the value 1
        except IndexError:
            pass

    k1 = dict_tweets.keys()
    v1 = dict_tweets.values()

    inp.seek(0) # put the cursor at the beginning of the reader file, so we can use it again
    #here we will count the number of total retweets a of a tweet with the hashtag
    for row in stuff:
        if not row[7] == "retweet_count": #make sure we don't count the header as an entry for the dictionary
            try:
                for i in range(13, 19):

                    if row[i] in dict_retweets:
                        dict_retweets[row[i]] = dict_retweets[row[i]] + int(row[7]) #if the hashtag is already in the dictionary, increase the counter by the number of retweets
                    else:
                        dict_retweets[row[i]] = int(row[7]) #else create a new key "name of hashtag" with the value nr_retweets
            except IndexError:
                pass

    k2 = dict_retweets.keys()
    v2 = dict_retweets.values()

    inp.seek(0)# put the cursor at the beginning of the reader file, so we can use it again
    #here we will count the number of total retweets a of a tweet with the hashtag
    for row in stuff:
        if not row[8] == "favorite_count": #make sure we don't count the header as an entry for the dictionary
            try:
                for i in range(13, 19):

                    if row[i] in dict_likes:
                        dict_likes[row[i]] = dict_likes[row[i]] + int(row[8]) #if the hashtag is already in the dictionary, increase the counter by the number of likes
                    else:
                        dict_likes[row[i]] = int(row[8]) #else create a new key "name of hashtag" with the value nr_likes
            except IndexError:
                pass

    k3 = dict_likes.keys()
    v3 = dict_likes.values()

    #write the entries in a new csv file
    for i in range (0, len(k1)):
        list1=[k1[i],v1[i],v2[i],v3[i]]
        writer.writerow(list1)
