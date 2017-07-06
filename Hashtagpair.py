import unicodecsv

with open('hashtag.csv', 'r') as inp, open('hplikes.csv', 'w') as out:
    writer = unicodecsv.writer(out, delimiter=';', lineterminator='\n', encoding='ISO-8859-1')
    stuff = unicodecsv.reader(inp, delimiter=';', encoding='ISO-8859-1')
    dict_tweets = {}
    dict_retweets = {}
    dict_likes = {}
    m = []
    # defining three dictionaries
    # here we will count the number of tweets one hashtag occurs in
    for row in stuff:
        try:
            if row[13] != "Hashtag":  # make sure we don't count the header as an entry for the dictionary
                l = []
                try:
                    if row[14] != "":
                        l.append((row[13], row[14]))
                        try:
                            if row[15] != "":
                                l.append((row[13], row[15]))
                                l.append((row[14], row[15]))
                            try:
                                if row[16] != "":
                                    l.append((row[13], row[16]))
                                    l.append((row[14], row[16]))
                                    l.append((row[15], row[16]))
                                try:
                                    if row[17] != "":
                                        l.append((row[13], row[17]))
                                        l.append((row[14], row[17]))
                                        l.append((row[15], row[17]))
                                        l.append((row[16], row[17]))
                                    try:
                                        if row[18] != "":
                                            l.append((row[13], row[18]))
                                            l.append((row[14], row[18]))
                                            l.append((row[15], row[18]))
                                            l.append((row[16], row[18]))
                                    except IndexError:
                                        pass
                                except IndexError:
                                    pass
                            except IndexError:
                                pass
                        except IndexError:
                            pass
                        for i in range(0, len(l)):
                            if l[i] in dict_tweets:
                                dict_tweets[
                                    l[i]] += 1  # if the hashtag is already in the dictionary, increase the counter by 1
                            else:
                                dict_tweets[l[i]] = 1  # else create a new key "name of hashtag" with the value 1

                            if l[i] in dict_retweets:
                                dict_retweets[l[i]] = (dict_retweets[l[i]] + int(row[
                                                                                     7]))  # if the hashtag is already in the dictionary, increase the counter by the number of retweets
                            else:
                                try:
                                    dict_retweets[l[i]] = int(
                                        row[7])  # else create a new key "name of hashtag" with the value nr_retweets
                                except ValueError:
                                    pass

                except IndexError:
                    pass


        except IndexError:
            pass
    n = []
    k1 = dict_tweets.keys()
    v1 = dict_tweets.values()
    k2 = dict_retweets.keys()
    v2 = dict_retweets.values()
    dict_tweets2 = {}
    dict_retweets2 = {}
    for i in range(0,len(k2)):
        j = []
        l1 = k1[i][0]
        l2 = k1[i][1]
        j.append(l1)
        j.append(l2)
        if sorted(j) not in m:
            dict_tweets2[k1[i]] = 1
            print k1[i]
      
