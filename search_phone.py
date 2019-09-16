import requests
url = "http://m.ip138.com/mobile.asp?"
try:
	phone_num = input("输入手机号码：") 
	kv = {'mobile': str(phone_num)}
	r = requests.get(url, params=kv)
	r.raise_for_status
	print(r.url)
	print(r.text[-500:])
except:
	print("查询失败")