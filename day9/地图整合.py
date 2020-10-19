from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Map
from pyecharts.charts import Page
pie_obj = (
    Pie()
    .add("数据", [["北京",200],["吉林",300],["山西",800],["广东",500]])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)
map_obj = (
    Map()
    .add("商家A", [["北京",200],["吉林",300],["山西",800],["广东",500]], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
        visualmap_opts=opts.VisualMapOpts(max_=600),
    )
)
# page对象用于整合地图
p = Page(layout=Page.SimplePageLayout)
p.add(pie_obj,map_obj)
p.render("地图整合.html")

