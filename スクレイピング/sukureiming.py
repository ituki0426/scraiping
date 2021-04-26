from selenium import webdriver
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

url='https://scraping-for-beginner.herokuapp.com/login_page'

browser.get(url)

elem_username = browser.find_element_by_id('username')

elem_username.send_keys('imanishi')

elem_pasword = browser.find_element_by_id('password')

elem_pasword.send_keys('kohei')

elem_login_btn = browser.find_element_by_id('login-btn')

elem_login_btn.click()
elem_th=browser.find_elements_by_tag_name('th')
elem_th[0].text

