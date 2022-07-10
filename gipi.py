#!/usr/bin/env python3
import sys
import os
from requests import get
from termcolor import colored
# Some important variables
version = "v0.2.2"
commands = ["help", "version", "contact", "ip", "uninstall"]
# The translations
pt = {
    "errors": {
        "noArgs": "Erro: Precisas de informar um argumento, usa gipi help para mais informações!",
        "commandNotExist": "Erro: Não encontramos o comando #cmd# usa gipi help para veres todos os comandos disponiveis",
        "noExistsIP": "Erro: Parece que esse ip não existe!",
    },
    "continent": "Continente: ",
    "country": "Pais: ",
    "region": "Distrito (Estado): ",
    "city": "Cidade: ",
    "currency": "Moeda: ",
    "zip": "Código Postal (CEP): ",
    "timezone": "Fuso Horário: "
}
en = {
    "errors": {
        "noArgs": "You must specify an argument, try use gipi help!",
        "commandNotExist": "Error: Commmand #cmd# not found, try to use gipi help to see all commands",
        "noExistsIP": "An error ocurred when finding that ip adress, check if the ip exists",
    
    },
    "continent": "Continent: ",
    "country": "Country: ",
    "region": "Distrito: ",
    "city": "City: ",
    "currency": "Currency: ",
    "zip": "ZIP: ",
    "timezone": "Timezone: "
}
# Check if the system language is portuguese and if not use english
if os.getenv('LANG').startswith("pt"):
    t = pt
else:
    t = en
if not len(sys.argv) > 1:
    print(colored(t["errors"]["noArgs"], "red", attrs=["underline"]))
    exit()
if not sys.argv[1] in commands:
   print(colored(t["errors"]["commandNotExist"].replace("#cmd#", f'"{sys.argv[1]}"'), "red", attrs=["bold"]))
if sys.argv[1] == "help":
    print(colored("ip,version,contact,uninstall,help", "green"))
if sys.argv[1] == "version" or sys.argv[1] == "v":
    print(version)
if sys.argv[1] == "contact":
    print(colored("Discord:", "yellow", attrs=["bold"]) + "\n" + colored("Canas#8888", "cyan", attrs=["bold"]) + "\n" + "---" + "\n" + colored("Support Server:", "yellow", attrs=["bold"]) + "\n" + colored(
        "https://discord.gg/aj3sSAyMsh", "cyan", attrs=["bold"]) + "\n" + "---" + "\n" + colored("Github:", "yellow", attrs=["bold"]) + "\n" + colored("https://github.com/davidcanas/gipi", "cyan", attrs=["bold"]))
if sys.argv[1] == "uninstall":
   print("Uninstalling GIPI, hope to see you again :)\nIf you're not happy with something create an issue on github")
   os.system("sudo rm /usr/bin/gipi")
   print("Sucessfully uninstalled gipi!")
if sys.argv[1] == "ip":
    if not len(sys.argv) > 2:
        ip = get('https://api.ipify.org').text
    else:
        ip = sys.argv[2]
    result = get(
        f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,currency,isp,org,as,query").json()
    if result["status"] != "success":
        print(colored(t["errors"]["noExistsIP"], "red", attrs=["underline"]))
        exit()
    print(colored("IP: ", "green", attrs=["bold"]) + result["query"])
    print(colored(t["continent"], "green", attrs=[
          "bold"]) + result["continent"] + " ("+result["continentCode"]+")")
    print(colored(t["country"], "green", attrs=[
          "bold"]) + result["country"] + " ("+result["countryCode"]+")")
    print(colored(t["region"], "green", attrs=["bold"]) + result["regionName"])
    print(colored(t["city"], "green", attrs=["bold"]) + result["city"])
    print(colored(t["zip"], "green", attrs=["bold"]) + result["zip"])
    print(colored(t["timezone"], "green", attrs=["bold"]) + result["timezone"])
    print(colored(t["currency"], "green", attrs=["bold"]) + result["currency"])
    print(colored("ISP: ", "green", attrs=["bold"]) + result["isp"])
    print(colored("ORG: ", "green", attrs=["bold"]) + result["org"])
