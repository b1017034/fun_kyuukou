from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from os.path import join, dirname
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

import os
from selenium.webdriver.common.keys import Keys

import re


class scraping:

    def __init__(self, password, username):
        options = ChromeOptions()
        # set headless mode
        options.add_argument('--headless')

        self.selector = {
            'phantom': webdriver.PhantomJS(),
            'chrome-headless': webdriver.Chrome(chrome_options=options)
        }

        self.browser = self.selector['chrome-headless']
        self.browser.implicitly_wait(10)
        url = 'https://student.fun.ac.jp'
        self.browser.get(url)

        self.password = password
        self.username = username

    def login(self):
        self.usernameField = self.browser.find_element_by_id('form1:htmlUserId')
        self.usernameField.send_keys(self.username)
        self.passwordField = self.browser.find_element_by_id("form1:htmlPassword")
        self.passwordField.send_keys(self.password)
        self.button = self.browser.find_element_by_id("form1:login")
        self.button.click()

    def check(self):
        profile = "https://student.fun.ac.jp"
        self.browser.get(profile)
        print(self.browser)
        self.browser.close()

    def kyuukou(self):
        self.kyu = self.browser.find_element_by_id("form1:Poa00201A:htmlParentTable:1:htmlDetailTbl:0:htmlTitleCol1")
        self.kyu.click()

        WebDriverWait(self.browser, 3).until((lambda d: len(d.window_handles) > 1))
        handles = self.browser.window_handles
        self.browser.switch_to_window(handles[1])

        self.text = self.browser.find_element_by_id("form1:htmlMain").text
        self.text_array = self.text.splitlines()

    def quit_Browser(self):
        self.browser.quit()


if __name__ == "__main__":

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    a = scraping("%s" % os.environ["FUN_PASSWORD"], "%s" % os.environ["FUN_MAIL"])
    a.login()
    a.kyuukou()
    a.quit_Browser()
