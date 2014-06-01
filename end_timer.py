import json, checkmetools

#### FUNCTION DEFINITIONS
def endTimer(data, current_time):
	start = data[0]['start_time']
	pause = data[0]['pause']

	total_workspan = checkmetools.timeDifference(current_time, start)
	total_timespan = total_workspan - computeTotalPause(pause)
	
	data[0]['total_workspan'] = total_workspan
	data[0]['total_timespan'] = total_timespan
	data[0]['end_time'] = current_time
	return data

def computeTotalPause(pause_obj):
	if pause_obj is None:
		return 0
	else:
		total = 0
		for pause in pause_obj:
			total += pause['duration']
		return total

#### MAIN
def run():
	current_time, date = checkmetools.getTimeDate()
	data_path = checkmetools.createPath()

	with open(data_path, "r+") as data_json:
		working_time = json.load(data_json)
		data_json.seek(0)
		working_time = endTimer(working_time, current_time)
		json.dump(working_time, data_json, indent=2)
		data_json.truncate()