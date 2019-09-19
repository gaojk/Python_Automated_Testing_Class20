# @Time :2019/9/17 21:29
# @Author :jinbiao

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(url="https://www.12306.cn/index/")


def wait(element):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(element))


serch_element = (By.XPATH, '//a[@id="search_one"]')
fromStationText_element = (By.XPATH, '//input[@id="fromStationText"]')
toStationText_element = (By.XPATH, '//input[@id="toStationText"]')

# WebDriverWait(driver, 20).until(EC.visibility_of_element_located(fromStationText_element))
elements = [serch_element, fromStationText_element, toStationText_element]
for i in elements:
    wait(i)

start_off_js = """fromStationText = document.getElementById("fromStationText");
fromStationText.value = "上海";
fromStation = document.getElementById("fromStation");
fromStation.value = "SHH";
toStationText = document.getElementById("toStationText");
toStationText.value = "北京";
toStation = document.getElementById("toStation");
toStation.value = "BJP";
train_date = document.getElementById("train_date");
train_date.readOnly = false;
train_date.value = "2019-10-10";"""

driver.execute_script(script=start_off_js)
serch = driver.find_element(*serch_element)
serch.click()
