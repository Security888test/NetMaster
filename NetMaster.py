import urllib
import requests
from time import sleep
from colorama import Fore, Back, Style, init
import os

def Menu():
	print (Fore.WHITE + Style.BRIGHT + "   _   _      _  ___  ___          _            ")
	print ("  | \ | |    | | |  \/  |         | |           ")
	print ("  |  \| | ___| |_| .  . | __ _ ___| |_ ___ _ __ ")
	print ("  | . ` |/ _ \ __| |\/| |/ _` / __| __/ _ \ '__|")
	print ("  | |\  |  __/ |_| |  | | (_| \__ \ ||  __/ |   ")
	print ("  \_| \_/\___|\__\_|  |_/\__,_|___/\__\___|_|   ")
	print ("                                                ")
	print ("               V 1.3 - Adler - 2020             ")
	print ()

def Ask():
	print()
	query = input(Fore.WHITE + Style.BRIGHT + " Enter an IP Adress or a Domain Name to scan \n >>")

	if query == "":
		print(Fore.RED + Style.BRIGHT + " Error : Please enter a target.")
	else:
		urlstatus = "http://ip-api.com/csv/" + query + "?fields=status&lang=en"
		filestatus = urllib.request.urlopen(urlstatus)

		for line in filestatus:
			dcd_status = line.decode("utf-8")

		if "fail" in dcd_status:
			print(Fore.RED + Style.BRIGHT + "\n Error : Invalid or unreachable target.")
			Ask()
		else:
			print(Fore.BLUE + Style.BRIGHT + "\n [i] " + Fore.WHITE + "Starting scan...")

			print("")
			print(" OVERALL INFORMATIONS :")
			print("")
		
			urlip = "http://ip-api.com/csv/" + query + "?fields=query&lang=en"
			fileip = urllib.request.urlopen(urlip)

			for line in fileip:
				dcd_ip = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " IP Adress : " + dcd_ip, end="")

			urlmob = "http://ip-api.com/csv/" + query + "?fields=mobile&lang=en"
			filemob = urllib.request.urlopen(urlmob)

			for line in filemob:
				dcd_mob = line.decode("utf-8")

				if "false" in dcd_mob:
					print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Mobile : No")
				elif "true" in dcd_mob:
					print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Mobile : Yes")
				else:
					print(Fore.YELLOW + Style.BRIGHT + " [*]" + Fore.WHITE + " Mobile : Unknown")

			urlisp = "http://ip-api.com/csv/" + query + "?fields=isp&lang=en"
			fileisp = urllib.request.urlopen(urlisp)

			for line in fileisp:
				dcd_isp = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Internet Service Provider [I.S.P.] : " + dcd_isp, end="")
				
			urlorg = "http://ip-api.com/csv/" + query + "?fields=org&lang=en"
			fileorg = urllib.request.urlopen(urlorg)

			for line in fileorg:
				dcd_org = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Organisation : " + dcd_org, end="")
				
			urlas = "http://ip-api.com/csv/" + query + "?fields=as&lang=en"
			fileas = urllib.request.urlopen(urlas)

			for line in fileas:
				dcd_as = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Autonomous System : " + dcd_as, end="")

			urlasn = "http://ip-api.com/csv/" + query + "?fields=asname&lang=en"
			fileasn = urllib.request.urlopen(urlasn)

			for line in fileasn:
				dcd_asn = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Autonomous System Name : " + dcd_asn, end="")

			print("")
			print(" GEOGRAPHICAL INFORMATIONS :")
			print("")

			urlc = "http://ip-api.com/csv/" + query + "?fields=continent&lang=en"
			filec = urllib.request.urlopen(urlc)

			for line in filec:
				dcd_c = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Continent : " + dcd_c, end="")

			urlcc = "http://ip-api.com/csv/" + query + "?fields=continentCode&lang=en"
			filecc = urllib.request.urlopen(urlcc)

			for line in filecc:
				dcd_cc = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Continental Code : " + dcd_cc, end="")

			urlnation = "http://ip-api.com/csv/" + query + "?fields=country&lang=en"
			filenation = urllib.request.urlopen(urlnation)

			for line in filenation:
				dcd_nation = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Country : " + dcd_nation, end="")

			urlcnation = "http://ip-api.com/csv/" + query + "?fields=countryCode&lang=en"
			filecnation = urllib.request.urlopen(urlcnation)

			for line in filecnation:
				dcd_cnation = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Country Code : " + dcd_cnation, end="")

			urlregion = "http://ip-api.com/csv/" + query + "?fields=regionName&lang=en"
			fileregion = urllib.request.urlopen(urlregion)

			for line in fileregion:
				dcd_region = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Region : " + dcd_region, end="")

			urlrcegion = "http://ip-api.com/csv/" + query + "?fields=region&lang=en"
			filecregion = urllib.request.urlopen(urlrcegion)

			for line in filecregion:
				dcd_cregion = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " Region code : " + dcd_cregion, end="")

			urlrzip = "http://ip-api.com/csv/" + query + "?fields=zip&lang=en"
			filezip = urllib.request.urlopen(urlrzip)

			for line in filezip:
				dcd_zip = line.decode("utf-8")
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " ZIP Code : " + dcd_zip, end="")

			print("")
			print(" DNS INFORMATIONS :")
			print("")

			urlrdnsa = "https://api.hackertarget.com/dnslookup/?q=" + query
			filednsa = urllib.request.urlopen(urlrdnsa)

			for line in filednsa:
				dcd_dnsa = line.decode("utf-8")

			if "try" in dcd_dnsa:
				print(Fore.YELLOW + Style.BRIGHT + " Only available with Domain Names.")
			else:
				print(Fore.GREEN + Style.BRIGHT + " [+]" + Fore.WHITE + " " + dcd_dnsa)
			
			print("")
			print(Fore.BLUE + Style.BRIGHT + " [i] " + Fore.WHITE + "Scan done." + Fore.WHITE)

			print("")
			rep = input(" Would you like to scan another target ? [Y/n] >>")

			if rep == "Y":
				Ask()
			elif rep == "y":
				Ask()
			elif rep == "Yes":
				Ask()
			elif rep == "yes":
				Ask()
			elif rep == "":
				Ask()
			elif rep == "n":
				print (Fore.RED + Style.BRIGHT + "\n Exiting...")
				exit()
			elif rep == "N":
				print (Fore.RED + Style.BRIGHT + "\n Exiting...")
				exit()
			elif rep == "No":
				print (Fore.RED + Style.BRIGHT + "\n Exiting...")
				exit()
			elif rep == "no":
				print (Fore.RED + Style.BRIGHT + "\n Exiting...")
				exit()

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

Menu()
print( " Welcome on the NetMaster - By Adler - [V 1.0] \n")
Ask()