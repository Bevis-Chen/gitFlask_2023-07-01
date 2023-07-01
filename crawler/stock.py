import requests
from bs4 import BeautifulSoup


def get_stocks():
    url = "https://tw.stock.yahoo.com/"
    stocks = []
    try:
        resp = requests.get(url)
        txt = BeautifulSoup(resp.text, "lxml")
        spans = txt.find(class_="indexChartNav").find_all("li")
        for span in spans:
            # print(span.find(class_="Fx(n)").text)
            # print(span.find(class_="Fw(600)").text)
            dict1 = {
                "分類": span.find(class_="Fx(n)").text,
                "指數": span.find(class_="Fw(600)").text,
            }
            stocks.append(dict1)
    except Exception as e:
        print("ฅ⁽͑ ˚̀ ˙̭ ˚́ ⁾̉ฅ")
        print(e)
    return stocks


if __name__ == "__main__":
    # print(get_stocks())
    print()
