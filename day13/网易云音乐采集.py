from selenium import webdriver
import time
import MySQLdb
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='spider',
    charset='utf8'
)
cursor = conn.cursor()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') # 隐藏浏览器
url = "https://music.163.com/#/song?id=1487009176"
driver = webdriver.Chrome(r'E:\04 爬虫\代码\myspider\chromedriver.exe',options=chrome_options)
driver.get(url)
driver.switch_to_frame('g_iframe') # 切换到对应的frame界面
for i in range(10): # 爬十页
    js = "var q=document.documentElement.scrollTop=7000"
    driver.execute_script(js)
    nodes = driver.find_elements_by_xpath('//div[@class="cnt f-brk"]')
    for i in nodes:
        try:
            sql = 'insert into wyyyy values(%s)'
            cursor.execute(sql,[i.text])
            conn.commit()
        except:
            pass
        print(i.text)
    a = driver.find_element_by_xpath('//a[text()="下一页"]')
    a.click()
    time.sleep(2)