from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

fans_main_url = "https://fans.jype.com/"
user_id = ""
user_pw = ""

def option():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    return chrome_options

def driver_load():
    return webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option())

def login():
    driver = driver_load()
    driver.get(fans_main_url)
    driver.implicitly_wait(4)
    driver.find_element(By.ID, 'txtUserID').send_keys(user_id)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'txtPassword').send_keys(user_pw)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/div/div[2]/input').click()
    driver.implicitly_wait(4)
