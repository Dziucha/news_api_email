import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-17&sortBy=" \
      "publishedAt&apiKey=e79aef38d6a14ade8d8a3d9eea769861"

api_key = "e79aef38d6a14ade8d8a3d9eea769861"

request = requests.get(url)
content = request.text

print(content)
