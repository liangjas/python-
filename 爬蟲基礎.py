import requests
from bs4 import BeautifulSoup
#前面需要先去系統下載requests和BeautifulSoup
#這很重要!!!

# 目標網站 
url = ''
# 發送 GET 請求到目標網站
response = requests.get(url)

# 確認請求成功
if response.status_code == 200:
    # 解析 HTML
    soup = BeautifulSoup(response.text, 'lxml')

    # 找到所有標題
    titles = soup.find_all('a', class_='storylink')

    # 打印每個標題
    for index, title in enumerate(titles):
        print(f"{index + 1}. {title.get_text()}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")