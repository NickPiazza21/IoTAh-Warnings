import gspread
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Accessing firefox driver
driver = webdriver.Firefox(executable_path="C:/Users/npiaz/Downloads/geckodriver.exe")


def login():
    driver.get("https://www.iotah-view.com/#/admin-panel/warnings")  # Going to IoTAh website
    driver.find_element(By.NAME, "email").send_keys("npiazza@smartchargetech.com")  # Typing in email
    driver.find_element(By.NAME, "password").send_keys("silkycoconut392")  # Typing in password
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block rounded']").click()  # Click login button


# Issue: elements are blocking buttons
# Issue: button element is only clicking on first iteration
def getJson():
    url = "https://www.iotah-view.com/#/admin-panel/warnings"
    response = url.open(url)
    data = json.loads(response.read())
    print(data)


account = gspread.service_account(filename='warnings.json')  # Accessing google account connected to spreadsheet
sheet = account.open('IoTAhs with Warnings').sheet1  # Opening spreadsheet. Sheets are organized by order not name...
# ...(e.g. Total == sheet1, No Password == sheet3)

# sheet.update('A25', 'TEST')

login()
getJson()
