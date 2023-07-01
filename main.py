from flask import Flask, render_template
from datetime import datetime


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
    for stock in stocks:
        print(stock["分類"], stock["指數"])
    return render_template("stock.html", stocks=stocks, now=now())


def now():
    nowtime = datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
    # return f"<h2>{nowtime}</h2>"
    return nowtime


if __name__ == "__main__":
    # print(stock())
    # 資料固定所以放這裡
    stocks = [
        {"分類": "日經指數", "指數": "22,920.30"},
        {"分類": "韓國綜合", "指數": "2,304.59"},
        {"分類": "香港恆生", "指數": "25,083.71"},
        {"分類": "上海綜合", "指數": "3,380.68"},
    ]
    app.run(debug=True)
