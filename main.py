from flask import Flask, render_template, request
from datetime import datetime
from crawler.stock import get_stocks
from crawler.lottory import get_lottory
from crawler.pm25 import get_pm25
import requests

app = Flask(__name__)


@app.route("/bmi/height=<h>&&weight=<w>")
def bmi(w, h):
    try:
        bmi = eval(w) / (eval(h) / 100) ** 2
        return f"bmi: {bmi}"
    except Exception as e:
        print(e)
        return "one More!"


@app.route("/book/<int:id>")
def books(id):
    try:
        books = {1: "Python", 2: "Java"}
        return books[id]
    except Exception as e:
        print(e)
        return "查無資料!"


@app.route("/today")
def today():
    nowtime = datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
    return f"<h2>{nowtime}</h2>"


@app.route("/index")
@app.route("/")
def index():
    name = "Austin"
    date = datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
    content = {"name": name, "date": date}
    return render_template("index.html", content=content)


@app.route("/stock")
def stock():
    stocks = get_stocks()
    # for stock in stocks:
    #     print(stock["分類"], stock["指數"])
    return render_template("stock.html", stocks=get_stocks(), now=now())


@app.route("/lotto")
def lotto():
    lottory_group = {"威力彩": "02", "大樂透": "04", "今彩539": "06"}
    lotto = get_lottory()[1]
    dollars = get_lottory()[0]

    return render_template(
        "lotto.html", lotto=get_lottory()[1], dollars=get_lottory()[0]
    )


@app.route("/pm25", methods=["GET", "POST"])
def pm25():
    # print(request)
    sort = True
    # sort = request.args.get("sort")
    # print(sort)
    if request.method == "POST":
        sort = request.form.get("sort")
        print(sort)

    columns, values = get_pm25(sort)

    return render_template("pm25.html", sort=sort, columns=columns, values=values)


def now():
    nowtime = datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
    # return f"<h2>{nowtime}</h2>"
    return nowtime


if __name__ == "__main__":
    # print(stock())
    # print(get_stocks())
    # 資料固定所以放這裡
    stocks = [
        {"分類": "日經指數", "指數": "22,920.30"},
        {"分類": "韓國綜合", "指數": "2,304.59"},
        {"分類": "香港恆生", "指數": "25,083.71"},
        {"分類": "上海綜合", "指數": "3,380.68"},
    ]

    app.run(debug=True)
