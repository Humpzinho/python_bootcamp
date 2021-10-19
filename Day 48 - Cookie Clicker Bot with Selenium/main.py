from selenium import webdriver

#Version 93.0.4577.63
chrome_driver_path = "Day 48 - Cookie Clicker Bot with Selenium\\chromedriver.exe"
op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=op)

driver.get("https://www.python.org/")

li_names = driver.find_elements_by_css_selector(".event-widget li a")
li_dates = driver.find_elements_by_css_selector(".event-widget time")

conferences = {
    li_names.index(name): {
        "name": name.text,
        "time": date.get_attribute("datetime").split("T")[0]
    } for name, date in zip(li_names, li_dates)
}

print(conferences) 
driver.quit()
