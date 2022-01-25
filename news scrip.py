from bs4 import BeautifulSoup
import urllib.request as req

url="https://news.daum.net/"
res=req.urlopen(url)
soup=BeautifulSoup(res, "html.parser")

news=soup.select("div.thumb_relate")

for list in news:
    a=list.select_one("a")
    print("링크: "+a.get('href'))
    
    title=a.string
    print("제목:", title)
    span=list.select_one("span")
    print("언론사:", span.string)
