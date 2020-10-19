import requests
from multiprocessing import Pool  #进程池
import threading
import os
#1 - 625
def run(i):
    url = "https://douban.donghongzuida.com/20201009/10722_a9c63d95/1000k/hls/a02ef2edf7d000%03d.ts"%i
    r = requests.get(url).content
    name = url[-7:]
    print("开始下载:%s"%name)
    with open("movie/{}".format(name),'wb') as w:
        w.write(r)
if __name__ == '__main__':
    # pool = Pool(10)
    # pool.apply_async(run,(i,))
    # pool.close()
    # pool.join()
    # print("爬虫结束")
    a = os.popen('copy /b .\movie\*.ts hehe.mp4')
    print(a.read())