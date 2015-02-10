CREATE  TABLE "main"."tweets" ("twitter_tweet_id" INTEGER , 
	"tweet_timestamp" VARCHAR, 
	"tweet_text" VARCHAR,
	"tweet_language" VARCHAR,
	"twitter_user_twitter_id" INT
	"tweet_retweet_count" INTEGER
	"tweet_place" VARCHAR,
	"tweet_user_mention_count" VARCHAR,
	"tweet_users_mentioned_screennames" VARCHAR,
	"tweet_users_mentioned_ids" INTEGER
	"tweet_hashtag_mention_count" INTEGER
	"tweet_hashtags_mentioned" VARCHAR,
	"tweet_url_count" INTEGER
	"tweet_shortened_urls_mentioned" VARCHAR,
	"tweet_full_urls_mentioned" VARCHAR,
	"tweet_display_urls_mentioned" VARCHAR
	);

CREATE  TABLE "main"."users" ("twitter_user_twitter_id" INTEGER, 
	"twitter_user_screenname" VARCHAR, 
	"user_followers_count" INTEGER
	"user_favorites_count" INTEGER
	"user_created" VARCHAR
	"user_location" VARCHAR,
	"user_description" VARCHAR,
	"user_friends_count" INTEGER
	"user_statuses_count" INT
	);



update tweets
set tweet_user_mention_count=coalesce(tweet_user_mention_count,0)
,tweet_hashtag_mention_count=coalesce(tweet_hashtag_mention_count,0)
,tweet_url_count=coalesce(tweet_url_count,0)

