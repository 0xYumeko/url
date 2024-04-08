try:
	import requests
	from time import sleep
	from bs4 import BeautifulSoup
	from os import system
except Exception as Wl:
	print(" MISSING LIB , ",Wl)
	exit()
	
system('clear')
def helltakerc3rb():
	print('''
                  【0】【x】【3】【f】【3】【c】
	   
	\033[2;36murl \033[1;97mHelltakerC3rb
	''')
	
	ur = input('\n\033[2;32murl '+'\033[1;97m:\033[2;34m ')
	url = "https://cutt.us/processreq.php"
	r = requests.get(url)
	k = BeautifulSoup(r.text,"html5lib")
	to = k.find('input',{'type':'text' ,'name':'txt_name' ,'id':'txt_name'})['value']
	headers = {
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'ar',
		'Connection': 'keep-alive',
		'Content-Length': '65',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': 'PHPSESSID=cc1dadfab59e5cc33c67b707ec3e46b6; __utma=255283994.84811555.1654465762.1654465762.1654465762.1; __utmc=255283994; __utmz=255283994.1654465762.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=255283994.1.10.1654465762',
		'Host': 'cutt.us',
		'Origin': 'https://cutt.us',
		'Referer': 'https://cutt.us/',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
	}
	data = {
		'txt_url': ur,
		'txt_name': to
	}
	
	R = requests.post(url, headers=headers,data=data)
	
	if 'If ' ' check the link entered.!!' in R.text:
		print('\n\033[2;32m[\033[1;97m-\033[2;32m] \033[1;31mCheck the entered link')
		sleep(0.70)
		print('\n\033[2;32m[\033[1;97m+\033[2;32m]\033[1;97m Do you want to restart the tool?')
		sleep(0.5)		
		v = input('‏​‏\n\033[2;32m[\033[1;97m+\033[2;32m]\033[2;35m \033[2;34my\033[1;97m/\033[1;31mn \033[1;97m: \033[2;32m')
		if v == 'y':
			sleep(0.70)
			system('clear')
			helltakerc3rb()
		elif v == 'n':
			sleep(0.70)
			print('\n\033[2;32m[\033[1;97m+\033[2;32m]\033[1;97m see you later\033[2;32m\n')
			sleep(0.4)
			exit()
		else:
			sleep(0.70)
			print(f'\n\033[2;32m[\033[1;97m-\033[2;32m]\033[1;97m There is no such option [\033[1;31m{v}\033[1;97m]\n\033[2;32m')
			sleep(0.4)
			exit()
	else:
		try:
			X = BeautifulSoup(R.text,"html5lib")
			T = X.find('input',{'dir':'ltr'})['value']
			Awham = T.split('/')[3]
			print(f'\n\033[2;32m[\033[1;97m+\033[2;32m] \033[2;35mhttps\033[1;97m:\033[1;31m//\033[2;36mcutt\033[1;97m.\033[2;36mus\033[1;31m/\033[2;36m{helltakerc3rb}')
			sleep(0.4)
			print('\n\033[2;32m[\033[1;97m+\033[2;32m]\033[1;97m see you later\n\033[2;32m')
			sleep(0.4)
		except Exception:
			print('\n\033[2;32m[\033[1;97m-\033[2;32m]\033[1;31m Error\n\033[2;32m')
			sleep(0.4)
			exit()
helltakerc3rb()
