import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_count.click()

# random_article = driver.find_element(By.LINK_TEXT, "Random article")
# random_article.click()

# search = driver.find_element(By.NAME,"search")
# search.send_keys("Python")
# search.send_keys(Keys.RETURN)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Shaun")
second_name = driver.find_element(By.NAME, "lName")
second_name.send_keys("Brown")
email = driver.find_element(By.NAME, "email")
email.send_keys("srbrown1989@gmail.com")

sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()

time.sleep(10)

driver.close()
