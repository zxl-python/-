from selenium import webdriver
import time
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://qzone.qq.com/')
time.sleep(1.5)
bro.switch_to.frame('login_frame')
bro.find_element_by_id('switcher_plogin').click()
time.sleep(2)
user = bro.find_element_by_id('u')
pws = bro.find_element_by_id('p')
user.send_keys('2119327621')
pws.send_keys('*******')
bro.find_element_by_id('login_button').click()
time.sleep(3)
bro.quit()

