"""
@author: Arpit Somani
"""
""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(executable_path=r'geckodriver.exe')

driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver, 600)

target='"friendname"' #enter your friend's name
string="Message sent using python!!"  #The message you need to send to your friend

x_arg='//span[contains(@title,'+target+')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box=driver.find_element_by_class_name('_3uMse')
for i in range(5):
    input_box.send_keys(string+Keys.ENTER)
    

