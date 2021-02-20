from transformers import BertTokenizer, TFBertForSequenceClassification
from transformers import 
import tensorflow
import praw
from praw.models import MoreComments

reddit = praw.Reddit (
    client_id = "ID HERE",
    client_secret = "SECRET API KEY HERE",
    user_agent = "SentiScraper/version 0.0.1",
    username = "USERNAME HERE",
    password = "PASSWORD HERE",
    check_for_async=False
)

comment_list = []
ticker_strang = input("Enter tickers, separated by spaces: ")
ticker_list = ticker_strang.split()

for post in reddit.subreddit("wallstreetbets").hot(limit=1):
  post.comments.replace_more(limit=15)
  for comment in post.comments.list():
    for ticker in ticker_list:
      if comment.body.find(ticker) != -1:
        comment_list.append(comment.body)

sentiment_list = []
pos = 0
neg = 0
nlp = pipeline('sentiment-analysis')
for i in range(0, len(comment_list) - 1):
  result = nlp(comment_list[i])
  if result['label'] = "POSITIVE":
    pos += 1
  else:
    neg += 1
print("{}% positive".format((pos/(neg + pos)))
