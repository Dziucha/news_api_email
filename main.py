import requests
from functions import send_email

topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-01-23" \
      "&sortBy=publishedAt&apiKey=e79aef38d6a14ade8d8a3d9eea769861&language=en"

api_key = "e79aef38d6a14ade8d8a3d9eea769861"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"][:20]:
    try:
        body = body + article["title"] + "\n" + article["description"] + "\n" \
               + article["url"] + 2*"\n"
    except TypeError:
        pass

body = body.encode("ascii", "ignore")

email_message = f"""\
Subject:Today's news

{body}
"""

send_email(email_message)
