from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
#인스타 웹페이지로 이동
driver=webdriver.Chrome(ChromeDriverManager().install())
url="https://www.instagram.com"
driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
#아이디 비밀번호 입력하고 로그인
email="아이디"
input_id=driver.find_element_by_css_selector('input._2hvTZ.pexuQ.zyHYP')
input_id.send_keys(email)
password="비밀번호"
input_ps=driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_ps.send_keys(password)
input_ps.submit()
#키워드 입력하고 이동
word='제주도맛집'
driver.get('https://www.instagram.com/explore/tags/'+word)
#첫번째 게시글로 이동
first=driver.find_element_by_css_selector("div._9AhH0")
first.click()
time.sleep(2)
tour_data=[]
for i in range(0,5):#5회 반복
    html=driver.page_source
    soup=BeautifulSoup(html, 'html.parser')
    content = soup.select("div.C4VMK>span")[0].text  # 본문
    try:
        like = soup.select("a.zV_Nj>span")[0].text  # 좋아요 갯수
    except:
        like=0
    try:
        date = soup.select("time._1o9PC.Nzb55")[0].text  # 작성시간
    except:
        date="알 수 없음"
    try:
        loca = soup.select("div.M30cS")[0].text  # 장소
    except:
        loca = " "
    data = [content, like, date, loca]
    tour_data.append(data)#데이터 저장
    next = driver.find_element_by_css_selector("div.l8mY4.feth3")
    next.click()  # 오른쪽 글로 이동
    time.sleep(2)

#pandas로 데이터프레임, 엑셀화하여 출력
jeju_df=pd.DataFrame(tour_data, columns=['본문', '좋아요', '작성시간', '위치'])
jeju_df.to_excel("jeju.xlsx", index=False)