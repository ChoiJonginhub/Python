from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
url="https://movie.naver.com/"#네이버 영화 사이트 접속
driver.get(url)
movie="너의 이름은"
input_mv=driver.find_element_by_css_selector('input.ipt_tx_srch')
input_mv.send_keys(movie)
search=driver.find_element_by_css_selector("#jSearchArea > div > button")
search.click()
get_movie=driver.find_element_by_css_selector("#old_content > ul.search_list_1 > li:nth-child(1) > p > a")
get_movie.click()
html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
title=soup.select_one("title").text
gaeyo=soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span>a")
mv_info=[]
for i in gaeyo:
    mv_info.append(i.text)
comment=soup.select_one("#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_result > ul > li:nth-child(1) > div.score_reple > p").text.strip()
print("영화제목:", title[:-9])
print("개요:", mv_info[:3])
print("대표 한줄평:", comment)
