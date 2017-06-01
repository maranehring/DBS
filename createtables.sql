CREATE TABLE IF NOT EXISTS TWEET (
                ID INTEGER,
                tText TEXT,
                nr_retweets INTEGER,
                nr_likes INTEGER,
                is_retweet BOOLEAN NOT NULL,
                has_hashtag BOOLEAN NOT NULL,
                person BOOLEAN,
                Ti_ID INTEGER NOT NULL,
                PRIMARY KEY (ID), 
                FOREIGN KEY(Ti_ID) REFERENCES TIME (Ti_ID),
                FOREIGN KEY(person) REFERENCES CANDIDATE (Nr)
)

CREATE TABLE IF NOT EXISTS CANDIDATE (
                Nr BOOLEAN,
                Name VARCHAR(15),
                PRIMARY KEY(Nr)
)


CREATE TABLE IF NOT EXISTS TIME (
                Ti_ID INTEGER,
                Date DATE,
                t_of_day TIME,
                PRIMARY KEY (Ti_ID)           
)

CREATE TABLE IF NOT EXISTS HASHTAG (
                text TEXT,
                nr_tweets INTEGER,
                nr_retweets INTEGER,
                nr_likes INTEGER,
                PRIMARY KEY (text)           
)

CREATE TABLE IF NOT EXISTS HASHTAGPAIR (
                pairText TEXT,
                nr_tweets INTEGER,
                nr_retweets INTEGER,
                nr_likes INTEGER,
                PRIMARY KEY (pairText)           
)

CREATE TABLE IF NOT EXISTS uses(
                ID INTEGER,
                text TEXT,
                PRIMARY KEY (ID, text),
                FOREIGN KEY(text) REFERENCES HASHTAG (text),
                FOREIGN KEY(text) REFERENCES HASHTAGPAIR (pairText),
                FOREIGN KEY(ID) REFERENCES TWEET (ID)
)

CREATE TABLE IF NOT EXISTS is_used_at(
                text TEXT,
                Ti_ID INTEGER,
                PRIMARY KEY (text, Ti_ID),  
                FOREIGN KEY(text) REFERENCES HASHTAG (text),
                FOREIGN KEY(Ti_ID) REFERENCES TIME (Ti_ID)
)

CREATE TABLE IF NOT EXISTS is_used_at2(
                pairText TEXT,
                Ti_ID INTEGER,
                PRIMARY KEY (pairText, Ti_ID),  
                FOREIGN KEY(pairText) REFERENCES HASHTAGPAIR (pairText),
                FOREIGN KEY(Ti_ID) REFERENCES TIME (Ti_ID)
)

CREATE TABLE IF NOT EXISTS is_part_of(
                text TEXT,
                pairText TEXT,
                PRIMARY KEY (text, pairText),  
                FOREIGN KEY(text) REFERENCES HASHTAG (text),
                FOREIGN KEY(pairText) REFERENCES HASHTAGPAIR (pairText)
)
