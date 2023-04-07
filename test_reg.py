import pytest
import csv
import time
from selenium.webdriver.common.by import By

Email=0
Password=1
Repeat_Password=2

def handle_data():
    with open('data.csv', 'r') as csv_file:
        csv_reader_file = csv.reader(csv_file)
        next(csv_reader_file)
        data = []
        for i in csv_reader_file:
            data.append(i)
        return data
@pytest.mark.parametrize('row', handle_data())
def test_registration(driver, i):
    driver.get("https://www.w3schools.com/howto/howto_css_register_form.asp")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys(i[Email])
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys(i[Password])
    driver.find_element(By.XPATH, "//input[@placeholder='Repeat Password']").send_keys(i[Repeat_Password])
    driver.find_element(By.XPATH, "//button[text()='Register']").click()
