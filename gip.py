#!/usr/bin/env python3

import sys
from requests import get
from termcolor import colored

# The version of the program
version = "v0.1.3"

if not len(sys.argv) > 1:
    print(colored("You must specify an argument, try use help!", "red", attrs=["underline"]))
    exit()

if sys.argv[1] == "help": 
    print(colored("Commands: ip,version,help", "green"))
if sys.argv[1] == "version": 
    print(version)
    
if sys.argv[1] == "ip":

    if not len(sys.argv) > 2:
     ip = get('https://api.ipify.org').text
     print(ip)
    else:
     ip = sys.argv[2]
    result = get(f"http://ip-api.com/json/{ip}").json()
    if result["status"] != "success":
        print(colored("An error ocurred when finding that ip adress, check if the ip exists", "red", attrs=["underline"]))
        exit()

    print(colored("📡 IP: ", "red", attrs=["bold"])+ result["query"])
    print(colored("🌍 Country: ", "red", attrs=["bold"])+ result["country"] + " ("+result["countryCode"]+")")
    