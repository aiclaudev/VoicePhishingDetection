from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
n = 0
root = 'https://www.fss.or.kr'
root_urls = []
for i in range(1, 24) :
    root_urls.append(f'https://www.fss.or.kr/fss/bbs/B0000207/list.do?menuNo=200691&bbsId=&cl1Cd=&pageIndex={i}&sdate=&edate=&searchCnd=1&searchWrd=')
#print(root_urls)
for root_url in root_urls :
    #html_root = urlopen("https://www.fss.or.kr/fss/bbs/B0000206/view.do?nttId=36733&menuNo=200690&pageIndex=1")
    #print(root_url)
    html_root = urlopen(root_url)  
    bsObject_root = BeautifulSoup(html_root, "html.parser") 
    target_urls = bsObject_root.select(".title")
    #print(target_urls[0].find("a")["href"])
    #print(target_urls[1].find("a")["href"])
    #print(target_urls[2].find("a")["href"])
    #print(target_urls[3].find("a")["href"])
    #print(target_urls[1])
    #print('gsg', len(target_urls))
    for i in range(len(target_urls)) :
        needs = ''
        target_url = root + target_urls[i].find("a")["href"]
        #print(target_url)
        #print(target_urls[i].find("a")["href"])
        #print(target_url)
        html = urlopen(target_url)
        bsObject = BeautifulSoup(html, "html.parser")
        t = bsObject.select(".b_scroll")
        if len(t) == 0 :
            continue
        else :
            needs = bsObject.select(".b_scroll")[0].get_text()
        #needs = needs.split('\n')
        #needs = [s + '\n' for s in needs]
        #print(needs)
        with open(f'{n}.txt', 'w', encoding='UTF8') as f :
            f.writelines(needs)
        n += 1
    
      

#html = urlopen("https://www.fss.or.kr/fss/bbs/B0000206/view.do?nttId=36733&menuNo=200690&pageIndex=1")
#bsObject = BeautifulSoup(html, "html.parser") 

#a = bsObject.select(".b_scroll")
#result = []
#print(type(a))
#a = str(a)
#print(type(a[0].get_text()))
#hi = a[0].get_text().split('\n')
#print(hi)
