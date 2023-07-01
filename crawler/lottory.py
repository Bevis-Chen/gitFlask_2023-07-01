import requests
from bs4 import BeautifulSoup


def get_lottory():
    def get_balls(name):
        main = txt.find(id=f"contents_logo_{lottory_group[name]}").find_parent("div")
        date = main.find("span", class_="font_black15").text.replace("\xa0", ",")
        numbers = main.find_all("div", class_="ball_tx")[6:]
        numlist = " ".join([number.text.strip() for number in numbers])
        return date, numlist

    lottory_group = {"威力彩": "02", "大樂透": "04", "今彩539": "06"}
    url = "https://www.taiwanlottery.com.tw/index_new.aspx"
    # url = "23"
    datas = {}
    try:
        resp = requests.get(url)
        txt = BeautifulSoup(resp.content, "lxml")
        for name in lottory_group:
            datas[name] = get_balls(name)
        dollars = [
            dollar.text.strip().replace("\n\n", " ")
            for dollar in txt.find_all("div", class_="top_dollar_tx")
        ]
    except Exception as e:
        print(e)
    return dollars, datas


# print(get_lottory())

if __name__ == "__main__":
    print()
    print(get_lottory())
