import requests

api_key = "4088b18a8c3d438bad562e7442364eca"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-15&sortBy" \
      "=publishedAt&apiKey=4088b18a8c3d438bad562e7442364eca"

# Make request
request = requests.get(url)
# Get dictionary with data
content = request.json()
# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

