import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

all_data_list = []
def tcb_spider(lp, spider_sleep):
    url = "https://kaijiang.500.com/shtml/ssq/" + lp + ".shtml"
    print("url: ", url)
    ball_list = []
    time.sleep(spider_sleep)
    resp = requests.get(url=url)
    if resp.status_code == 200:
        resp.encoding = "gb2312"
        html = resp.text
        bs = BeautifulSoup(html, "lxml")
        balls = bs.find("div", {"class": "ball_box01"}).find_all("li")
        for ball in range(len(balls)):
            temp = str(balls[ball]).replace("<li class=\"ball_red\">", "").replace("</li>", "").replace(
                "<li class=\"ball_blue\">", "")
            ball_list.append(temp)
    print(ball_list)
    if ball_list != []:
        all_data_list.append(ball_list)

for year in range(3, 23):
    if year < 10:
        new_year = "0" + str(year)
    else:
        new_year = str(year)
    for nper in range(1, 201):
        if nper < 10:
            new_nper = "00" + str(nper)
        elif nper < 100:
            new_nper = "0" + str(nper)
        else:
            new_nper = str(nper)
        # The lottery periods
        lp = new_year + new_nper
        # print("lp: ", lp)
        tcb_spider(lp, 1)
print("all_data_list: ", all_data_list)

data = pd.DataFrame(all_data_list, columns=['RED01', 'RED02', 'RED03', 'RED04', 'RED05', 'RED06', 'BLUE'])
data.to_excel('TCB.xlsx')
