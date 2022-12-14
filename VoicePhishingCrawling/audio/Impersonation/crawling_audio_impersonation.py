from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request
import os

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
    #tp = bsObject_root.find('a', class_='bd-list-thumb-a')
    target_urls = bsObject_root.select(".title")
    #print(target_urls)
    #print(len(target_urls))
    #print(target_urls[1].find('a')['href'])
    #print(target_urls[2].find('a')['href'])
    #print(target_urls[3].find('a')['href'])
    
    #tmp = target_urls.find('a')['href']
    targetURLs = []
    for t in target_urls :
        targetURLs.append(t.find('a')['href'])
    print(targetURLs)
    
    for i in targetURLs :
        needs = ''
        target_url = root + i
        #print(target_url)
        #break
        #print(target_url)
        #print(target_urls[i].find("a")["href"])
        #print(target_url)
        html = urlopen(target_url)
        bsObject = BeautifulSoup(html, "html.parser")
        t = bsObject.select(".dbdata")
        b = t[0].find('video')['src']
        #print(type(t))
        file_url = root + b
        os.chdir('C:/Users/82102/Desktop/Project/LIFLOW/221017/금감원 크롤링/audio/수사기관 사칭')
        request.urlretrieve(file_url, f'{n}.mp4')
        #print(t)
        """
        if len(t) == 0 :
            continue
        else :
            needs = bsObject.select(".b_scroll")[0].get_text()
        #needs = needs.split('\n')
        #needs = [s + '\n' for s in needs]
        #print(needs)
        with open(f'{n}.txt', 'w', encoding='UTF8') as f :
            f.writelines(needs)
        """
        n += 1
    #break
    
print("END")
#html = urlopen("https://www.fss.or.kr/fss/bbs/B0000206/view.do?nttId=36733&menuNo=200690&pageIndex=1")
#bsObject = BeautifulSoup(html, "html.parser") 

#a = bsObject.select(".b_scroll")
#result = []
#print(type(a))
#a = str(a)
#print(type(a[0].get_text()))
#hi = a[0].get_text().split('\n')
#print(hi)
