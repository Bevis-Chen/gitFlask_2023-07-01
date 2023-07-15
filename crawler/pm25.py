import requests
from bs4 import BeautifulSoup
import pandas as pd


# 讀取CSV
url = "https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=CSV"

df = None


def get_six_pm25():
    global df

    try:
        df = pd.read_csv(url).dropna()
        six_countys = ["臺北市", "新北市", "臺中市", "桃園市", "臺南市", "高雄市"]
        datas = []
        for county in six_countys:
            value = df.groupby("county").get_group(county)["pm25"].mean()
            datas.append([county, round(value, 1)])
        return datas
    except Exception as e:
        print(e)


def get_pm25(sort=False):
    # data = []
    try:
        df = pd.read_csv(url).dropna()
        columns = df.columns.tolist()
        values = df.values.tolist()
        highest = df.sort_values("pm25").iloc[-1][["site", "pm25"]].tolist()
        lowest = df.sort_values("pm25").iloc[0][["site", "pm25"]].tolist()
        if sort:
            values = sorted(values, key=lambda x: x[2], reverse=True)
    except Exception as e:
        print(e)
    return columns, values, highest, lowest


def get_json():
    pass


if __name__ == "__main__":
    print(get_pm25())
