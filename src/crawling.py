from selenium.webdriver.common.by import By
from uploading import update_tweet

midzy_only_url = "https://fans.jype.com/BoardList?BoardName=MIDZY_2ND_ONLY"
application_url = "https://fans.jype.com/BoardList?BoardName=itzy_Application"
before_midzy_only = []
before_app = []


def find_new(pre, now, community):
    if pre == []:
        return now
    elif pre == now:
        return now

    for post in reversed(now):
        if post not in pre:
            update_tweet(post[0], post[1], community)
    return now