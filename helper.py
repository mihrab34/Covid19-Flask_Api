import csv
import requests
import datetime
from io import StringIO

countries = ["Benin", "Burkina Faso", "Cape Verde", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Cote d'Ivoire", "Liberia", "Mali", "Mauritania", "Niger", "Nigeria", "Senegal", "Sierra Leone","Togo"]

# method for formatting time using datetime
def getDate(no_of_days = 1):
	today = datetime.datetime.today()
	yesterday = today - datetime.timedelta(days = no_of_days)
	return yesterday.strftime("%m-%d-%Y")

# method for fetching decoding raw_data into data needed
def fetchData(url, date=None):
	data = []
	raw_data = requests.get(url+date+".csv").content.decode("ascii")
	decoded_data = StringIO(raw_data)

	actual_data = csv.reader(decoded_data)

	for item in actual_data:
		if item[3] in countries:
			print(decoded_data)
			data.append({"Country" : item[3], "Confirmed" : item[7], "Deaths": item[8], "Recovered": item[9], "Active": item[10]})
	return data