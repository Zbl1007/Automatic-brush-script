
#coding:utf-8
#!/usr/bin/env python

# 功能：自动接单！封装在wx.py文件中
# 平台：微信，金锦耀世环球平台
# 作者：Zbl
# 邮箱：1399853961@qq.com
# 使用注意事项: 为死循环，不间断接单，未完全关闭可能占用cpu资源


import wx
import time



while True:
	# ss方法中的数字意义： 1代表当日单。。2代表流量单。。3代表标签单。。4代表隔日单(目前3、4未测试，理论上不能使用)
	if (wx.ss(2)==1):
		break;
	time.sleep(0.5)
import a