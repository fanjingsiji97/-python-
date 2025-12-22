#https://report.amap.com/index.do
# 1.	爬取高德地图实时全国拥堵城市榜单。
# 2.	高德地图实时拥挤前十名 拥堵延时指数，样例数据↓
# 3.	将采集下来的数据进行可视化处理，如生成柱状图。
import requests
from pyecharts import options as opts
from pyecharts.charts import *
headers = {
    # 如果不加这个 直接告诉网站 你是一个爬虫程序
    # 而加上这个  伪装成 浏览器 去访问
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
def get_data():
    url = "https://report.amap.com/ajax/getCityRank.do"
    res = requests.get(url,headers=headers)
    cities=res.json()
    x_data=[]
    y1_data=[]
    y2_data=[]
    y3_data=[]
    y4_data=[]
    y5_data=[]
    with open('rank.csv','w',encoding="utf8") as fp:

        for city in cities[:10]:
            name2=city['label']
            rank1=city['value']+1
            speed7=city['freeFlowSpeed']
            postpone3=city['rankState']
            oval5=city['idxRatioState']
            d4=city['idx1']
            f6=city['idxRatio']
            x_data.append(name2)
            y1_data.append(speed7)
            y2_data.append(postpone3)
            y3_data.append(d4)
            y4_data.append(oval5)
            y5_data.append(f6)
            if oval5=="flat":
                shit="←→"
            elif oval5=="up":
                shit="↑"
            elif oval5=="down":
                shit="↓"
            if postpone3 == "flat":
                k35 = "←→"
            elif postpone3 == "up":
                k35 = "↑"
            elif postpone3 == "down":
                k35 = "↓"
            citys=f"['城市排名':'{rank1}','城市名称':{name2},'拥堵延迟指数':{postpone3}{k35} {d4},'周环比数':{oval5}{shit} {f6},'畅通速度':{speed7}'km\h']\n"
            fp.write(citys)
    bar=Bar()
    bar1=Bar()
    bar2=Bar()
    bar1.add_xaxis(x_data)
    bar.add_xaxis(x_data)
    bar2.add_xaxis(x_data)
    bar.add_yaxis("畅通速度",y1_data)
    bar1.add_yaxis("拥堵延迟指数",y3_data)
    bar2.add_yaxis("周环比数",y5_data)
    bar.render("城市前十畅通速度数据.html")
    bar1.render("城市前十拥堵延迟指数.html")
    bar2.render("城市前十周环比数.html")
    # with open("城市数据.xlsx",'w',encoding="utf8")as fp1:
get_data()

