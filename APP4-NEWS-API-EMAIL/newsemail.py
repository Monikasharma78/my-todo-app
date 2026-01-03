import requests
from sentemail import send_email
topic = "apple"
api_key = "a636bab2243b415a8130c90de32d079e"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&from" \
     "=2026-01-02&to=2026-01-02&sortBy=popularity&apiKey=a636bab2243b415a8130c90de32d079e&" \
     "language=en"
#Make request
response = requests.get(url)
#content = response.text
#print(content)

#Get a dictionary with data
content = response.json()

#Access the Article titles and description
#print(len(content["articles"]))
body =""
for article in content["articles"][:15]:
    #print(article["description"])
    #print(article["title"])
    #if article["title"] is not None:
    #body = body + article["title"] + "\n" + article["description"] + 2*"\n"

    body ="Subject: Today's news" + "\n" + body + str(article.get("title") or "") + "\n" \
           + str(article.get("description") or "") + "\n" \
           + str(article.get("url") or "") +"\n\n"
body=body.encode("utf-8")
send_email(message=body)






























