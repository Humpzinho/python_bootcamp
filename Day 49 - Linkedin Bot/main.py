from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

with open("Day 49 - Linkedin Bot\\private_data.json") as file:
    private_data = json.load(file)

chrome_driver_path = "Day 48 - Cookie Clicker Bot with Selenium\\chromedriver.exe"
# op = webdriver.ChromeOptions()
# op.add_argument('headless')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?distance=25&f_AL=true&geoId=107621648&keywords=python%20developer&location=S%C3%A3o%20Gon%C3%A7alo%2C%20RJ"
)

driver.fullscreen_window()

time.sleep(2)

login_button = driver.find_element_by_class_name("cta-modal__primary-btn")
login_button.click()

time.sleep(1)

email_input = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

email_input.send_keys(private_data["email"])
password.send_keys(private_data["password"])
password.send_keys(Keys.ENTER)

time.sleep(1)

list_of_jobs = driver.find_elements_by_css_selector(
    ".jobs-search-results__list.list-style-none li[data-occludable-entity-urn]")

button = driver.find_element_by_css_selector(
        ".jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary"
)

button.click()
for job in list_of_jobs:
    button = driver.find_element_by_css_selector(
        ".jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary"
    )
    if list_of_jobs.index(job) > 1:
        job.click()
        time.sleep(2)
        button.click()