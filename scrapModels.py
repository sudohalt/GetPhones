import urllib2 
import re

phoneCompanies = ['Acer', 'Alcatel', 'Allview', 'Amazon', 'Amoi', 'Apple', 'Archos', 'Asus', 'AT&T', 'Benefon', 'BenQ', 'BenQ-Siemens', 'Bird', 'BlackBerry', 'BLU', 'Bosch', 'Casio', 'Cat', 'Celkon', 'Chea', 'Dell', 'Emporia', 'Ericsson', 'Eten', 'FujitsuSiemens', 'Garmin-Asus', 'Gigabyte', 'Gionee', 'Haier', 'HP', 'HTC', 'Huawei', 'i-mate', 'i-mobile', 'Icemobile', 'Innostream', 'iNQ', 'Jolla', 'Karbonn', 'Kyocera', 'Lava', 'Lenovo', 'LG', 'Maxon', 'Maxwest', 'Meizu', 'Micromax', 'Microsoft', 'Mitac', 'Mitsubishi', 'Modu', 'Motorola', 'MWg', 'NEC', 'Neonode', 'NIU', 'Nokia', 'Nvidia', 'O2', 'OnePlus', 'Oppo', 'Orange', 'Palm', 'Panasonic', 'Pantech', 'Parla', 'Philips', 'Plum', 'Prestigio', 'Qtek', 'Sagem', 'Samsung', 'Sendo', 'Sewon', 'Sharp', 'Siemens', 'Sonim', 'Sony', 'SonyEricsson', 'Spice', 'T-Mobile', 'Tel.Me.', 'Telit', 'Thuraya', 'Toshiba', 'Unnecto', 'Vertu', 'verykool', 'Vivo', 'VKMobile', 'Vodafone', 'Wiko', 'WND', 'XCute', 'Xiaomi', 'XOLO', 'Yezz', 'ZTE']

# Change all to lowercase since the html page uses lower case phone names
phoneCompanies = [x.lower() for x in phoneCompanies]
# Url of phone database
url = 'http://www.gsmarena.com/nokia-phones-%d.php'
# The site has 98 different phone companies
for i in range(1,99):
	# Get url
	response = urllib2.urlopen(url % i)
	# Get contents of page
	k = response.read()
	# The site has php files for each model, scrap these
	models = re.findall(r'[A-Za-z0-9_-]*.php', k);
	for i in models:
		if 'phones' not in i and 'review' not in i:
			i = i.replace('-', ' ')
			i = i.replace('.php', '')
			i = i.replace('_', ' ')
			if i.split(' ')[0] in phoneCompanies:
				print "Company:" + i.split(' ')[0] + \
					" Model:" + ' '.join(i.split(' ')[1:])
