from mail import mailSender
import datetime as dt
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()
USERNAME = os.getenv("ID")
PASSWORD = os.getenv("CODE")
sender = os.getenv("SENDER")
password = os.getenv("ID_Pass")
receiver = os.getenv("RECEIVER")


def libraryBot(user, code):
    driver_path = "C:\Python310\geckodriver.exe"

    driver = webdriver.Firefox(executable_path=driver_path)
    driver.get("http://117.239.204.229:8380/opac/myaccount/myAccount.html")

    time.sleep(5)
    username = driver.find_element("id", "usernameId")

    username.send_keys(user)
    password = driver.find_element("id", "passwordId")
    password.send_keys(code)

    submit = driver.find_element("id", "submitButton")
    submit.click()

    # searching books

    my_account = driver.find_element("id", "myaccount")
    time.sleep(1)
    my_account.click()

    checkout = driver.find_element("id", "checkOut")
    checkout.click()

    books = driver.find_elements(By.CLASS_NAME, "recordObjectDiv")
    for i in books:
        due_date = driver.find_element(By.ID, "Span9")

        date = dt.datetime.strptime(due_date.text, '%d/%m/%Y').date()

        if(dt.date.today() + dt.timedelta(days=1) > date):
            renewAll = driver.find_element("id", "renewLabel")
            renewAll.click()
            error = driver.find_element(By.CLASS_NAME, "errorLbl")
            if(error.text == "MAXIMUM NO. OF RENEWALS REACHED"):
                mailSender(sender, password, receiver)
            print(f"Renewal done!!!{USERNAME} ")
        else:
            print("No renewal Required")


libraryBot(USERNAME, PASSWORD)
