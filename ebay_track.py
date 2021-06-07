import pandas as pd 
import numpy as np 
import requests 
from bs4 import BeautifulSoup
import math 
import re 
import altair as alt 
from datetime import datetime 
from dateutil import parser
import dateutil.parser
import altair_viewer
import scipy.stats as stats
import seaborn as sns 
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go


#ebay tracker
product='adidas basketball sneakers' #add product description 

#page1 
url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312&_nkw=adidas+basketball+sneakers&_sacat=0"
page=requests.get(url)
soup=BeautifulSoup(page.content)
sd1=soup.find_all('span',class_=re.compile('s-item__price'))

#item prices 
p1=[]
for f in sd1:
    print(f.get_text()) 
    p1.append(f.get_text())

#item description 
sd2=soup.find_all('span',class_=re.compile('BOLD'))
p2=[]
for f in sd2:
    print(f.get_text()) 
    p2.append(f.get_text())

#item bids
sd3=soup.find_all('span',class_="s-item__bids s-item__bidCount")
p3=[]
for f in sd3: 
    print(f.get_text())
    p3.append(f.get_text())

#lists to dataframes 
d1=pd.DataFrame({'desc':p2})
d2=pd.DataFrame({'bids':p3})
d2['bids'] = d2['bids'].replace('bids','',regex=True)
d2['bids'] = d2['bids'].replace('bid','',regex=True)
d2['bids'] = d2['bids'].astype(float)
d3=pd.DataFrame({'price':p1})
d3['price'] = d3['price'].map(lambda x: x.lstrip('$').rstrip('aAbBcC'))
d3['price'] = d3['price'].replace(',','',regex=True)
d3['price']=d3[~d3.price.str.contains('to')]
d3['price'] = d3['price'].astype(float)

#page 2 
url="https://www.ebay.com/sch/i.html?_from=R40&_nkw=adidas+basketball+sneakers&_sacat=0&_pgn=2"
page=requests.get(url)
soup=BeautifulSoup(page.content)
sd1=soup.find_all('span',class_=re.compile('s-item__price'))

p1=[]
for f in sd1:
    print(f.get_text()) 
    p1.append(f.get_text())

sd2=soup.find_all('span',class_=re.compile('BOLD'))
p2=[]
for f in sd2:
    print(f.get_text()) 
    p2.append(f.get_text())

sd3=soup.find_all('span',class_="s-item__bids s-item__bidCount")
p3=[]
for f in sd3: 
    print(f.get_text())
    p3.append(f.get_text())

d1x=pd.DataFrame({'desc':p2})
d2x=pd.DataFrame({'bids':p3})
d2x['bids'] = d2x['bids'].replace('bids','',regex=True)
d2x['bids'] = d2x['bids'].replace('bid','',regex=True)
d2x['bids'] = d2x['bids'].astype(float)
d3x=pd.DataFrame({'price':p1})
d3x['price'] = d3x['price'].map(lambda x: x.lstrip('$').rstrip('aAbBcC'))
d3x['price'] = d3x['price'].replace(',','',regex=True)
d3x['price']=d3x[~d3x.price.str.contains('to')]
d3x['price'] = d3x['price'].astype(float)


#page 3 
url="https://www.ebay.com/sch/i.html?_from=R40&_nkw=adidas+basketball+sneakers&_sacat=0&_pgn=3"
page=requests.get(url)
soup=BeautifulSoup(page.content)
sd1=soup.find_all('span',class_=re.compile('s-item__price'))

p1=[]
for f in sd1:
    print(f.get_text()) 
    p1.append(f.get_text())

sd2=soup.find_all('span',class_=re.compile('BOLD'))
p2=[]
for f in sd2:
    print(f.get_text()) 
    p2.append(f.get_text())

sd3=soup.find_all('span',class_="s-item__bids s-item__bidCount")
p3=[]
for f in sd3: 
    print(f.get_text())
    p3.append(f.get_text())

d1xx=pd.DataFrame({'desc':p2})
d2xx=pd.DataFrame({'bids':p3})
d2xx['bids'] = d2xx['bids'].replace('bids','',regex=True)
d2xx['bids'] = d2xx['bids'].replace('bid','',regex=True)
d2xx['bids'] = d2xx['bids'].astype(float)
d3xx=pd.DataFrame({'price':p1})
d3xx['price'] = d3xx['price'].map(lambda x: x.lstrip('$').rstrip('aAbBcC'))
d3xx['price'] = d3xx['price'].replace(',','',regex=True)
d3xx['price']=d3xx[~d3xx.price.str.contains('to')]
d3xx['price'] = d3xx['price'].astype(float)

#page 4 
url="https://www.ebay.com/sch/i.html?_from=R40&_nkw=adidas+basketball+sneakers&_sacat=0&_pgn=4"
page=requests.get(url)
soup=BeautifulSoup(page.content)
sd1=soup.find_all('span',class_=re.compile('s-item__price'))

p1=[]
for f in sd1:
    print(f.get_text()) 
    p1.append(f.get_text())

sd2=soup.find_all('span',class_=re.compile('BOLD'))
p2=[]
for f in sd2:
    print(f.get_text()) 
    p2.append(f.get_text())

sd3=soup.find_all('span',class_="s-item__bids s-item__bidCount")
p3=[]
for f in sd3: 
    print(f.get_text())
    p3.append(f.get_text())

d1xxx=pd.DataFrame({'desc':p2})
d2xxx=pd.DataFrame({'bids':p3})
d2xxx['bids'] = d2xxx['bids'].replace('bids','',regex=True)
d2xxx['bids'] = d2xxx['bids'].replace('bid','',regex=True)
d2xxx['bids'] = d2xxx['bids'].astype(float)
d3xxx=pd.DataFrame({'price':p1})
d3xxx['price'] = d3xxx['price'].map(lambda x: x.lstrip('$').rstrip('aAbBcC'))
d3xxx['price'] = d3xxx['price'].replace(',','',regex=True)
d3xxx['price'] = d3xxx['price'].replace('$','',regex=True)
d3xxx['price']=d3xxx[~d3xxx.price.str.contains('to')]
d3xxx['price'] = d3xxx['price'].astype(float)

#page 5 
url="https://www.ebay.com/sch/i.html?_from=R40&_nkw=adidas+basketball+sneakers&_sacat=0&_pgn=5"
page=requests.get(url)
soup=BeautifulSoup(page.content)
sd1=soup.find_all('span',class_=re.compile('s-item__price'))

p1=[]
for f in sd1:
    print(f.get_text()) 
    p1.append(f.get_text())

sd2=soup.find_all('span',class_=re.compile('BOLD'))
p2=[]
for f in sd2:
    print(f.get_text()) 
    p2.append(f.get_text())

sd3=soup.find_all('span',class_="s-item__bids s-item__bidCount")
p3=[]
for f in sd3: 
    print(f.get_text())
    p3.append(f.get_text())

d1xxxx=pd.DataFrame({'desc':p2})
d2xxxx=pd.DataFrame({'bids':p3})
d2xxxx['bids'] = d2xxxx['bids'].replace('bids','',regex=True)
d2xxxx['bids'] = d2xxxx['bids'].replace('bid','',regex=True)
d2xxxx['bids'] = d2xxxx['bids'].astype(float)
d3xxxx=pd.DataFrame({'price':p1})
d3xxxx['price'] = d3xxxx['price'].map(lambda x: x.lstrip('$').rstrip('aAbBcC'))
d3xxxx['price'] = d3xxxx['price'].replace(',','',regex=True)
d3xxxx['price']=d3xxxx[~d3xxxx.price.str.contains('to')]
d3xxxx['price'] = d3xxxx['price'].astype(float)

#combine the item dataframes
df1=pd.concat([d1,d1x,d1xx,d1xxx,d1xxxx],axis=0) #desc 
df2=pd.concat([d2,d2x,d2xx,d2xxx,d2xxxx],axis=0) #bids 
df3=pd.concat([d3,d3x,d3xx,d3xxx,d3xxxx],axis=0) #price 

#***************************************************************
#product visualizations 

#price viz 
f1=alt.Chart(df3).mark_bar().encode(
    alt.X("price", bin=True),
    y='count()',
).properties(height=300,width=250,title="Price Distribution For " + product + " on Ebay")
f1.show()

#bids viz 
f2=alt.Chart(df2).mark_bar().encode(
    alt.X("bids", bin=True),
    y='count()',
).properties(height=300,width=250,title="Bids Distribution For " + product + " on Ebay")
f2.show()

#sample product price
f1= go.Figure(data=[go.Table(
    header=dict(values=list(df3.columns),
                fill_color='white',
                align='left'),
    cells=dict(values=[df3.price],
               fill_color='white',
               align='left'))
])

f1.update_layout(
    height=800,
    showlegend=False,
    title_text="Sample of Listed Prices on Ebay For  " +  product ,
)

f1.show() 

#sample product bids  
f2= go.Figure(data=[go.Table(
    header=dict(values=list(df2.columns),
                fill_color='white',
                align='left'),
    cells=dict(values=[df2.bids],
               fill_color='white',
               align='left'))
])

f2.update_layout(
    height=800,
    showlegend=False,
    title_text="Sample of Bids on Ebay For " +  product ,
)

f2.show() 

#the average price, bids, and count of sampled products
avg_price=df3.mean()
avg_price=round(avg_price[0],3)
avg_price=str(avg_price)
avg_bids=df2.mean()
avg_bids=round(avg_bids[0],3)
avg_bids=str(avg_bids) 
count_items=df3.shape[0]
count_items=str(count_items)

print("The average price for " + product + " is $" + avg_price)
print("The average bids for " + product + " is " + avg_bids)
print("The number of listed items for " + product + " is " + count_items)
