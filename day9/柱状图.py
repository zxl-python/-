from pyecharts import options as opts
from pyecharts.charts import Bar
c = (
    Bar()
    .add_xaxis(("衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子","T恤衫","秋裤","蕾丝","短袖","毛裤","军大衣"))
    .add_yaxis("商家B", ['10', '10', '56', '20', '75', '80'])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家C", [20, 20, 36, 10, 75, 90])
    .add_yaxis("商家D", [30, 20, 36, 10, 75, 90])
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),
                     datazoom_opts=[opts.DataZoomOpts()]
                     )
    .render("bar_base.html")
)