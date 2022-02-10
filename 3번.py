from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
url="https://imnews.imbc.com/pc_main.html"
driver.get(url)
time.sleep(2)
html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
print("<금일 톱뉴스>")
print("(", soup.select_one("div.top_title.ellipsis").text, ")")
print(soup.select_one("div.top_sub.ellipsis2").text)
print("<추천 주요뉴스>")
news=soup.select("#content > section.news_top > div.news_header > div.news_text_right > ul > li")
for i in news:
    print("-", i.text)
print("(톱뉴스 상세내용)")
topnews=driver.find_element_by_css_selector("#content > section.news_top > div.news_header > div.top_left")
topnews.click()
time.sleep(2)
html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
print(soup.select_one("div.news_txt").text)