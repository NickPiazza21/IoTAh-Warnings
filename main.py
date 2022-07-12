import gspread
import requests
import json
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Accessing firefox driver
driver = webdriver.Firefox(executable_path="C:/Users/npiaz/Downloads/geckodriver.exe")


def login():
    driver.get("https://www.iotah-view.com/#/admin-panel/api-page")  # Going to IoTAh website
    driver.find_element(By.NAME, "email").send_keys("npiazza@smartchargetech.com")  # Typing in email
    driver.find_element(By.NAME, "password").send_keys("silkycoconut392")  # Typing in password
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block rounded']").click()  # Click login button


def getAPI():
    search = driver.find_element(By.NAME, "url")
    search.click()
    search.send_keys("device/getAllSitesDevicesListing")
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

    content = driver.find_element(By.XPATH, "//div[@class='mt-4 col-10 result']").text

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get("https://jsonformatter.org/json-parser")

    paste = driver.find_element(By.XPATH, "//textarea[@class='ace_text-input']")
    paste.print(content)


def test():
    payload = {'email': 'npiazza@smartchargetech.com', 'password': 'silkycoconut392'}
    url = 'https://www.iotah-view.com/user/login'
    response = requests.post(url, data=payload)
    print(response.content)


account = gspread.service_account(filename='warnings.json')  # Accessing google account connected to spreadsheet
sheet = account.open('IoTAhs with Warnings').sheet1  # Opening spreadsheet. Sheets are organized by order not name...
# ...(e.g. Total == sheet1, No Password == sheet3)

# sheet.update('A25', 'TEST')

test()
