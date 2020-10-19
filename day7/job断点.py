import requests
import MySQLdb
import re
import json
from lxml import etree
conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='spider',
    charset='utf8'
)
cursor = conn.cursor()
# 打断点
def duandians(list_url):
    sql = "update job_duandian set list_url=%s"
    cursor.execute(sql,[list_url])
    conn.commit()
# 取断点数据
def get_duandian():
    sql = "select * from job_duandian"
    cursor.execute(sql)
    return cursor.fetchone()[0] # 元祖
def get_list_url():
    global headers
    headers = {'user-agent': 'baiduspider'}
    duandian_url = get_duandian() #取断点数据
    if duandian_url == "1":  # 没有断点
        for i in range(1,100):
            url = "https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html".format(i)
            duandians(url)
            res = requests.get(url,headers=headers).content.decode('gbk')
            rule = "__SEARCH_RESULT__ = (.*?)</script>"
            job_dict = json.loads(re.findall(rule, res)[0])
            for job in job_dict['engine_search_result']:
                get_detail(job['job_href']) # 页码url和详情url
    else: #有断点
        rule = 'python,2,(.*).html'
        page = int(re.findall(rule,duandian_url)[0])#断点页面的页码
        for i in range(page,100):
            duandian = "https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,{}.html".format(i) #拼接url,从断点位置往下抓取
            res = requests.get(duandian, headers=headers).content.decode('gbk')
            duandians(duandian)
            rule = "__SEARCH_RESULT__ = (.*?)</script>"
            job_dict = json.loads(re.findall(rule, res)[0])
            for job in job_dict['engine_search_result']:
                get_detail(job['job_href']) # 页码url和详情url
def get_detail(detail_url):
    res = requests.get(detail_url,headers=headers).content.decode('gbk')
    ele = etree.HTML(res)
    com_name = ele.xpath('//p[@class="cname"]/a/@title')[0]
    print(com_name)

get_list_url()

