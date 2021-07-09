from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import requests

#set headers
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36','Referer':'https://www.amazon.com/stores/page/0B6B05F4-EE4D-4696-A789-BB7152AB8DCE?ingress=0&visitId=9365015c-39f1-4f05-8ec9-61dfafb3a84a&channel=SB-gway&liveVideoDataUrl=https%3A%2F%2Famazonlive-portal.amazon.com%2Fv2&ref_=sb_w_i_ctcd_snkrs&productGridPageIndex=4'}

#Define URL and send get request

url = 'https://www.amazon.com/Lacoste-Carnaby-Sneaker-White-Medium/dp/B07T5Q2VLG?s=shopbop&ref_=sb_ts'
html = requests.get(url,headers=header)

#Create BeautifulSoup object
bsobj = soup(html.content,'lxml')

#Brand Name
bsobj.findAll('div',{'class':'a-section a-spacing-none'})[0].a.text

#product name
bsobj.h1.text.strip()

#Ratings
bsobj.findAll('i',{'class':'a-icon a-icon-star a-star-3'})[0].text

#Price
bsobj.findAll('table',{'class':'a-lineitem'})[0].tr.span.text

#Shoe Size
for a in bsobj.findAll('span',{'class':'a-dropdown-container'})[0].findAll('option')[1:]:
  print(a.text.strip())
  
#Shoe Color
colors =[]
for a in range(0,6):
  name = 'color_name_' + str(a)
  colors.append(name)
  
for color in bsobj.findAll('li',{'id':colors}):print(color.img['alt'])