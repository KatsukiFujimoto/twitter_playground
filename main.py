import tweepy
import pandas
from pprint import pprint
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import pdb
# pdb.set_trace()

load_dotenv()
expansions = [
    "attachments.poll_ids",
    "attachments.media_keys",
    "author_id",
    "entities.mentions.username",
    "geo.place_id",
    "in_reply_to_user_id",
    "referenced_tweets.id",
    "referenced_tweets.id.author_id",
]
tweet_fields = [
    "attachments",
    "author_id",
    "context_annotations",
    "conversation_id",
    "created_at",
    "entities",
    "geo",
    "id",
    "in_reply_to_user_id",
    "lang",
    # "non_public_metrics",
    "public_metrics",
    # "organic_metrics",
    # "promoted_metrics",
    "possibly_sensitive",
    "referenced_tweets",
    "reply_settings",
    "source",
    "text",
    "withheld",
]
user_fields = [
    "created_at",
    "description",
    "entities",
    "id",
    "location",
    "name",
    "pinned_tweet_id",
    "profile_image_url",
    "protected",
    "public_metrics",
    "url",
    "username",
    "verified",
    "withheld",
]
client = tweepy.Client(os.environ["BEARER_TOKEN"])
res = client.search_recent_tweets(
        "cryptocurrency",
        max_results = 10,
        expansions = expansions,
        tweet_fields = tweet_fields,
        user_fields = user_fields,
      )
JST = timezone(timedelta(hours=+9), "JST")
formatted_time = datetime.now(JST).strftime("%Y-%m-%d-%H-%M-%S")
if res.errors:
    os.makedirs("errors", exist_ok=True)
    with open(f"errors/{formatted_time}.txt", mode="w") as f:
        pprint(res.errors, depth=2, stream=f)
else:
    os.makedirs("results", exist_ok=True)
    rows = []
    for x in res.data:
        rows.append([
            x.id,
            x.text,
            x.created_at.astimezone(JST).isoformat(),
        ])
    data_frame = pandas.DataFrame(rows, columns = [
        "tweet_id",
        "content",
        "tweeted_at",
    ]).to_csv(f"results/{formatted_time}.csv", encoding="utf-8")
