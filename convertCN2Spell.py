#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: chl
#Email: haolin.chen1991@gmail.com
#2016.01.06 17:26

import re

def convertCN2Spell(ch, max = 5):
	"""
		该函数通过输入汉字返回其拼音，数字和字母会被跳过
	"""
	length = len('柯') #测试汉字占用字节数，utf-8，汉字占用3字节.bg2312，汉字占用2字节
	# intord = ord(ch[0:1])
	ret = ""
	regularCHN = re.compile(ur"[\u4e00-\u9fff]{1}")
	allCHNList = regularCHN.findall(ch.decode("utf-8"))

	allCHNList = allCHNList[0:max]

	# if (intord >= 48 and intord <= 57):
	# 	ret = ret + ch[0:1]
	# if (intord >= 65 and intord <=90 ) or (intord >= 97 and intord <=122):
	# 	ret = ret + ch[0:1].lower()
	# ch = ch[0:length] #多个汉字只获取第一个

	tempDist = {}
	with open(r'convert-utf-8.txt') as f:
		for line in f:
			for ch in allCHNList:
				chStr = ch.encode("utf-8")
				if chStr in line:
					if line.find(","):
						line = line[0:len(line)-2]			# -2是txt编码问题
					s = line.split(",")[0]					# 处理多音字情况
					# print s, len(s)
					tempDist[ch] = s[length:len(s)-1]		# -1是去掉音调
					# print tempDist[ch]

	for origin in allCHNList:
		ret = ret + tempDist[origin]
	return ret