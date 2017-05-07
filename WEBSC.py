#!/usr/bin/python3
from main import *

about = """
+-------------------------------+
| SCRIPT : WEBSC                |
| BY : Aymen Benchiheub         |
| DATE : 07/05/2017             |
|                               |
|My Facebbok:			|
|   www.facebook.com/benchiehub |
+-------------------------------+

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
	w = whois(domain)
	# CREATE the folder where we save the files
	name = domain
	# write the informations into the file
	informations = [ip,n,w]
	name = str(name + time)
	#Create the dir
	create_dir(domain)
	for data in informations:
		write_file(name,data)
	bye()

#Get The Url From The User
print(about)
url = input('[+] - Please Put The Link Here => : ')
#Start !!!
if __name__ == '__main__':
	start(url)
