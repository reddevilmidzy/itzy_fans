from selenium.webdriver.common.by import By
from uploading import update_tweet

midzy_only_url = "https://fans.jype.com/BoardList?BoardName=MIDZY_2ND_ONLY"
application_url = "https://fans.jype.com/BoardList?BoardName=itzy_Application"
before_midzy_only = []
before_app = []


def crawling_midzy(driver):
    global before_midzy_only
    now_midzy_only = []

    driver.implicitly_wait(3)
    driver.get(midzy_only_url)
    driver.implicitly_wait(1)

    table = driver.find_element(By.XPATH, '/html/body/form/div[4]/div/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td/div[2]/table')
    tbody = table.find_element(By.TAG_NAME, "tbody")

    for tr in tbody.find_elements(By.TAG_NAME, "tr")[1:6]:
        tds = tr.find_elements(By.TAG_NAME, "td")
        aTag = tds[1].find_element(By.TAG_NAME, 'a')
        url = aTag.get_attribute("href")
        title = aTag.get_attribute("innerText")
        now_midzy_only.append((title, url))

    before_midzy_only = find_new(before_midzy_only, now_midzy_only, "MIDZY 2ND ONLY")


def find_new(pre, now, community):
    if pre == []:
        return now
    elif pre == now:
        return now

    for post in reversed(now):
        if post not in pre:
            update_tweet(post[0], post[1], community)
    return now