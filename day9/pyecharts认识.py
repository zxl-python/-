from pyecharts.charts import Bar
# bar = Bar()  #实例柱状图对象
# #添加x轴选项名称
# bar.add_xaxis(("衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"))
# #添加y轴对应的数据量
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.add_yaxis("商家B", [10, 10, 56, 20, 75, 80])
# bar.render()

# 链式调用
# Bar().add_xaxis(("衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子")).add_yaxis("商家A", [5, 20, 36, 10, 75, 90]).add_yaxis("商家B", [10, 10, 56, 20, 75, 80]).render("1.html")

#配置选项
#配置图表风格样式
from pyecharts.globals import ThemeType
from pyecharts import options
Bar(init_opts=options.InitOpts(theme=ThemeType.MACARONS)).add_xaxis(("衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"))\
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])\
    .add_yaxis("商家B", [10, 10, 56, 20, 75, 80])\
    .set_global_opts(title_opts=options.TitleOpts("衣服销量",subtitle='仅供参考'),
                     toolbox_opts=options.ToolboxOpts(), #工具栏选项
                     brush_opts=options.BrushOpts() #工具刷对象
                     )\
    .render("1.html")
