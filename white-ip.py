import argparse
import requests, json
import sys
from sys import argv
import os


parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (yellow+"""

█───█ █──█ ─▀─ ▀▀█▀▀ █▀▀ 　 ─▀─ █▀▀█ 　 ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀█ 
█▄█▄█ █▀▀█ ▀█▀ ──█── █▀▀ 　 ▀█▀ █──█ 　 ──█── █▄▄▀ █▄▄█ █── █▀▀ █▄▄▀ 
─▀─▀─ ▀──▀ ▀▀▀ ──▀── ▀▀▀ 　 ▀▀▀ █▀▀▀ 　 ──▀── ▀─▀▀ ▀──▀ ▀▀▀ ▀▀▀ ▀─▀▀
"""+yellow)
print (lgreen+bold+"|||||||||||||| Author : white-eagle |||||||||||||||| \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        print("=====================================================")
        
        print ("Victim 		| ", data['query'])
        
        print("_____________________________________________________")
        
        print ("ISP		: ", data['isp'])
        
        print("_____________________________________________________")
        
        print ("Organisation	: ", data['org'])
        
        print("_____________________________________________________")
        
        print ("City		: ", data['city'])
        
        print("_____________________________________________________")
        
        print ("Region		: ", data['region'])
        
        print("_____________________________________________________")
        
        print ("Longitude	: ", data['lon'])
        
        print("_____________________________________________________")
        
        print ("Latitude	: ", data['lat'])
        
        print("_____________________________________________________")
        
        print ("Time zone	: ", data['timezone'])
        
        print("_____________________________________________________")
        
        print ("Zip code	: ", data['zip'])
        
        print("=====================================================")

except KeyboardInterrupt:
        print ('Exiting because of keyboard interrupt....'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"I think your internet connection is not good :)"+clear)
sys.exit(1)
