from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # 隐藏浏览器
driver = webdriver.Chrome(r'E:\04 爬虫\代码\myspider\chromedriver.exe',options=chrome_options)
driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').send_keys("张文广")
# driver.find_element_by_id('su').click() #鼠标点击
# res = driver.find_elements_by_xpath('//div')
data = driver.find_element_by_id('wrapper').text
#打印数据内容
print(data)
