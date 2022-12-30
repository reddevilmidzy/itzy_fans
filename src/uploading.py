import tweepy

api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""

def update_tweet(title, link, community):
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(formatted_string(title, link, community))

def formatted_string(title, link, community):
    return f"ITZY Fan's\n[{community}] 새 글 알림\n\n{title}\n\n{link}\n\n#ITZY #있지"