import requests
from bs4 import BeautifulSoup

URL = "https://www.kaggle.com/uciml/mushroom-classification"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="site-container")

print(type(results))
print(results.prettify())

job_elements = results.find_all("div", class_="markdown-converter__text--rendered")

for job_element in job_elements:
    print(job_element, end="\n"*2)

# Kaggle does not render the content when the client is not human