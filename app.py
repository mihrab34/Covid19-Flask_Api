from flask import Flask, jsonify, request
from helper import fetchData, getDate

covidapp = Flask(__name__)

url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/"

todayDate = getDate()

@covidapp.route("/api/v1", methods=["GET"])
@covidapp.route("/api/v1/<date>", methods=["GET"])

def index(date=None):
	query_date = request.args.get("date")
	if date is None:
		if query_date is not None:
			d = query_date
		else:
			data = fetchData(url, date=query_date)
	else:
		data = fetchData(url, date)

	return jsonify({"total_cases": data})

if __name__ == "__main__":
	covidapp.run(debug=True)