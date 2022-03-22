# https://kaijiang.500.com/shtml/ssq/22030.shtml
import requests
import time
from bs4 import BeautifulSoup
from excel_tools import ExcelTools

excel_tool = ExcelTools()

excel_tool.create_workbook()

year = ""
per = ""
for i in range(3, 23):
    if i < 10:
        year = "0" + str(i)
    else:
        year = str(i)

    for k in range(1, 201):
        if k < 10:
            per = "00" + str(k)
        elif k < 100:
            per = "0" + str(k)
        else:
            per = str(k)

        nop = year + per
        # print(nop)
        URL = "https://kaijiang.500.com/shtml/ssq/%s.shtml" % nop
        # print(URL)
        ball_list = []
        time.sleep(1)
        resp = requests.get(url=URL)

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
            rows = excel_tool.get_rows()
            excel_tool.additional_data(ball_list, rows)
excel_tool.close_app()
