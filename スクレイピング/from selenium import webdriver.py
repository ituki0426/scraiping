from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#ヘッドレスモードに必要なモジュール
import chromedriver_binary

# オプションの作成
option = Options()     
# ヘッドレスモードの設定      
option.add_argument('--headless')
# Chromeをヘッドレスモードにする
driver = webdriver.Chrome(options=option)

#Chrome上でURLを指定してGETリクエスト・このURLを開きます。
driver.get("https://www.google.com/?hl=ja")
 
#検索窓のxpathを指定
element = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
#pythonと入力
element.send_keys("python")
#エンターを押します。
element.send_keys('\n')
#検索1番目を取得
element = driver.find_element_by_xpath("//*[@id='rso']/div/div/div[1]/div/div/div[1]/a/h3")
print(element.text)

# ドライバを閉じるChromeも終了する
driver.quit()