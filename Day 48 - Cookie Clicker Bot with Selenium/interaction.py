from selenium import webdriver
import time
import threading as th

chrome_driver_path = "Day 48 - Cookie Clicker Bot with Selenium\\chromedriver.exe"
# op = webdriver.ChromeOptions()
# op.add_argument('headless')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")
# driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = 15 #Minutes
check_timeout = 2
current_time_loop = time.time()


def check_store():
    
    global check_timeout
    global T
    # list_of_items_obj = driver.find_elements_by_css_selector(
    #         "#store div:not(.grayed, .amount)")
    list_of_upgrades_obj = driver.find_elements_by_css_selector(
        ".upgrade.enabled")
    for n in range(len(list_of_upgrades_obj) - 1, -1, -1):
        try:
            list_of_upgrades_obj[n].click()
        except:
            pass
        else:
            break
    list_of_products_obj = driver.find_elements_by_css_selector(".enabled")
    for n in range(len(list_of_products_obj) - 1, -1, -1):
        try:
            list_of_products_obj[n].click()
        except:
            pass
        else:
            break
    T = th.Timer(check_timeout, check_store)
    T.start()
    check_timeout = 10


# cookie_buttom = driver.find_element_by_id("cookie")
time.sleep(2)
cookie_buttom = driver.find_element_by_id("bigCookie")

check_store()

while time.time() < current_time_loop + timeout*60:
    cookie_buttom.click()

cps = driver.find_element_by_css_selector("#cookies div")
print(cps.text)

driver.quit()
quit()
