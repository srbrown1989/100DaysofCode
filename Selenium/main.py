import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

PRICE_XPATH = '//*[@id="corePrice_feature_div"]/div/span/span[1]'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.amazon.com/Pacrate-Stereo-Gaming-Headset-Cancelling/dp/B07Y1WRD1H/ref=sr_1_1_sspa?keywords"
#            "=gaming+headsets&pd_rd_r=a8d2edc1-9cc2-49ce-b0e0-91cf660a667f&pd_rd_w=IR4IU&pd_rd_wg=152PG&pf_rd_p"
#            "=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=QMXKVMGQRTJBQJ1PBG7V&qid=1672923784&sr=8-1-spons&psc=1&smid"
#            "=ATS1RBXW02LHW&spLa"
#            "=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVU5ZT1RGWjdCWEY1JmVuY3J5cHRlZElkPUEwMzQ0NDcwMllFOExUV1lYUEZTSiZlbmNyeXB0ZWRBZElkPUEwODAyODk0MlJYT1RaTTJXTlRKMCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
# price = driver.find_element(By.XPATH, PRICE_XPATH)
# print(price.get_attribute("innerHTML"))

driver.get("https://www.python.org/")

times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
times = [time.get_attribute("datetime")[:10] for time in times]

names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
names = [name.text for name in names]

events = {i: {"time": times[i], "name": names[i]} for i in range(0, len(times))}
print(events)
driver.close()
