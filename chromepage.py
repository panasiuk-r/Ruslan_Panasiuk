from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Intro:
    browser = webdriver.Chrome()
    def login(self):
        self.browser.maximize_window()
        self.browser.implicitly_wait(20)
        self.browser.get('https://opensource-demo.orangehrmlive.com/')
        username = self.browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[1]').text.replace('Username : ', '')
        password = self.browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[2]').text.replace('Password : ', '')
        select_box = self.browser.find_element(By.NAME, 'username')
        select_box.click()
        select_box.send_keys(username)
        select_box = self.browser.find_element(By.NAME, 'password')
        select_box.click()
        select_box.send_keys(password)
        click_send = self.browser.find_element(By.CLASS_NAME, 'orangehrm-login-button')
        click_send.click()

class Main_test(Intro):
    def task(self):
        select_box = self.browser.find_element(By.CLASS_NAME, 'oxd-main-menu-item--name')
        select_box.click()
        select_box = self.browser.find_element(By.CLASS_NAME, 'oxd-topbar-body-nav-tab-item')
        select_box.click()
        select_box = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
        select_box.click()
        select_box = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]/a')
        select_box.click()
        select_box = self.browser.find_element(By.CLASS_NAME, 'oxd-button--secondary')
        select_box.click()
        select_box = self.browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input')
        select_box.click()
        select_box.send_keys('Sun')
        select_box = self.browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input')  #clock
        select_box.click()
        select_box = self.browser.find_element(By.CLASS_NAME, 'oxd-time-hour-input-down')
        for i in range(3):
            select_box.click()
        select_box = self.browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[1]/input')
        select_box.click()
        select_box = self.browser.find_element(By.CLASS_NAME, 'oxd-time-hour-input-up')
        select_box.click()
        select_box = self.browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[1]/input')
        select_box.click()
        select_box.send_keys('Odis Adalwin')
        sleep(2)
        select_box = self.browser.find_element(By.CLASS_NAME, '--positon-bottom')
        select_box.click()
        select_box = self.browser.find_element(By.CLASS_NAME, 'orangehrm-left-space')
        select_box.click()
        box_list = self.browser.find_elements(By.CLASS_NAME, "oxd-table-card")
        for card in box_list:
            element = card.find_elements(By.CLASS_NAME, 'oxd-padding-cell')
            if element[1].text == 'Sun' and element[2].text == '06:00' and element[3].text == '18:00' and element[4].text == '12.00':
                sleep(2)
                select_box = element[5].find_element(By.CLASS_NAME, 'oxd-table-cell-action-space')
                select_box.click()
                select_box = self.browser.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/div[3]/button[2]')
                select_box.click()
                break
        sleep(4)
        self.browser.quit()

if __name__ == '__main__':
    browser = webdriver.Chrome()
    test = Main_test()
    test.login()
    test.task()
