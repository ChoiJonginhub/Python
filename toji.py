from bs4 import BeautifulSoup
toji=open("toji.html","r",encoding='utf-16')
soup=BeautifulSoup(toji,'html.parser')
writer=soup.select_one("author").text
extent=soup.select_one("extent").text
publisher=soup.select_one("publisher").text
title=soup.select_one("title").text
date=soup.select_one("date").text
heads=soup.select("head")
print("저자명:", writer)
print("어절:", extent)
print("출판사:", publisher)
print("제목:",title[:-5])
print("출판연도:", date+"\n")
print(heads[0].text)
for i in heads[2:]:
    k=i.text
    print(k)
