from pyecharts import options as opts
from pyecharts.charts import Map,Bar
from pyecharts.charts import Page
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
sql = "select * from province"
cursor.execute(sql)
datas = cursor.fetchall()
china_sql = 'select * from china_count'
cursor.execute(china_sql)
china_data = cursor.fetchone()
#地图
map_obj = (
    Map()
    .add("", datas, "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="疫情情况",subtitle="截止目前为止,全国共有累计确诊{}例,累计治愈{}例,累计死亡{}例,疑似{}例"
                                  .format(china_data[0],china_data[1],china_data[2],china_data[3])
                                  ),
        visualmap_opts=opts.VisualMapOpts(max_=3),
    )
)
name_list = [name[0] for name in datas]
data_list = [name[1] for name in datas]
#柱状图
bar_obj = (
    Bar()
    .add_xaxis(name_list)
    .add_yaxis("各省份数据对比",data_list )
    .set_global_opts(title_opts=opts.TitleOpts(title="各省份目前情况"),
                     datazoom_opts=[opts.DataZoomOpts()]
                     )
)
# page对象用于整合地图
p = Page(layout=Page.SimplePageLayout)
p.add(map_obj,bar_obj)
p.render("疫情实时监控.html")

