from bs4 import BeautifulSoup
import urllib.request
import re
import bs4

def Flights():
	
	url = "https://www.easemytrip.com/flights.html"
	page = urllib.request.urlopen(url) # conntect to website
	try:
	    page = urllib.request.urlopen(url)
	except:
	    print("An error occured.")

	soup = BeautifulSoup(page, 'html.parser')



	divTag = soup.find_all("div", {"class": "slider-wrap"})
	# print(divTag)

	package_names = []
	package_details = []
	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "offer-title"})
		for tag in tdTags: 
			package_names.append(tag.text)

	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "promo-code"})
		for tag in tdTags:
			# taggg = tag.find("div", {"class": "promo-code"})
			s = ''.join(e for e in tag if type(e) is bs4.element.NavigableString)
			package_details.append(s+" "+tag.find('p').text)
			# print(s)
			# print (tag.find('p').text) 

	for pack in range(len(package_names)):
		print(package_names[pack]+" "+package_details[pack])
def Hotels():

	url = "https://www.easemytrip.com/hotels/"
	page = urllib.request.urlopen(url) # conntect to website
	try:
	    page = urllib.request.urlopen(url)
	except:
	    print("An error occured.")

	soup = BeautifulSoup(page, 'html.parser')



	divTag = soup.find_all("div", {"class": "ofrblock"})
	# print(divTag)


	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "ofr_block_1"})
		for tag in tdTags: 
			print (re.sub("\s\s+", " ",tag.text))

	print("-------------------------------------------------------------------------")

def Buses():
	url = "https://www.easemytrip.com/bus/"
	page = urllib.request.urlopen(url) # conntect to website
	try:
	    page = urllib.request.urlopen(url)
	except:
	    print("An error occured.")

	soup = BeautifulSoup(page, 'html.parser')



	divTag = soup.find_all("div", {"class": "slider-wrap"})
	# print(divTag)


	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "new_hp_text"})
		for tag in tdTags: 
			print (re.sub("\s\s+", " ",tag.text))		



	print("-------------------------------------------------------------------------")

def HolidayPackages():
	url = "https://www.easemytrip.com/holiday-packages.html"
	page = urllib.request.urlopen(url) # conntect to website
	try:
	    page = urllib.request.urlopen(url)
	except:
	    print("An error occured.")

	soup = BeautifulSoup(page, 'html.parser')



	divTag = soup.find_all("div", {"class": "slider-wrap"})
	# print(divTag)


	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "img_hvr"})
		for tag in tdTags: 
			print (re.sub("\s\s+", " ",tag.text))		


print("-------------------------------------------------------------------------")	


def Cabs():

	url = "https://www.easemytrip.com/cabs"
	page = urllib.request.urlopen(url) # conntect to website
	try:
	    page = urllib.request.urlopen(url)
	except:
	    print("An error occured.")

	soup = BeautifulSoup(page, 'html.parser')



	divTag = soup.find_all("div", {"class": "ofrblock"})
	# print(divTag)


	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "ofr_block_1"})
		for tag in tdTags: 
			print (re.sub("\s\s+", " ",tag.text))

	print("----------------------------------------------------------------------------")

def Activities():

	url = "http://activities.easemytrip.com/"
	page = urllib.request.urlopen(url) # conntect to website
	try:
	    page = urllib.request.urlopen(url)
	except:
	    print("An error occured.")

	soup = BeautifulSoup(page, 'html.parser')



	divTag = soup.find_all("div", {"class": "carousel-inner"})
	# print(divTag)


	package_names = []
	package_details = []
	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "trav-list-bod"})
		for tag in tdTags: 
			package_names.append(re.sub("\s\s+", " ",tag.text))


	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "hot-page2-alp-ri-p3 tour-alp-ri-p3"})
		for tag in tdTags: 
			package_details.append(re.sub("\s\s+", " ",tag.text))

	no_of_packages = len(package_details)
	for pack in range(no_of_packages):
		print(package_names[pack]+" "+package_details[pack])

	print("-------------------------------------------------------------------------")


def ExpiredOffers():

	url = "https://www.easemytrip.com/offers/expired.html"
	page = urllib.request.urlopen(url) # conntect to website
	try:
	    page = urllib.request.urlopen(url)
	except:
	    print("An error occured.")

	soup = BeautifulSoup(page, 'html.parser')



	divTag = soup.find_all("div", {"class": "flt-rht-ar-bo"})
	# print(divTag)


	for tag in divTag:
		tdTags = tag.find_all("div", {"class": "offer-box"})
		for tag in tdTags: 
			print(re.sub("\s\s+", " ",tag.text))
			print("\n")
	

def SpecialOffers(category):

	if(category == 1):
		url = "https://www.easemytrip.com/offers/flights.html"
		page = urllib.request.urlopen(url) # conntect to website
		try:
		    page = urllib.request.urlopen(url)
		except:
		    print("An error occured.")

		soup = BeautifulSoup(page, 'html.parser')



		divTag = soup.find_all("div", {"class": "flt-rht-ar-bo"})
		# print(divTag)


		for tag in divTag:
			tdTags = tag.find_all("div", {"class": "offer-box"})
			for tag in tdTags: 
				print(re.sub("\s\s+", " ",tag.text))
	elif(category == 2):
		url = "https://www.easemytrip.com/offers/hotels.html"
		page = urllib.request.urlopen(url) # conntect to website
		try:
		    page = urllib.request.urlopen(url)
		except:
		    print("An error occured.")

		soup = BeautifulSoup(page, 'html.parser')



		divTag = soup.find_all("div", {"class": "flt-rht-ar-bo"})
		# print(divTag)


		for tag in divTag:
			tdTags = tag.find_all("div", {"class": "offer-box"})
			for tag in tdTags: 
				print(re.sub("\s\s+", " ",tag.text))
	elif(category == 3):
		url = "https://www.easemytrip.com/offers/bus.html"
		page = urllib.request.urlopen(url) # conntect to website
		try:
		    page = urllib.request.urlopen(url)
		except:
		    print("An error occured.")

		soup = BeautifulSoup(page, 'html.parser')



		divTag = soup.find_all("div", {"class": "flt-rht-ar-bo"})
		# print(divTag)


		for tag in divTag:
			tdTags = tag.find_all("div", {"class": "offer-box"})
			for tag in tdTags: 
				print(re.sub("\s\s+", " ",tag.text))
	elif(category == 4):
		url = "https://www.easemytrip.com/offers/cab.html"
		page = urllib.request.urlopen(url) # conntect to website
		try:
		    page = urllib.request.urlopen(url)
		except:
		    print("An error occured.")

		soup = BeautifulSoup(page, 'html.parser')



		divTag = soup.find_all("div", {"class": "flt-rht-ar-bo"})
		# print(divTag)


		for tag in divTag:
			tdTags = tag.find_all("div", {"class": "offer-box"})
			for tag in tdTags: 
				print(re.sub("\s\s+", " ",tag.text))
	elif(category == 5):
		url = "https://www.easemytrip.com/offers/hot-deals.html"
		page = urllib.request.urlopen(url) # conntect to website
		try:
		    page = urllib.request.urlopen(url)
		except:
		    print("An error occured.")

		soup = BeautifulSoup(page, 'html.parser')



		divTag = soup.find_all("div", {"class": "row-holidayd"})
		# print(divTag)


		for tag in divTag:
			tdTags = tag.find_all("div", {"class": "mask"})
			for tag in tdTags: 
				print(re.sub("\s\s+", " ",tag.text))
	



	

print("Welcome to Coupon Hunters")
print("We will Steal Coupons from easemytrip .....")
print("Which coupons you want to steal?")


while(True):
	
	print("Select 1 for FLIGHTS ")
	print("Select 2 for HOTELS ")
	print("Select 3 for BUSES ")
	print("Select 4 for HOLIDAYS ")
	print("Select 5 for CABS ")
	print("Select 6 for ACTIVITIES ")
	print("Select 7 for Special Offers")
	print("Select 8 for Expired Offers")
	print("Select 9 to Stop ")

	offersChoice = eval(input())
	if(offersChoice == 1):
		Flights()
	elif(offersChoice == 2):
		Hotels()
	elif(offersChoice == 3):
		Buses()
	elif(offersChoice == 4):
		HolidayPackages()
	elif(offersChoice == 5):
		Cabs()
	elif(offersChoice == 6):
		Activities()
	elif(offersChoice == 7):
		print("Select 1 for FLIGHTS ")
		print("Select 2 for HOTELS ")
		print("Select 3 for BUSES ")
		print("Select 4 for CABS ")
		print("Select 5 for Hot Deals")
		category = eval(input())
		SpecialOffers(category)
	elif(offersChoice == 8):
		ExpiredOffers()
	elif(offersChoice == 9):
		break

	print( "*****************************************************************\n")
print("------------------- Thanks -------------------")









