import requests
url = "http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearchDG.html"
data = {
'page':'1',
'rows':'400000',
'annNum':'1020',
'annType':'',
'tmType':'',
'coowner':'',
'recUserName':'',
'allowUserName':'',
'byAllowUserName':'',
'appId':'',
'appIdZhiquan':'',
'bfchangedAgengedName':'',
'changeLastName':'',
'transferUserName':'',
'acceptUserName':'',
'regName':'',
'tmName':'',
'intCls':'',
'fileType':'',
'totalYOrN':'true',
'appDateBegin':'',
'appDateEnd':'',
'agentName':'',
}
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
res = requests.post(url,data=data,headers=headers).json()
print(res['rows'])
print(len(res['rows']))
