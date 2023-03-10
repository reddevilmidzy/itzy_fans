from selenium.webdriver.common.by import By
from uploading import update_tweet

midzy_only_url = "https://fans.jype.com/BoardList?BoardName=MIDZY_2ND_ONLY"
application_url = "https://fans.jype.com/BoardList?BoardName=itzy_Application"
before_midzy_only = []
before_application = []


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


def crawling_application(driver):
    global before_application
    now_application = []
    driver.implicitly_wait(2)
    driver.get(application_url)

    table = driver.find_element(By.XPATH, '/html/body/form/div[4]/div/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td/div[2]/table')
    tbody = table.find_element(By.TAG_NAME, "tbody")

    for tr in tbody.find_elements(By.TAG_NAME, "tr")[:5]:
        tds = tr.find_elements(By.TAG_NAME, "td")
        aTag = tds[1].find_element(By.TAG_NAME, 'a')
        url = aTag.get_attribute("href")
        title = tds[1].get_attribute("innerText")
        title = list(title.split())
        title = ' '.join(title)
        now_application.append((title, url))

    before_application = find_new(before_application, now_application, "APPLICATION")


def find_new(pre, now, community):
    if pre == []:
        return now
    elif get_url_list(pre) == get_url_list(now):
        return now

    for post in reversed(now):
        if post not in pre:
            update_tweet(post[0], post[1], community)
    return now

def get_url_list(lis):
    result = []
    for i in lis:
        result.append(i[0])
    return result