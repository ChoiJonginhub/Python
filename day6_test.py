import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

train=pd.read_csv('train_b.csv')

train.info()
train['datetime']

#datetime-날짜형식(년월일시 분리) 시간대별 자전거 대여수?

train['year']=pd.to_datetime(train['datetime']).dt.year
train['month']=pd.to_datetime(train['datetime']).dt.month
train['day']=pd.to_datetime(train['datetime']).dt.day
train['hour']=pd.to_datetime(train['datetime']).dt.hour

#datetime-날짜형식(년월일시 분리) 시간대별 자전거 대여수?
train.groupby('hour')['count'].value_counts()
#season 에 따른 자전거 대여수? 
train.groupby('season')['count'].value_counts()
#holiday 에 따른 자전거 대여수?
train.groupby('holiday')['count'].value_counts()
#weather 에 따른 자전거 대여수?
train.groupby('weather')['count'].value_counts()
#temp 에 따른 자전거 대여수?
train.groupby('temp')['count'].value_counts()
#humidity  에 따른 자전거 대여수?
train.groupby('humidity')['count'].value_counts()
#windspeed 에 따른 자전거 대여수?
train.groupby('windspeed')['count'].value_counts()


hour_c=train.pivot_table('count','hour')
season_c=train.pivot_table('count','season')
holiday_c=train.pivot_table('count','holiday')
weather_c=train.pivot_table('count','weather')
temp_c=train.pivot_table('count','temp')
windspeed_c=train.pivot_table('count','windspeed')


import seaborn as sns

import matplotlib
from matplotlib import font_manager, rc
import platform
if platform.system()=="Windows":
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus']=False

import warnings
warnings.filterwarnings("ignore")


plt.plot(hour_c.index, hour_c['count'])
plt.xlabel('시간대')
plt.ylabel('자전거대여수')
plt.title('시간대별 자전거 대여')


season_c.plot(kind='bar', color='skyblue')
plt.xlabel('시즌')
plt.ylabel('자전거대여수')
plt.title('시즌별 자전거 대여')

holiday_c.plot(kind='bar')

train.plot(kind='scatter', x='weather', y='count', c='orange', s=10)
plt.title('날씨별 자전거 대여')

train.plot(kind='scatter', x='temp', y='count', c='pink', s=10)
plt.title('온도별 자전거 대여')
