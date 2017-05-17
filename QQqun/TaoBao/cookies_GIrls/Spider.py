#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import tool
import os
import http.cookiejar
from urllib2 import urlopen

#抓取MM
class Spider:

	#页面初始化
	def __init__(self):
		self.siteURL = 'https://mm.taobao.com/json/request_top_list.htm'
		self.tool = tool.Tool()

	#获取索引页面的内容
	def getPage(self,pageIndex):
		url = self.siteURL + "?page=" + str(pageIndex)
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read().decode('gbk')

	#获取索引界面所有MM的信息，list格式
	def getContents(self,pageIndex):
		page = self.getPage(pageIndex)
		pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
		items = re.findall(pattern,page)
		contents = []
		for item in items:
			contents.append([item[0],item[1],item[2],item[3],item[4]])
		return contents

	#获取MM个人详情页面
	def getDetailPage(self,infoURL):
		def makeMyOpener(head = {
			'accept-encoding':'deflate, sdch',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Language': 'zh-CN,zh;q=0.8',
			#此处填写浏览器发送的cookie数据，开发者模式可捕获
			'cookie':'mt=ci%3D-1_0; swfstore=175300; miid=6024843796364610146; cna=P4abDr4n/nYCAd4UJKclEvP5; v=0; tk_trace=oTRxOWSBNwn9dPyscxqAz9fIO73QQFhF7kVkgTL59JVC7kpHTxat6tLGFTB1Ee398YXFDzNwl8A9IzonLcCJCAEL9tNKym86NxOGePc2ON8tMUTcpViURxhRMs5HruPxVXZnMKJZdesyct2XkVumqfd68uXgZDzk7MX2T391dDZLxf%2F%2Bv%2Fr%2BEKRguvkK1wc12SldPUQVmoKxn29sV78dc1%2F3VkK%2FwW4pxPVtLhfv%2FVESEqBssWI%2B2J3yARKlM22BT%2BdP5%2FDPdhC7iuy67dofgBg6H3htJVN61%2B2aHML9WddDu0hdthqzWvGTZewmNo7%2BhsJfI0A5Jn8ceS3VeFz8Zyfui4WzsnMT1nTgL3D0TXIfnsvvrQtK4NETzybFYi4hOoCtgQqrpnPZ0txQlQMUbzAAFW8FACvcHi75SYlpQ8CXk2QEbwOMgqVRRhpHqqFNog78FcJWTgMfDTL1B5b%2Bx6Sy%2Bu%2BrEBMBrwxbWhkH%2Fd%2FscML%2F4yspR86l4DiPrEW0697BQwKUZP2Eb4%2BCyUcJcwlmxjEQ7%2BmQShxETjQkUJjFmK0dk0J1lTtu3upVkskFcigqsTmv6m0CjuIzKEXruTo7xji3lxFC8wxsVDTbHvD%2F%2FXwkiP3OuhaNdFErQe1iI3FJNPiAT%2FNsIVu57l4UqkqXRAzQrqdfYux1mZoMX4VXrTRuYcFBOI6VPmUXYSv49Ql1KhGPzXGR0pHM898mOjGZ3Co%3D; _tb_token_=gicDteN5Mdp; thw=cn; uc3=nk2=tfXtw6t5DHo%3D&id2=VWn0%2FIhglnpe&vt3=F8dARHKr2dLWxGNcThQ%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTQ3ODA3NDI4OQ%3D%3D; lgc=%5Cu5FD7%5Cu7EDF%5Cu5929%5Cu4E0B; tracknick=%5Cu5FD7%5Cu7EDF%5Cu5929%5Cu4E0B; cookie2=1d840641e827300a90d22cb8a79a36db; sg=%E4%B8%8B1a; cookie1=URsUvVDpRqhlIAeuQJTUC9syfqik1sAl43FAWek4bYI%3D; unb=668021201; skt=77364f2adc1d8cad; t=b713786e6222484cb1c5fdfafd5c9954; _cc_=URm48syIZQ%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=%5Cu5FD7%5Cu7EDF%5Cu5929%5Cu4E0B; cookie17=VWn0%2FIhglnpe; mt=ci=63_1; CNZZDATA30064598=cnzz_eid%3D685840673-1478074058-https%253A%252F%252Fmm.taobao.com%252F%26ntime%3D1478074058; CNZZDATA30063600=cnzz_eid%3D229860023-1478071142-https%253A%252F%252Fmm.taobao.com%252F%26ntime%3D1478071142; JSESSIONID=E4DC8B8A01667AEF9315507ADF600DAF; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=URm48syIYn73&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&pas=0&cookie14=UoWwLAWNV%2Fzp6Q%3D%3D&tag=7&lng=zh_CN; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; l=ApiYMRRGlsNEbjFQZEFM2pbD6MwqgfwL; isg=Ar-_Qsz82--9ttCV4-D3av-MTpONHBNGHFfxAlGMW261YN_iWXSjlj1y1Idk; whl=-1%260%260%261478074526697',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
		}):
			cookie = http.cookiejar.CookieJar()
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
			header = []
			for key, value in head.items():
				elem = (key, value)
				header.append(elem)
			opener.addheaders = header
			return opener

		oper = makeMyOpener()
		uop = oper.open(infoURL)
		data = uop.read().decode('UTF-8')
		return data
		# response = urllib2.urlopen(infoURL)
		# return response.read().decode('gbk')

	#获取个人文字简介
	def getBrief(self,page):
		pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		result = re.search(pattern,page)
		print(result.group())
		return self.tool.replace(result.group(1))

	#获取页面所有图片
	def getAllImg(self,page):
		pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		#个人信息页面所有代码
		content = re.search(pattern,page)
		#从代码中提取图片
		patternImg = re.compile('<img.*?src="(.*?)"',re.S)
		images = re.findall(patternImg,content.group(1))
		return images

	#保存多张写真图片
	def saveImgs(self,images,name):
		number = 1
		print (u"发现",name,u"共有",len(images),u"张照片")
		for imageURL in images:
			splitPath = imageURL.split('.')
			splitPath=splitPath
			fTail = splitPath.pop()
			if len(fTail) > 3:
				fTail = "jpg"
			fileName = name + "/" + str(number) + "." + fTail
			imageURL='https:'+imageURL
			self.saveImg(imageURL,fileName)
			number += 1

	# 保存头像
	def saveIcon(self,iconURL,name):
		splitPath = iconURL.split('.')
		fTail = splitPath.pop()
		fileName = name + "/icon." + fTail
		self.saveImg(iconURL,fileName)

	#保存个人简介
	def saveBrief(self,content,name):
		fileName = name + "/" + name + ".txt"
		f = open(fileName,"w+")
		print (u"正在保存信息为",fileName)
		f.write(content.decode('utf-8'))

	#保存图片地址页到各文件夹中
	def saveToLocal(self,Li,name):
		fileName = name + "/" +"urlPage.txt"
		print (u"正在保存图片地址页：",fileName)
		#f.write(content.decode('utf-8'))
		# pre=pre.replace("[","")
		# pre=pre.replace("]","")+"\n"
		#print (pre)
		f = open(fileName,"w")
		f.write(Li)
		f.close()

		#追加方式写入当前爬行的名字，后续调用
		content=name+" "
		with open('url.txt', 'a') as url:
			url.write(content)
			url.close()
		print (name+u"追加完成！\n")

	#传入图片地址，文件名，保存单张图片
	def saveImg(self,imageURL,fileName):
		try:
			u = urllib2.urlopen(imageURL)
			data = u.read()
			f = open(fileName, 'wb')
			f.write(data)
			print (u"正在保存的一张图片为",fileName)
			f.close()
		except urllib2.URLError as e:
			 print (e.reason)

	#创建新目录
	def mkdir(self,path):
		path = path.strip()
		# 判断路径是否存在
		# 存在	 True
		# 不存在   False
		isExists=os.path.exists(path)
		# 判断结果
		if not isExists:
			# 如果不存在则创建目录
			print (u"新建了名字叫做",path,u'的文件夹')
			# 创建目录操作函数
			os.makedirs(path)
			return True
		else:
			# 如果目录存在则不创建，并提示目录已存在
			print (u"名为",path,'的文件夹已经创建成功')
			return False


	#将一页淘宝MM的信息保存起来
	def savePageInfo(self,pageIndex):
		#获取第一页淘宝MM列表
		contents = self.getContents(pageIndex)
		for item in contents:
			#item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
			print (u"发现一位名字叫",item[2],u"年龄",item[3],u",她在",item[4])
			print (u"正在保存",item[2],"的信息")

			print (u"个人详情地址是","https:"+str(item[0]))
			#个人详情页面的URL
			detailURL = "http:"+str(item[0])
			#得到个人详情页面代码
			detailPage = self.getDetailPage(detailURL)
			#获取个人简介
			brief = self.getBrief(detailPage)
			#获取所有图片列表
			images = self.getAllImg(detailPage)
			self.mkdir(item[2])
			#保存个人简介
			self.saveBrief(brief.encode('utf-8'),item[2])
			#保存图片地址页到本地
			self.saveToLocal(detailPage,item[2])
			#保存头像
			self.saveIcon("https:"+str(item[1]),item[2])

	#删除旧名单(如果有)
	def deleteOldTxt(self):
		filename = 'url.txt'
		if os.path.exists(filename):
			os.remove(filename)
			print("\n发现旧名单，已删除\n采集开始\n")

	#传入起止页码，获取MM页面保存
	def savePagesInfo(self,start,end):
		for i in range(start,end+1):
			print (u"正在寻找第",i,u"个地方")
			self.savePageInfo(i)
			#保存图片
			#self.saveImgs(images,item[2])

	#读取名字list
	def openNameList(self):
		with open("url.txt","r") as f:
			for line in f:
				line=line.strip()
				# line.split(",")
				# result.append(line)
				#result.append(line.split(","))
			#\s匹配空格与tab，\s+表示至少一个
			result=re.split(r'\s+',line)
		return result

	#逐个调取文件夹下页面中地址来保存
	def saveAll(self):
		i=spider.openNameList()
		for name in i:
			print ("当前正在保存的是"+name+"的图片")
			filepath=name+"/urlPage.txt"
			with open(filepath,"r") as urlContent:
				urlContent=urlContent.read()
			images=spider.getAllImg(urlContent)
			spider.saveImgs(images,name)


#传入起止页码即可，在此传入了6,10,表示抓取第6到10页的MM
spider = Spider()
spider.deleteOldTxt()
spider.savePagesInfo(6,10)
print("\n第一步保存信息完成，输入y保存所有图片，其他信息退出：")
a=input()
if a=='y':
	spider.saveAll()
else:
	pass