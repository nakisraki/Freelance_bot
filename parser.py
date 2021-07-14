## -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import json




def json_load(file):
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
    return data


def KWORK(pref):
    new = {}
    for i in pref:
        try:
            URL = "https://kwork.ru/projects?c=" + i
            page = requests.get(URL)
            data = bs(page.content,'html.parser')
            cont = data.findAll('div',{'class':"card"})
            input = json_load("last")
            last = input['KWORK'][i]
            heads = [i.find('a').get("href") for i in cont]
            input['KWORK'][i] = heads[0]
            with open('last', 'w') as outfile: json.dump(input, outfile)
            ind = heads.index(last) if last in heads else len(heads)
            for i in cont[:ind]:
                head = i.find("a").text
                adr = i.find("a").get("href")
                notice = i.find("div",{"class":"wants-card__description-text br-with-lh"}).text.split("Показать полностью")[-1].replace("Скрыть","").replace("\n\n","\n")
                price = i.find("div",{"class":"wants-card__header-price"}).text
                img = i.find("img").get("src")
                path = '0'
                if 'ico-galka-green.png' not in img:
                    try:
                        download,path = requests.get(img),"Image/"+ img.split("/")[-1]
                        with open(path, 'wb') as f:
                            f.write(download.content)
                    except:
                        path = 'Image/no.png'
                else:
                    path = 'Image/no.png'
                new[head] = [adr,notice,price,path]
        except:
            print("Error in code")
    print(str(len(new)) + " New in KWORK")
    return new


def FL(pref):
    new = {}
    for i in pref:
        #try:
            URL = "https://www.fl.ru/projects/category/" + i
            page = requests.get(URL)
            data = bs(page.content, 'lxml')
            cards = data.findAll('div', {'data-id': "qa-lenta-1"})
            inp = json_load("last")
            #last = input['FL'][i]
            #heads = ["https://www.fl.ru"+i.find("a").get("href").replace("/project/","") for i in cards]
            #input['FL'][i] = heads[0]
            #with open('last', 'w') as outfile:
                #json.dump(input, outfile)
            #ind = heads.index(last) if last in heads else len(heads)
            for j in cards:
                adr = "https://www.fl.ru"+j.find("a").get("href").replace("/project/","")
                if adr not in inp['FL'][i]:
                   head = j.text.replace("\n","")
                   scrs = j.find_all("script")
                   price = str(scrs[0]).split("Безопасная сделка</a> ")[-1].split(";<span")[0].replace("&nbsp","").replace("&nbsp;","").replace(";","") + " ₽"
                   if price != "1199 ₽":
                        price = "Желаемый бюджет : " + price
                   else:
                        price = "Оплата по договоренности"

                   notice = str(scrs[1]).split('<div class="b-post__txt "> ')[-1].split("</div>")[0].replace("&nbsp"," ").replace("&nbsp;"," ")
                   if "script" in head:
                       head = head.split('<script')[0]
                   if "script" in price:
                       price = price.split('> ')[-1]
                   #print(adr)
                   #print(price)
                   #print(describe)
                   #time.sleep(7)
                   path = 'Image/no.png'
                   new[head] = [adr,notice,price,path]
                   inp['FL'][i] = inp['FL'][i] + [adr]
                else:
                    pass
            if len(inp['FL'][i]) > 200:
                inp['FL'][i] = inp['FL'][i][100:]
                print("Data was clared")
            with open('last', 'w') as outfile:
                json.dump(inp, outfile)
        #except:
        #    print("Error in code")
    print(str(len(new)) + " New in FL")
    return new


def y():
    return 0
def z():
    return 0

