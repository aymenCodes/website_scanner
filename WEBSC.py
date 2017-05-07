from main import *


about = """
+-------------------------------+
| SCRIPT : Website Scanner      |
| BY : Aymen Benchiheub         |
| DATE : 23/04/2017             |
|                               |
|My Facebbok:			|
|   www.facebook.com/benchiehub |
+-------------------------------+

===================================================
= Dedication For : Zinou Elgahri And Isaac Lee <3 =
===================================================

"""

def start(url):
	time = get_local_time()
	# Just to Get The Domain Name !
	domain = get_domain(url)
	# To Get The Ip adress
	ip = get_ip(domain)
	# Start Scaning The Website using Nmap Tool
	n = nmap("-F",ip)
	#Scaning The Website using Whois Tool
	whois = whois(ip)
	# CREATE the folder where we save the files
	name = domain
	# write the informations into the file
	informations = [ip,n,whois]
	for data in informations:
		write_file(name + time,data)

#Get The Url From The User
print(about)
url = input('[+]Please Put The Link Here ==> : ')
#Start !!!

start(url)
