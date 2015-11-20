from views 


def get_forecast():
# put together variables for the API call and save to a dict
# TODO :add error handling if response != 200
api_date_range = str(depart_date.month) + str(depart_date.day) + str(return_date.month) + str(return_date.day)
api_call = API_URL % (WU_KEY, api_date_range, destination)
api_data = requests.get(api_call).json()

return forecast = {
		'max_temp_f': int(api_data[u'trip'][u'temp_high'][u'max'][u'F']),
		'max_temp_c': int(api_data[u'trip'][u'temp_high'][u'max'][u'C']),
		'avg_temp_f': int(api_data[u'trip'][u'temp_high'][u'avg'][u'F']),
		'avg_temp_c': int(api_data[u'trip'][u'temp_high'][u'avg'][u'C']),
		'min_temp_f': int(api_data[u'trip'][u'temp_low'][u'min'][u'F']),
		'min_temp_f': int(api_data[u'trip'][u'temp_low'][u'min'][u'C']),					
		'precip': int(api_data[u'trip'][u'chance_of'][u'chanceofrainday'][u'percentage']),
		'snow': int(api_data[u'trip'][u'chance_of'][u'chanceofsnowday'][u'percentage'])
		}

# categorize forecast variables into temp categories
if forecast['avg_temp_f'] >= 90:
	temp_cat = 'temp_high'
elif forecast['avg_temp_f'] < 90 and forecast['avg_temp_f'] >= 80:
	temp_cat = 'temp_medhigh'
elif forecast['avg_temp_f'] < 80 and forecast['avg_temp_f'] >= 60:
	temp_cat = 'temp_temp'
elif forecast['avg_temp_f'] < 60 and forecast['avg_temp_f'] >= 50:
	temp_cat = 'temp_medcold'
else:
	temp_cat = 'temp_cold'