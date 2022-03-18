import requests
import xlwings as xw
import pandas as pd
from bs4 import BeautifulSoup

# year:03-22
# per:001-200
years = ["03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
pers = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015", "016", "017", "018", "019", "020",
        "021", "022", "023", "024", "025", "026", "027", "028", "029", "030", "031", "032", "033", "034", "035", "036", "037", "038", "039", "040",
        "041", "042", "043", "044", "045", "046", "047", "048", "049", "050", "051", "052", "053", "054", "055", "056", "057", "058", "059", "060",
        "061", "062", "063", "064", "065", "066", "067", "068", "069", "070", "071", "072", "073", "074", "075", "076", "077", "078", "079", "080",
        "081", "082", "083", "084", "085", "086", "087", "088", "089", "090", "091", "092", "093", "094", "095", "096", "097", "098", "099", "100",
        "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120",
        "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140",
        "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160",
        "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180",
        "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200"]

big_ball_list = []
for i in range(len(years)):
    year = years[i]
    for j in range(len(pers)):
        per = pers[j]
        year_per = year + per
        url = "https://kaijiang.500.com/shtml/ssq/%s.shtml" % year_per
        resp = requests.get(url=url)
        resp.encoding = "gb2312"
        status_code = resp.status_code
        if status_code == 200:
            html_doc = resp.text
            soup = BeautifulSoup(html_doc, "html.parser")

            red_balls = soup.find_all("li", attrs={"class": "ball_red"})
            # red ball list
            red_ball_list = []
            for k in range(len(red_balls)):
                red_ball = str(red_balls[k]).replace("<li class=\"ball_red\">", "").replace("</li>", "")
                red_ball_list.append(int(red_ball))

            # blue ball list
            blue_ball_list = []
            blue_balls = soup.find_all("li", attrs={"class": "ball_blue"})
            blue_ball = str(blue_balls[0]).replace("<li class=\"ball_blue\">", "").replace("</li>", "")
            blue_ball_list.append(int(blue_ball))
            print("red_ball_list: ", red_ball_list)
            print("blue_ball_list: ", blue_ball_list)

            data_list = [year_per] + red_ball_list + blue_ball_list
            big_ball_list.append(data_list)
        else:
            pass
        # print("resp_text: ", resp.text)
excel_data = pd.DataFrame([big_ball_list], columns=["期数", "1号红球", "2号红球", "3号红球", "4号红球", "5号红球", "6号红球", "蓝球"])
excel_data.to_excel("TCB.xlsx")

