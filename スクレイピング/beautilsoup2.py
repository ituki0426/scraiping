from bs4 import BeautifulSoup
import requests
url = 'https://www.ibaraki-ct.ac.jp/?cat=13'
soup = BeautifulSoup(res.text,'html.parser')
res = requests.get(url)
content = soup.find('span',attrs={'class':'tadv-color'})
contents = soup.find_all('span',attrs={'class':'tadv-color'})
keys=[]
for content in contents:
    key=content.text
    keys.append(key)
print(keys)
