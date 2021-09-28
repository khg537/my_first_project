import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

url = "https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"

r = requests.get(url, headers=headers)
bs = BeautifulSoup(r.text, "lxml")

number = []
name = []
position = []
age = []
nation =[]
team=[]
value =[]

player_info = bs.find_all('tr',  class_ = ['odd', 'even'])

for info in player_info:
    player = info.find_all("td")
    number.append(player[0].text)
    name.append(player[1].img['title'])
    position.append(player[4].text)
    age.append(player[5].text)
    nation.append(player[6].img['alt'])
    team.append(player[7].img['alt'])
    value.append(player[8].span['title'])


my_data = { 'number': number, 'name': name, 'position': position, 'age':age , 'nation':nation, 'team':team, 'value': value}
df = pd.DataFrame(my_data)

print(df)



