#importing all the necessary libaries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input('enter the name of user')
msg = input('enter your message')
count = int(input("enter the count"))
input('enter after scanning QR code')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()