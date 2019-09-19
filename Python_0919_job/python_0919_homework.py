# @Time :2019/9/19 21:06
# @Author :jinbiao

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Py0919:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ketangpai.com/")

    def elements(self, element):
        self.a = (By.XPATH, element)
        return self.a

    def wait(self, element):
        b = self.elements(element)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(b))

if __name__ == '__main__':
    py = Py0919()
    py.wait('//a[@class="login"]')
    py.driver.find_element(*py.a).click()
    py.wait('//input[@name="account"]')
    py.driver.find_element(*py.a).send_keys("13611767797")
    py.wait('//input[@name="pass"]')
    py.driver.find_element(*py.a).send_keys("Ktp123")
    py.wait('//div[@class="padding-cont pt-login"]/a[@class="btn-btn"]')
    py.driver.find_element(*py.a).click()
    py.wait('//a[text()="Python全栈第20期"]')
    py.driver.find_element(*py.a).click()
    py.wait('//a[text()="作业"]')
    py.driver.find_element(*py.a).click()
    py.wait('//a[text()="查看成绩"]')
    py.driver.find_element(*py.a).click()
    py.wait('//p[text()="成绩"]/span')
    print(py.driver.find_element(*py.a).text)
    py.wait('//a[text()="作业讨论"]')
    py.driver.find_element(*py.a).click()
    py.wait('//p[text()="添加评论"]')
    py.driver.find_element(*py.a).click()
    py.wait('//textarea[@class="comment-txt"]')
    py.driver.find_element(*py.a).send_keys("test")
    py.wait('//a[@class="sure active"]')
    py.driver.find_element(*py.a).click()
    py.wait('//span[text()="Python全栈第20期"]')
    py.driver.find_element(*py.a).click()
    py.wait('//i[@class="iconfont iconchengyuan"]')
    py.driver.find_element(*py.a).click()
    py.wait('//li[@class="all"]')
    py.driver.find_element(*py.a).click()
    py.wait('//div[@class="fr input-box"]/input')
    py.driver.find_element(*py.a).send_keys("2002", Keys.ENTER)



    # //a[text()="查看成绩"]
    #//div[@class="padding-cont pt-login"]/a[@class="btn-btn"]
    # //p[text()="成绩"]/span
    # //a[text()="作业讨论"]
    # //p[text()="添加评论"]
    # //a[@class="sure active"]
    # //span[text()="Python全栈第20期"]
    # //i[@class="iconfont iconchengyuan"]
    # //li[@class="all"]
    # //div[@class="fr input-box"]/input