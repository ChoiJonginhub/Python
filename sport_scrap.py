from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
topic=input("관심스포츠를 말씀해주세요 :")
driver=webdriver.Chrome(ChromeDriverManager().install())
if topic=="야구":
    url="https://sports.news.naver.com/kbaseball/index"
elif topic=="해외야구":
    url="https://sports.news.naver.com/wbaseball/index"
elif topic=="축구":
    url="https://sports.news.naver.com/kfootball/index"
elif topic=="해외축구":
    url="https://sports.news.naver.com/wfootball/index"
elif topic=="농구":
    url="https://sports.news.naver.com/basketball/index"
elif topic=="배구":
    url="https://sports.news.naver.com/volleyball/index"
elif topic=="골프":
    url="https://sports.news.naver.com/golf/index"
else:
    url="https://sports.news.naver.com/general/index"
driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
head_news=soup.select('#content > div > div.home_feature > div.feature_main > div > div > div:nth-child(1) > a:nth-child(1) > div.text_area > span.title')[0].text
main_news=soup.select('#content > div > div.home_feature > div.feature_side > div > ol > li')
main_text=[]
for i in main_news:
    main_text.append(i.text)
first=driver.find_element_by_css_selector("#content > div > div.home_feature.type_headline_unit6 > div.feature_main > div > div > div:nth-child(1) > a:nth-child(1) > div.text_area > span.title")
first.click()
time.sleep(3)
html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
news=soup.select('#newsEndContents')[0].text
f=open("sport_news.html", "wt", encoding="utf-8")
f.write("""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>선택한 스포츠의 뉴스들</title>
</head>
<body>
""")
f.write("""
<h1>*당신이 선택한 스포츠:""")
f.write(topic)
f.write("</h1><br>")
f.write("해당 스포츠의 메인 뉴스<br><h2 color='green'>[")
f.write(head_news)
f.write("]</h2><br>")
f.write("""
<fieldset>
<legend>{해당 스포츠 TOP10 뉴스}</legend>
<ul>""")
for i in main_text:
    f.write("<li>")
    f.write(i)
    f.write("</li>")
f.write("""
</ul>
</fieldset>
=메인뉴스 내용=<br>
""")
f.write(news)
f.write("""
</body>
</html>
""")
f.close()
