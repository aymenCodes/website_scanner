import os
import time
from tld import get_tld

def get_local_time():
    date = time.localtime()
    day = "__%d_%d_%d"%(date[1],date[2],date[0])
    return day

def get_domain(url):
    # Just to Get The Domain Name !
    #example : google.com
    url = get_tld(url)
    return url

def get_ip(domain):
    # To Get The Ip adress
    command = "host " + domain
    process = os.popen(command)
    reusalt = str(process.read())
    return reusalt

def nmap(options,ip):
    # We Will scan The Websit By Nmap Tool
    # to get the open Ports And more Informations
    # About The Websit
    command = 'nmap ' + 'options ' + str(ip)
    process = os.popen(command)
    reusalt = str(process.read())
    return reusalt

def whois(ip):
    # We Will scan The Websit By Whois Tool
    # to get more Informations
    # About The Websit
    command = "whois " + ip
    process = os.popen(command)
    reusalt = str(process.read())
    return reusalt

def create_dir(directory):
    # Here we Will Creat A folder if is Not exists
    if not os.path.exists(directory):
        os.mkdir(directory)
        os.chdir(directory)

def write_file(name,data):
    # Create The TXT file where we will put
    # The Whole INFORMATIONS About The Website
    file = open(name + '.txt','a+')
    file.write(str(data) + "\n")
    file.close()

def bye():
    print('Exit Now...')
    time.sleep(1)
    print('Bye Press Enter To Exit...')
    x = input()
    exit()
# __The End__
