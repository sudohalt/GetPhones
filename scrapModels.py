#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2 
import re

# List of all the possible carriers that we could potentially care about
phoneCompanies = ['Acer', 'Alcatel', 'Allview', 'Amazon', 'Amoi', 'Apple', 'Archos', 'Asus', 'AT&T', 'Benefon', 'BenQ', 'BenQ-Siemens', 'Bird', 'BlackBerry', 'BLU', 'Bosch', 'Casio', 'Cat', 'Celkon', 'Chea', 'Dell', 'Emporia', 'Ericsson', 'Eten', 'FujitsuSiemens', 'Garmin-Asus', 'Gigabyte', 'Gionee', 'Haier', 'HP', 'HTC', 'Huawei', 'i-mate', 'i-mobile', 'Icemobile', 'Innostream', 'iNQ', 'Jolla', 'Karbonn', 'Kyocera', 'Lava', 'Lenovo', 'LG', 'Maxon', 'Maxwest', 'Meizu', 'Micromax', 'Microsoft', 'Mitac', 'Mitsubishi', 'Modu', 'Motorola', 'MWg', 'NEC', 'Neonode', 'NIU', 'Nokia', 'Nvidia', 'O2', 'OnePlus', 'Oppo', 'Orange', 'Palm', 'Panasonic', 'Pantech', 'Parla', 'Philips', 'Plum', 'Prestigio', 'Qtek', 'Sagem', 'Samsung', 'Sendo', 'Sewon', 'Sharp', 'Siemens', 'Sonim', 'Sony', 'SonyEricsson', 'Spice', 'T-Mobile', 'Tel.Me.', 'Telit', 'Thuraya', 'Toshiba', 'Unnecto', 'Vertu', 'verykool', 'Vivo', 'VKMobile', 'Vodafone', 'Wiko', 'WND', 'XCute', 'Xiaomi', 'XOLO', 'Yezz', 'ZTE']

# Change all to lowercase since the html page uses lower case phone names
phoneCompanies = [x.lower() for x in phoneCompanies]
# Start url of phone database
url = 'http://www.gsmarena.com/nokia-phones-%d.php'
# Url to use when continuing to the next pages
next_url = 'http://www.gsmarena.com/'
# SQL insert
start_id = 469
sql_insert = "INSERT INTO DEVICES(ID, TYPE, MANUFACTURER, MODEL) VALUES(%d, 'phone', '%s', '%s');"
# The site has 98 different phone companies
for i in range(2,12):
	# Get url
	response = urllib2.urlopen(url % i)
	# Get contents of page
	k = response.read()
	# The site has php files for each model, scrap these
	models = re.findall(r'[A-Za-z0-9_-]*.php', k);
	# Go throught the parsed input, and take the relevant data and parse it further
	for i in models:
		if 'phones' not in i and 'review' not in i:
			i = i.replace('-', ' ')
			i = i.replace('.php', '')
			i = i.replace('_', ' ')
			if i.split(' ')[0] in phoneCompanies:
				print sql_insert % (start_id, i.split(' ')[0], ' '.join(i.split(' ')[1:]))
				start_id += 1
#print "Commpany:" + i.split(' ')[0] + \
#					" Model:" + ' '.join(i.split(' ')[1:])
	while (True):
		next_page = re.findall(r'\"[A-Za-z0-9_-]*.php\" title=\"Next page\"', k) # title=\"Next Page\"', k)
		if next_page == []: break
		next_page = next_page[0].split(' title')[0]
		next_page = next_page.replace('"', '')
		# Repeat process done above
		response = urllib2.urlopen(next_url + next_page)
		k = response.read()
		models = re.findall(r'[A-Za-z0-9_-]*.php', k);
		# Go throught the parsed input, and take the relevant data and parse it further
		for i in models:
			if 'phones' not in i and 'review' not in i:
				i = i.replace('-', ' ')
				i = i.replace('.php', '')
				i = i.replace('_', ' ')
				if i.split(' ')[0] in phoneCompanies:
						print sql_insert % (start_id, i.split(' ')[0], ' '.join(i.split(' ')[1:]))
						start_id += 1
#response = urllib2.urlopen(url + next_page)
#		k = response.read()
		
