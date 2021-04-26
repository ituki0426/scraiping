from bs4 import BeautifulSoup
import requests
url = 'https://scraping-for-beginner.herokuapp.com/udemy'
soup = BeautifulSoup(res.text,'html.parser')
res = requests.get(url)
reviews=soup.find_all('p',attrs={'class':'reviews'})[0]
print(content.text)
n_reviews=int(reviews.text.split('：')[1])
print(n_reviews)