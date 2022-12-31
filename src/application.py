from apscheduler.schedulers.blocking import BlockingScheduler
from crawling import crawling_application, crawling_midzy
from login import login

def start():
    driver = login()
    crawling_midzy(driver)
    crawling_application(driver)

