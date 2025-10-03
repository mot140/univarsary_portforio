import requests
url ="https://weather.tsukumijima.net/api/forecast?city=140010"
response = requests.get(url)
response.encoding = "utf-8"
data = response.json()
print(data["forecasts"][0])
