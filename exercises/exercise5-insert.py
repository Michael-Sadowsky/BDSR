import sqlite3
import pandas as pd
import pandasql as sql
pysqldf = lambda q: sql.sqldf(q, globals()) #use sqldf without having to use the globals argument
conn = sqlite3.connect('twitter.sqlite') #connecting to sqlite3

twitter=pd.read_csv('tweet_sample.txt',sep='\t',encoding='utf_8') #read the csv



#Get individual tweets
tweets=twitter.loc[:,['twitter_tweet_id',"twitter_user_twitter_id",'user_followers_count',"tweet_timestamp","tweet_text","tweet_language","tweet_retweet_count","tweet_place","tweet_user_mention_count","tweet_users_mentioned_screennames","tweet_users_mentioned_ids","tweet_hashtag_mention_count","tweet_hashtags_mentioned","tweet_url_count", "tweet_shortened_urls_mentioned","tweet_full_urls_mentioned","tweet_display_urls_mentioned"]]
tweets=tweets.drop_duplicates(cols='twitter_tweet_id') #take only unique tweets
#Get individual users
users=twitter.loc[:,['twitter_user_twitter_id',"twitter_user_screenname","user_followers_count","user_favorites_count","user_created","user_location","user_description","user_friends_count","user_statuses_count"]]
#only taking users with the max user_statuses_count
users=pysqldf('select * from users where user_statuses_count in (select max(user_statuses_count) from users group by twitter_user_twitter_id)')
#dropping duplicate users
users=users.drop_duplicates(cols='twitter_user_twitter_id')
pd.io.sql.write_frame(tweets, "tweets", conn) #write files to the database
pd.io.sql.write_frame(users, "users", conn)
conn.commit() #commit the changes made to the database