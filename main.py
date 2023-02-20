import requests
from functions import send_email

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-23&sortBy=" \
      "publishedAt&apiKey=e79aef38d6a14ade8d8a3d9eea769861"

api_key = "e79aef38d6a14ade8d8a3d9eea769861"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    try:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
    except TypeError:
        pass

body = body.encode("ascii", "ignore")

email_message = f"""\
Subject:Tesla news

{body}
"""

send_email(email_message)
