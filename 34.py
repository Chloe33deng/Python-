import requests
from bs4 import BeautifulSoup
import os
#如果没有headers 可能会因为反爬虫而无法爬取到想要的图片
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15','Referer': 'https://m.mm131.net/'}
r=requests.get("https://m.mm131.net",headers=headers)
r.encoding='gb2312' #没有这句会乱码
soup=BeautifulSoup(r.text,'lxml')
html=soup.find('content',id='content').find('a',class_='post-title-link')['href']
#for html in htmls:
for i in range(200):
	img_req=requests.get(html,headers=headers)
	img_req.encoding='gb2312'
	img_soup=BeautifulSoup(img_req.text,'lxml')
	img_html=img_soup.find('content',id='content').find('img')
	print(img_html['src'])
	img_name=img_html['alt']+'.jpg'
	img_path='/Users/chenpeng/Desktop/图片/'
	if not os.path.exists(img_path+img_name):
		down_req=requests.get(img_html['src'],headers=headers)
		f=open(img_path+img_name,'wb')
		f.write(down_req.content)
		f.close()
	else:
		print("{}图片已下载".format(img_name))
	html='https://m.mm131.net/xinggan/'+img_soup.find('content',id='content').find('a')['href']

