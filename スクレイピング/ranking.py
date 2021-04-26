import requests
from bs4 import BeautifulSoup
url = 'https://scraping-for-beginner.herokuapp.com/ranking'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
spots = soup.find_all('div',attrs={'class':'u_areaListRankingBox'})
spot = spots[0]
spot_name=spot.find('div',attrs={'class':'u_title'})
spot_namekai=spot_name.find('span',attrs={'class':'badge'}).extract()
#extract()を使うと指定したタグ全体を削除する
spot_last=spot_namekai.text.replace('\n','')
#replace()を使うと指定した文字を指定した文字に置換する
hyoutei = spot.find('span',attrs={'class':'evaluateNumber'})
hyoutei_text=hyoutei.text
hyoutei_text2=float(hyoutei_text)
print(hyoutei_text2)
Categorie= spot.find('div',attrs={'class':'u_categoryTipsItem'})
print(Categorie.text)
first = Categorie.find_all('dl')
print(first)
first_1 = first[1]
print(first_1)
first_2 = first_1.find('dt')
first_3 = first_2.text

first_4=first_1.find('span')
rank = float(first_4.text)
details = {}
first_4=first_1.find('span')
rank = float(first_4.text)
details = {}
for first_1 in first:
 first_2 = first_1.find('dt')
 first_3 = first_2.text
 first_4=first_1.find('span')
 rank = float(first_4.text)
 details[first_3] = rank
datum = details
datum['観光地名']=spot_last
datum['評点']=hyoutei_text2
print(datum)
