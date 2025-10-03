import requests

class test:
    @staticmethod
    def json():
        url ="https://weather.tsukumijima.net/api/forecast?city=140010"
        response = requests.get(url)
        response.encoding = "utf-8"
        data = response.json()
        return data
    