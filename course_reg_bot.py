import base64
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox()
# driver.get("http://somedomain/url_that_delays_loading")

def get_credentials():
    with open('secrets.json') as f:
        creds = json.loads(''.join(f.readlines()))
        return creds['username'], base64.b64decode(creds['password']).decode('ascii').strip()

class Vergil:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://vergil.registrar.columbia.edu/')

    # def get_search_box(self):
    #     return self.driver.find_element_by_xpath()

    def search(self, course_name):
        s_elem = self.driver.find_element_by_id("search")
        s_elem.send_keys(course_name)
        sleep(2)
        s_elem.send_keys(Keys.ENTER)

    def activate_omitted(self):
        elem = self.driver.find_element_by_id("toggle-relevant-sections")
        elem.click()

class SSOL:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get('https://ssol.columbia.edu/')

    def login(self,username,pwd):
        # Sleep just tells the system to pause execution for the number of seconds given as parameters
        # I have included sleep parameters in order to make it look more life like
        sleep(1.5)
        user_elem = self.driver.find_element_by_name("u_id")
        user_elem.send_keys(username)

        sleep(1)
        pwd_elem = self.driver.find_element_by_name("u_pw")
        pwd_elem.send_keys(pwd)

        sleep(1.5)
        submit_elem = self.driver.find_element_by_name("submit")
        submit_elem.send_keys(Keys.ENTER)



    def registration(self):
        sleep(1)
        self.scroll_window_long()
        sleep(0.75)
        reg_elem = self.driver.find_element_by_link_text("Registration")
        reg_elem.click()


        sleep(1.5)
        self.scroll_window_long()
        sleep(0.75)
        fall_20_elem = self.driver.find_element_by_xpath("/html/body/div[3]/main/form[3]/fieldset/input[2]")
        fall_20_elem.click()


    def scroll_window_long(self):
        sleep(1.25)
        self.driver.execute_script("window.scrollTo(0, 100)")
        sleep(0.4)
        self.driver.execute_script("window.scrollTo(0, 200)")
        sleep(0.4)
        self.driver.execute_script("window.scrollTo(0, 300)")
        sleep(0.4)
        self.driver.execute_script("window.scrollTo(0, 350)")

    def scroll_window_short(self):
        sleep(1.25)
        self.driver.execute_script("window.scrollTo(0, 50)")
        sleep(0.4)
        self.driver.execute_script("window.scrollTo(0, 125)")
        sleep(0.4)
        self.driver.execute_script("window.scrollTo(0, 200)")

    def scroll_window_final(self):
        sleep(1.25)
        self.driver.execute_script("window.scrollTo(0, 200)")
        sleep(0.4)
        self.driver.execute_script("window.scrollTo(0, 300)")
        sleep(0.4)
        self.driver.execute_script("window.scrollTo(0, 400)")
        sleep(0.4)
        self.driver.execute_script("window.scrollTo(0, 500)")




    def course_reg(self,call_num):

        for course in call_num:
            call_num_elem = self.driver.find_element_by_name("tran[1]_CALLNUM")
            call_num_elem.send_keys(course)
            sleep(1)
            query_elem = self.driver.find_element_by_xpath("/html/body/div[3]/main/form[2]/table/tbody/tr[2]/td[2]/input")
            query_elem.click()
            sleep(0.75)
            self.scroll_window_long()
            sleep(0.75)
            wish_elem = self.driver.find_element_by_xpath("/html/body/div[3]/main/form[3]/table/tbody/tr[6]/td/input")
            wish_elem.click()
            self.scroll_window_short()
            sleep(0.5)
        self.scroll_window_final()

    def prev_page(self):
        self.driver.back()


if __name__ == '__main__':
    d = webdriver.Chrome()
    # vergil = Vergil(d)
    # sleep(1)
    # vergil.search('deep learning')
    # sleep(2)
    # vergil.activate_omitted()

    # SSOL Stuff
    user, pwd = get_credentials()
    ssol = SSOL(d)
    ssol.login(user, pwd)
    ssol.registration()
    sleep(1)

    courses = [10078,10808,10850,11671,10083,10080]
    ssol.course_reg(courses)


    """"10080 (Advanced ML), 10078 (ML NkVe), 11668 (Algos), 10808 (Algos DS)
    10850 (DL for Vision), 10083 (Foundations of Blockchains), 11671 (Foundations of Large Scale and Dist Systems)"""


